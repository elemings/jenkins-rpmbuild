
#%define workdir %{_var}/lib/jenkins # it changed from 2.150.3 to 2.164.1
%define workdir %{_var}/lib/jenkins/.jenkins

Name:       jenkins-plugins
Version:    2.164.1.1554405920
Release:    3%{?dist}
Summary:    Jenkins plugin bundle
Group:      Development/Tools/Building
License:    ASL 2.0
BuildArch:  noarch
Requires:   jenkins >= 2.164.1

URL:        https://updates.jenkins-ci.org/download/plugins
Source0:    https://updates.jenkins-ci.org/latest/ace-editor.hpi
Source1:    https://updates.jenkins-ci.org/latest/ant.hpi
Source2:    https://updates.jenkins-ci.org/latest/antisamy-markup-formatter.hpi
Source3:    https://updates.jenkins-ci.org/latest//apache-httpcomponents-client-4-api.hpi
Source4:    https://updates.jenkins-ci.org/latest/authentication-tokens.hpi
Source5:    https://updates.jenkins-ci.org/latest//bouncycastle-api.hpi
Source6:    https://updates.jenkins-ci.org/latest/branch-api.hpi
Source7:    https://updates.jenkins-ci.org/latest/build-timeout.hpi
Source8:    https://updates.jenkins-ci.org/latest/clearcase.hpi
Source9:    https://updates.jenkins-ci.org/latest/cloudbees-folder.hpi
Source10:    https://updates.jenkins-ci.org/latest/command-launcher.hpi
Source11:    https://updates.jenkins-ci.org/latest/credentials-binding.hpi
Source12:    https://updates.jenkins-ci.org/latest/credentials.hpi
Source13:    https://updates.jenkins-ci.org/latest/display-url-api.hpi
Source14:    https://updates.jenkins-ci.org/latest/docker-commons.hpi
Source15:    https://updates.jenkins-ci.org/latest/docker-workflow.hpi
Source16:    https://updates.jenkins-ci.org/latest/durable-task.hpi
Source17:    https://updates.jenkins-ci.org/latest/email-ext.hpi
Source18:    https://updates.jenkins-ci.org/latest/external-monitor-job.hpi
Source19:    https://updates.jenkins-ci.org/latest/git-client.hpi
Source20:    https://updates.jenkins-ci.org/latest/git.hpi
Source21:    https://updates.jenkins-ci.org/latest/git-server.hpi
Source22:    https://updates.jenkins-ci.org/latest/handlebars.hpi
Source23:    https://updates.jenkins-ci.org/latest/jackson2-api.hpi
Source24:    https://updates.jenkins-ci.org/latest/javadoc.hpi
Source25:    https://updates.jenkins-ci.org/latest/jdk-tool.hpi
Source26:    https://updates.jenkins-ci.org/latest/jira.hpi
Source27:    https://updates.jenkins-ci.org/latest/jquery.hpi
Source28:    https://updates.jenkins-ci.org/latest/jquery-detached.hpi
Source29:    https://updates.jenkins-ci.org/latest/jquery-ui.hpi
Source30:    https://updates.jenkins-ci.org/latest/jsch.hpi
Source31:    https://updates.jenkins-ci.org/latest/junit.hpi
Source32:    https://updates.jenkins-ci.org/latest/ldap.hpi
Source33:    https://updates.jenkins-ci.org/latest/lockable-resources.hpi
Source34:    https://updates.jenkins-ci.org/latest/mailer.hpi
Source35:    https://updates.jenkins-ci.org/latest/matrix-auth.hpi
Source36:    https://updates.jenkins-ci.org/latest/matrix-project.hpi
Source37:    https://updates.jenkins-ci.org/latest/momentjs.hpi
Source38:    https://updates.jenkins-ci.org/latest/pam-auth.hpi
Source39:    https://updates.jenkins-ci.org/latest/pipeline-build-step.hpi
Source40:    https://updates.jenkins-ci.org/latest/pipeline-graph-analysis.hpi
Source41:    https://updates.jenkins-ci.org/latest/pipeline-input-step.hpi
Source42:    https://updates.jenkins-ci.org/latest/pipeline-milestone-step.hpi
Source43:    https://updates.jenkins-ci.org/latest/pipeline-model-api.hpi
Source44:    https://updates.jenkins-ci.org/latest/pipeline-model-declarative-agent.hpi
Source45:    https://updates.jenkins-ci.org/latest/pipeline-model-definition.hpi
Source46:    https://updates.jenkins-ci.org/latest/pipeline-model-extensions.hpi
Source47:    https://updates.jenkins-ci.org/latest/pipeline-rest-api.hpi
Source48:    https://updates.jenkins-ci.org/latest/pipeline-stage-step.hpi
Source49:    https://updates.jenkins-ci.org/latest/pipeline-stage-tags-metadata.hpi
Source50:    https://updates.jenkins-ci.org/latest/pipeline-stage-view.hpi
Source51:    https://updates.jenkins-ci.org/latest/plain-credentials.hpi
Source52:    https://updates.jenkins-ci.org/latest/pubsub-light.hpi
Source53:    https://updates.jenkins-ci.org/latest/resource-disposer.hpi
Source54:    https://updates.jenkins-ci.org/latest/role-strategy.hpi
Source55:    https://updates.jenkins-ci.org/latest/scm-api.hpi
Source56:    https://updates.jenkins-ci.org/latest/script-security.hpi
Source57:    https://updates.jenkins-ci.org/latest/ssh.hpi
Source58:    https://updates.jenkins-ci.org/latest/ssh-agent.hpi
Source59:    https://updates.jenkins-ci.org/latest/ssh-credentials.hpi
Source60:    https://updates.jenkins-ci.org/latest/ssh-slaves.hpi
Source61:    https://updates.jenkins-ci.org/latest/structs.hpi
Source62:    https://updates.jenkins-ci.org/latest/timestamper.hpi
Source63:    https://updates.jenkins-ci.org/latest/token-macro.hpi
Source64:    https://updates.jenkins-ci.org/latest/workflow-aggregator.hpi
Source65:    https://updates.jenkins-ci.org/latest/workflow-api.hpi
Source66:    https://updates.jenkins-ci.org/latest/workflow-basic-steps.hpi
Source67:    https://updates.jenkins-ci.org/latest/workflow-cps-global-lib.hpi
Source68:    https://updates.jenkins-ci.org/latest/workflow-cps.hpi
Source69:    https://updates.jenkins-ci.org/latest/workflow-durable-task-step.hpi
Source70:    https://updates.jenkins-ci.org/latest/workflow-job.hpi
Source71:    https://updates.jenkins-ci.org/latest/workflow-multibranch.hpi
Source72:    https://updates.jenkins-ci.org/latest/workflow-scm-step.hpi
Source73:    https://updates.jenkins-ci.org/latest/workflow-step-api.hpi
Source74:    https://updates.jenkins-ci.org/latest/workflow-support.hpi
Source75:    https://updates.jenkins-ci.org/latest/ws-cleanup.hpi

%description
Plugins are the primary means of enhancing the functionality of a
Jenkins environment to suit organization- or user-specific needs. There
are over a thousand different plugins which can be installed on a
Jenkins master and to integrate various build tools, cloud providers,
analysis tools, and much more.

This Jenkins plugin bundle is specifically tailored for NG MS Boulder.

%prep

%build

%install
rm -rf %{buildroot}
%__install -d -m0755 %{buildroot}%{workdir}/plugins
%__install -D -m0644 %{SOURCE0} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE1} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE2} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE3} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE4} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE5} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE6} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE7} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE8} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE9} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE10} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE11} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE12} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE13} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE14} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE15} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE16} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE17} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE18} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE19} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE20} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE21} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE22} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE23} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE24} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE25} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE26} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE27} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE28} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE29} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE30} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE31} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE32} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE33} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE34} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE35} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE36} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE37} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE38} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE39} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE40} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE41} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE42} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE43} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE44} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE45} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE46} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE47} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE48} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE49} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE50} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE51} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE52} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE53} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE54} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE55} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE56} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE57} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE58} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE59} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE60} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE61} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE62} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE63} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE64} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE65} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE66} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE67} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE68} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE69} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE70} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE71} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE72} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE73} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE74} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE75} %{buildroot}%{workdir}/plugins/


%files
%defattr(-,jenkins,jenkins)
%dir %{workdir}
%dir %{workdir}/plugins
%{workdir}/plugins/ace-editor.hpi
%{workdir}/plugins/ant.hpi
%{workdir}/plugins/antisamy-markup-formatter.hpi
%{workdir}/plugins/apache-httpcomponents-client-4-api.hpi
%{workdir}/plugins/authentication-tokens.hpi
%{workdir}/plugins/bouncycastle-api.hpi
%{workdir}/plugins/branch-api.hpi
%{workdir}/plugins/build-timeout.hpi
%{workdir}/plugins/clearcase.hpi
%{workdir}/plugins/cloudbees-folder.hpi
%{workdir}/plugins/command-launcher.hpi
%{workdir}/plugins/credentials-binding.hpi
%{workdir}/plugins/credentials.hpi
%{workdir}/plugins/display-url-api.hpi
%{workdir}/plugins/docker-commons.hpi
%{workdir}/plugins/docker-workflow.hpi
%{workdir}/plugins/durable-task.hpi
%{workdir}/plugins/email-ext.hpi
%{workdir}/plugins/external-monitor-job.hpi
%{workdir}/plugins/git-client.hpi
%{workdir}/plugins/git.hpi
%{workdir}/plugins/git-server.hpi
%{workdir}/plugins/handlebars.hpi
%{workdir}/plugins/jackson2-api.hpi
%{workdir}/plugins/javadoc.hpi
%{workdir}/plugins/jdk-tool.hpi
%{workdir}/plugins/jira.hpi
%{workdir}/plugins/jquery.hpi
%{workdir}/plugins/jquery-detached.hpi
%{workdir}/plugins/jquery-ui.hpi
%{workdir}/plugins/jsch.hpi
%{workdir}/plugins/junit.hpi
%{workdir}/plugins/ldap.hpi
%{workdir}/plugins/lockable-resources.hpi
%{workdir}/plugins/mailer.hpi
%{workdir}/plugins/matrix-auth.hpi
%{workdir}/plugins/matrix-project.hpi
%{workdir}/plugins/momentjs.hpi
%{workdir}/plugins/pam-auth.hpi
%{workdir}/plugins/pipeline-build-step.hpi
%{workdir}/plugins/pipeline-graph-analysis.hpi
%{workdir}/plugins/pipeline-input-step.hpi
%{workdir}/plugins/pipeline-milestone-step.hpi
%{workdir}/plugins/pipeline-model-api.hpi
%{workdir}/plugins/pipeline-model-declarative-agent.hpi
%{workdir}/plugins/pipeline-model-definition.hpi
%{workdir}/plugins/pipeline-model-extensions.hpi
%{workdir}/plugins/pipeline-rest-api.hpi
%{workdir}/plugins/pipeline-stage-step.hpi
%{workdir}/plugins/pipeline-stage-tags-metadata.hpi
%{workdir}/plugins/pipeline-stage-view.hpi
%{workdir}/plugins/plain-credentials.hpi
%{workdir}/plugins/pubsub-light.hpi
%{workdir}/plugins/resource-disposer.hpi
%{workdir}/plugins/role-strategy.hpi
%{workdir}/plugins/scm-api.hpi
%{workdir}/plugins/script-security.hpi
%{workdir}/plugins/ssh.hpi
%{workdir}/plugins/ssh-agent.hpi
%{workdir}/plugins/ssh-credentials.hpi
%{workdir}/plugins/ssh-slaves.hpi
%{workdir}/plugins/structs.hpi
%{workdir}/plugins/timestamper.hpi
%{workdir}/plugins/token-macro.hpi
%{workdir}/plugins/workflow-aggregator.hpi
%{workdir}/plugins/workflow-api.hpi
%{workdir}/plugins/workflow-basic-steps.hpi
%{workdir}/plugins/workflow-cps-global-lib.hpi
%{workdir}/plugins/workflow-cps.hpi
%{workdir}/plugins/workflow-durable-task-step.hpi
%{workdir}/plugins/workflow-job.hpi
%{workdir}/plugins/workflow-multibranch.hpi
%{workdir}/plugins/workflow-scm-step.hpi
%{workdir}/plugins/workflow-step-api.hpi
%{workdir}/plugins/workflow-support.hpi
%{workdir}/plugins/ws-cleanup.hpi


%changelog
* Fri Feb 01 2019 Eric Lemings <eric@lemings.com> - 2.164.2.1552705448-1
- Update to 2.164.1.1552719454A
- Add/remove/update plugins per NG MS Boulder requirements.

