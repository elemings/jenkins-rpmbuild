
top_srcdir=.
srcdir=.

# same variable names used internally by rpm
_topdir=$(srcdir)
_builddir=$(_topdir)/BUILD
_buildrootdir=$(_topdir)/BUILDROOT
_rpmdir=$(_topdir)/RPMS
_sourcedir=$(_topdir)/SOURCES
_specdir=$(_topdir)/SPECS
_srcrpmdir=$(_topdir)/SRPMS

WGET = wget
CURL = curl -kLs
DOWNLOAD = $(CURL)

SPECTOOL = spectool
SPECTOOL_FLAGS = -g -C $(_sourcedir)

OPENSSL = openssl
KEYTOOL = keytool

RPMBUILD = rpmbuild
RPMBUILD_DEFS = --define '_topdir $(shell realpath $(srcdir))'
RPMBUILD_FLAGS = -v -ba --clean $(RPMBUILD_DEFS)

BUILD.rpm = $(RPMBUILD) $(RPMBUILD_FLAGS)

RHEL = $(shell uname -r|grep -o 'el[0-9]')

# targets

JENKINS_DIST_URL=http://mirrors.jenkins.io/war-stable
# prepare yourself (is there an easier way?)
JENKINS_LATEST_RELEASE=$(shell \
	curl -L $(JENKINS_DIST_URL) 2>/dev/null\
	|grep 'href="2'\
	|tail -1\
	|grep -o '[0-9]*\.[0-9]*\.[0-9]*'\
	|uniq)
JENKINS_DEFS = --define 'version $(JENKINS_LATEST_RELEASE)'

RPMBUILD_FLAGS += $(JENKINS_DEFS)
SPECTOOL_FLAGS += $(JENKINS_DEFS)

JENKINS_SPEC = $(_specdir)/jenkins.spec
JENKINS_PLUGINS_SPEC = $(_specdir)/jenkins-plugins.spec

JENKINS_DL_SOURCES = \
	$(_sourcedir)/jenkins.war
JENKINS_KS_SOURCES = \
	$(_sourcedir)/jenkins.jks
JENKINS_VC_SOURCES = \
	$(_sourcedir)/jenkins.init.in \
	$(_sourcedir)/jenkins.logrotate \
	$(_sourcedir)/jenkins.prestart.in \
	$(_sourcedir)/jenkins.service.in \
	$(_sourcedir)/jenkins.sysconfig.in

JENKINS_KEY = $(_sourcedir)/jenkins.key
JENKINS_CERT = $(_sourcedir)/jenkins.crt
JENKINS_PKCS12 = $(_sourcedir)/jenkins.p12
JENKINS_PKCS12_NAME = -name jenkins
JENKINS_JKS = $(_sourcedir)/jenkins.jks

include Makefile.jenkins-plugins
JENKINS_PLUGINS_URL = https://updates.jenkins-ci.org/download/plugins
JENKINS_PLUGINS_DL_SOURCES = \
	$(addsuffix .hpi,$(addprefix $(_sourcedir)/,$(notdir $(JENKINS_PLUGINS))))

JENKINS_SOURCES = \
	$(JENKINS_DL_SOURCES) \
	$(JENKINS_KS_SOURCES) \
	$(JENKINS_VC_SOURCES)
JENKINS_PLUGINS_SOURCES = \
	$(JENKINS_PLUGINS_DL_SOURCES) \
	$(JENKINS_PLUGINS_VC_SOURCES)
SOURCES = \
	$(JENKINS_SOURCES) \
	$(JENKINS_PLUGINS_SOURCES)

JENKINS_RPMS = \
	$(_rpmdir)/noarch/jenkins-$(JENKINS_LATEST_RELEASE)-1.$(RHEL).noarch.rpm
JENKINS_PLUGINS_RPMS = \
	$(_rpmdir)/noarch/jenkins-plugins-$(JENKINS_LATEST_RELEASE)-1.$(RHEL).noarch.rpm
RPMS = \
	$(JENKINS_RPMS) \
	$(JENKINS_PLUGINS_RPMS)

JENKINS_SRPM_FILE = \
	$(_srcrpmdir)/jenkins-$(JENKINS_LATEST_RELEASE)-1.$(RHEL).src.rpm
JENKINS_PLUGINS_SRPM_FILE = \
	$(_srcrpmdir)/jenkins-plugins-$(JENKINS_LATEST_RELEASE)-1.$(RHEL).src.rpm
SRPMS = \
	$(JENKINS_SRPM_FILE) \
	$(JENKINS_PLUGINS_SRPM_FILE)

TARGETS = \
	$(RPMS) \
	$(SRPMS)

.PHONY: all clean distclean plugins resign

all: $(TARGETS)

$(JENKINS_RPMS) $(JENKINS_SRPM_FILE): $(JENKINS_SOURCES) $(JENKINS_SPEC)
	$(BUILD.rpm) $(JENKINS_SPEC)
$(JENKINS_PLUGINS_RPMS) $(JENKINS_PLUGINS_SRPM_FILE): $(JENKINS_PLUGINS_SOURCES) $(JENKINS_PLUGINS_SPEC)
	$(BUILD.rpm) $(JENKINS_PLUGINS_SPEC)

$(JENKINS_DL_SOURCES): $(JENKINS_SPEC)
	$(SPECTOOL) $(SPECTOOL_FLAGS) $^

# There are various ways to create a Jenkins keystore.  The following
# rules create, bundle, and import a private key and self-signed certifcate.
$(JENKINS_KEY) $(JENKINS_CERT):
	$(OPENSSL) req -newkey rsa:4096 -nodes -keyout $(JENKINS_KEY) -x509 -days 365 -out $(JENKINS_CERT)
$(JENKINS_PKCS12): $(JENKINS_KEY) $(JENKINS_CERT)
	$(OPENSSL) pkcs12 -export -inkey $(JENKINS_KEY) -in $(JENKINS_CERT) -out $(JENKINS_PKCS12) $(JENKINS_PKCS12_NAME)
$(JENKINS_JKS): $(JENKINS_PKCS12)
	$(KEYTOOL) -importkeystore -srckeystore $(JENKINS_PKCS12) -srcstoretype pkcs12 -destkeystore $(JENKINS_JKS) -deststoretype JKS

plugins: Makefile.jenkins-plugins
	@i=1; for jp in $(JENKINS_PLUGINS); do \
	  printf "Source%d:\t%s/%s/%s.hpi\n" $$i $(JENKINS_PLUGINS_URL) `basename $$jp` $$jp; \
	  (( ++i )); \
	done

#$(JENKINS_PLUGINS_DL_SOURCES): $(JENKINS_PLUGINS_SPEC)
#	$(SPECTOOL) $(SPECTOOL_FLAGS) $^
$(JENKINS_PLUGINS_DL_SOURCES):
	$(SPECTOOL) $(SPECTOOL_FLAGS) $(JENKINS_PLUGINS_SPEC)

resign: $(RPMS) $(SRPMS)
	rpm --resign $^

config:
	@echo "RHEL=$(RHEL)"
	@echo "_topdir=$(_topdir)"
	@echo "JENKINS_DIST_URL=$(JENKINS_DIST_URL)"
	@echo "JENKINS_LATEST_RELEASE=$(JENKINS_LATEST_RELEASE)"
	@echo "RPMS=$(RPMS)"
	@echo "SRPMS=$(SRPMS)"
	@echo "TARGETS=$(TARGETS)"
	@echo "JENKINS_PLUGINS_DL_SOURCES=$(JENKINS_PLUGINS_DL_SOURCES)"

clean:
	-$(RM) $(TARGETS)
distclean: clean
	-$(RM) $(JENKINS_DL_SOURCES) $(JENKINS_PLUGINS_DL_SOURCES)
	-$(RM) $(JENKINS_KEY) $(JENKINS_CERT) $(JENKINS_PKCS12) $(JENKINS_JKS)

