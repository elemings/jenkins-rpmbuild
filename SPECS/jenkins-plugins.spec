
%define workdir %{_var}/lib/jenkins

Name:       jenkins-plugins
Version:    2.235.5
Release:    1%{?dist}
Summary:    Jenkins plugin bundle

Group:      Development/Tools/Building
License:    ASL 2.0
URL:        https://plugins.jenkins.io/

Source1:    https://updates.jenkins-ci.org/download/plugins/ace-editor/1.1/ace-editor.hpi
Source2:    https://updates.jenkins-ci.org/download/plugins/ant/1.11/ant.hpi
Source3:    https://updates.jenkins-ci.org/download/plugins/antisamy-markup-formatter/2.1/antisamy-markup-formatter.hpi
Source4:    https://updates.jenkins-ci.org/download/plugins/apache-httpcomponents-client-4-api/4.5.10-2.0/apache-httpcomponents-client-4-api.hpi
Source5:    https://updates.jenkins-ci.org/download/plugins/bouncycastle-api/2.18/bouncycastle-api.hpi
Source6:    https://updates.jenkins-ci.org/download/plugins/branch-api/2.5.9/branch-api.hpi
Source7:    https://updates.jenkins-ci.org/download/plugins/build-timeout/1.20/build-timeout.hpi
Source8:    https://updates.jenkins-ci.org/download/plugins/clearcase/1.6.3/clearcase.hpi
Source9:    https://updates.jenkins-ci.org/download/plugins/cloudbees-folder/6.14/cloudbees-folder.hpi
Source10:   https://updates.jenkins-ci.org/download/plugins/command-launcher/1.4/command-launcher.hpi
Source11:   https://updates.jenkins-ci.org/download/plugins/conditional-buildstep/1.3.6/conditional-buildstep.hpi
Source12:   https://updates.jenkins-ci.org/download/plugins/credentials-binding/1.23/credentials-binding.hpi
Source13:   https://updates.jenkins-ci.org/download/plugins/credentials/2.3.12/credentials.hpi
Source14:   https://updates.jenkins-ci.org/download/plugins/display-url-api/2.3.3/display-url-api.hpi
Source15:   https://updates.jenkins-ci.org/download/plugins/durable-task/1.34/durable-task.hpi
Source16:   https://updates.jenkins-ci.org/download/plugins/echarts-api/4.8.0-2/echarts-api.hpi
Source17:   https://updates.jenkins-ci.org/download/plugins/email-ext/2.75/email-ext.hpi
Source18:   https://updates.jenkins-ci.org/download/plugins/fortify/20.1.33/fortify.hpi
Source19:   https://updates.jenkins-ci.org/download/plugins/git-client/3.4.2/git-client.hpi
Source20:   https://updates.jenkins-ci.org/download/plugins/git-server/1.9/git-server.hpi
Source21:   https://updates.jenkins-ci.org/download/plugins/git/4.4.0/git.hpi
Source22:   https://updates.jenkins-ci.org/download/plugins/handlebars/1.1.1/handlebars.hpi
Source23:   https://updates.jenkins-ci.org/download/plugins/jackson2-api/2.11.2/jackson2-api.hpi
Source24:   https://updates.jenkins-ci.org/download/plugins/jdk-tool/1.4/jdk-tool.hpi
Source25:   https://updates.jenkins-ci.org/download/plugins/jira/3.1.1/jira.hpi
Source26:   https://updates.jenkins-ci.org/download/plugins/jobConfigHistory/2.26/jobConfigHistory.hpi
Source27:   https://updates.jenkins-ci.org/download/plugins/jquery3-api/3.5.1-1/jquery3-api.hpi
Source28:   https://updates.jenkins-ci.org/download/plugins/jquery-detached/1.2.1/jquery-detached.hpi
Source29:   https://updates.jenkins-ci.org/download/plugins/jsch/0.1.55.2/jsch.hpi
Source30:   https://updates.jenkins-ci.org/download/plugins/junit/1.32/junit.hpi
Source31:   https://updates.jenkins-ci.org/download/plugins/ldap/1.24/ldap.hpi
Source32:   https://updates.jenkins-ci.org/download/plugins/lockable-resources/2.8/lockable-resources.hpi
Source33:   https://updates.jenkins-ci.org/download/plugins/log-parser/2.1/log-parser.hpi
Source34:   https://updates.jenkins-ci.org/download/plugins/mailer/1.32/mailer.hpi
Source35:   https://updates.jenkins-ci.org/download/plugins/mapdb-api/1.0.9.0/mapdb-api.hpi
Source36:   https://updates.jenkins-ci.org/download/plugins/matrix-auth/2.6.2/matrix-auth.hpi
Source37:   https://updates.jenkins-ci.org/download/plugins/matrix-project/1.17/matrix-project.hpi
Source38:   https://updates.jenkins-ci.org/download/plugins/momentjs/1.1.1/momentjs.hpi
Source39:   https://updates.jenkins-ci.org/download/plugins/pam-auth/1.6/pam-auth.hpi
Source40:   https://updates.jenkins-ci.org/download/plugins/parameterized-trigger/2.37/parameterized-trigger.hpi
Source41:   https://updates.jenkins-ci.org/download/plugins/pipeline-build-step/2.13/pipeline-build-step.hpi
Source42:   https://updates.jenkins-ci.org/download/plugins/pipeline-graph-analysis/1.10/pipeline-graph-analysis.hpi
Source43:   https://updates.jenkins-ci.org/download/plugins/pipeline-input-step/2.11/pipeline-input-step.hpi
Source44:   https://updates.jenkins-ci.org/download/plugins/pipeline-milestone-step/1.3.1/pipeline-milestone-step.hpi
Source45:   https://updates.jenkins-ci.org/download/plugins/pipeline-model-api/1.7.1/pipeline-model-api.hpi
Source46:   https://updates.jenkins-ci.org/download/plugins/pipeline-model-declarative-agent/1.1.1/pipeline-model-declarative-agent.hpi
Source47:   https://updates.jenkins-ci.org/download/plugins/pipeline-model-definition/1.7.1/pipeline-model-definition.hpi
Source48:   https://updates.jenkins-ci.org/download/plugins/pipeline-model-extensions/1.7.1/pipeline-model-extensions.hpi
Source49:   https://updates.jenkins-ci.org/download/plugins/pipeline-rest-api/2.14/pipeline-rest-api.hpi
Source50:   https://updates.jenkins-ci.org/download/plugins/pipeline-stage-step/2.5/pipeline-stage-step.hpi
Source51:   https://updates.jenkins-ci.org/download/plugins/pipeline-stage-tags-metadata/1.7.1/pipeline-stage-tags-metadata.hpi
Source52:   https://updates.jenkins-ci.org/download/plugins/pipeline-stage-view/2.14/pipeline-stage-view.hpi
Source53:   https://updates.jenkins-ci.org/download/plugins/plain-credentials/1.7/plain-credentials.hpi
Source54:   https://updates.jenkins-ci.org/download/plugins/plugin-util-api/1.2.3/plugin-util-api.hpi
Source55:   https://updates.jenkins-ci.org/download/plugins/pubsub-light/1.13/pubsub-light.hpi
Source56:   https://updates.jenkins-ci.org/download/plugins/resource-disposer/0.14/resource-disposer.hpi
Source57:   https://updates.jenkins-ci.org/download/plugins/run-condition/1.3/run-condition.hpi
Source58:   https://updates.jenkins-ci.org/download/plugins/scm-api/2.6.3/scm-api.hpi
Source59:   https://updates.jenkins-ci.org/download/plugins/script-security/1.74/script-security.hpi
Source60:   https://updates.jenkins-ci.org/download/plugins/snakeyaml-api/1.26.4/snakeyaml-api.hpi
Source61:   https://updates.jenkins-ci.org/download/plugins/ssh/2.6.1/ssh.hpi
Source62:   https://updates.jenkins-ci.org/download/plugins/ssh-agent/1.20/ssh-agent.hpi
Source63:   https://updates.jenkins-ci.org/download/plugins/ssh-credentials/1.18.1/ssh-credentials.hpi
Source64:   https://updates.jenkins-ci.org/download/plugins/ssh-slaves/1.31.2/ssh-slaves.hpi
Source65:   https://updates.jenkins-ci.org/download/plugins/structs/1.20/structs.hpi
Source66:   https://updates.jenkins-ci.org/download/plugins/timestamper/1.11.5/timestamper.hpi
Source67:   https://updates.jenkins-ci.org/download/plugins/token-macro/2.12/token-macro.hpi
Source68:   https://updates.jenkins-ci.org/download/plugins/trilead-api/1.0.8/trilead-api.hpi
Source69:   https://updates.jenkins-ci.org/download/plugins/workflow-aggregator/2.6/workflow-aggregator.hpi
Source70:   https://updates.jenkins-ci.org/download/plugins/workflow-api/2.40/workflow-api.hpi
Source71:   https://updates.jenkins-ci.org/download/plugins/workflow-basic-steps/2.20/workflow-basic-steps.hpi
Source72:   https://updates.jenkins-ci.org/download/plugins/workflow-cps-global-lib/2.17/workflow-cps-global-lib.hpi
Source73:   https://updates.jenkins-ci.org/download/plugins/workflow-cps/2.82/workflow-cps.hpi
Source74:   https://updates.jenkins-ci.org/download/plugins/workflow-durable-task-step/2.35/workflow-durable-task-step.hpi
Source75:   https://updates.jenkins-ci.org/download/plugins/workflow-job/2.39/workflow-job.hpi
Source76:   https://updates.jenkins-ci.org/download/plugins/workflow-multibranch/2.22/workflow-multibranch.hpi
Source77:   https://updates.jenkins-ci.org/download/plugins/workflow-scm-step/2.11/workflow-scm-step.hpi
Source78:   https://updates.jenkins-ci.org/download/plugins/workflow-step-api/2.22/workflow-step-api.hpi
Source79:   https://updates.jenkins-ci.org/download/plugins/workflow-support/3.5/workflow-support.hpi
Source80:   https://updates.jenkins-ci.org/download/plugins/ws-cleanup/0.38/ws-cleanup.hpi

BuildArch:  noarch
Requires:   jenkins >= %{version}


%description
Plugins are the primary means of enhancing the functionality of a
Jenkins environment to suit organization- or user-specific needs. There
are over a thousand different plugins which can be installed on a
Jenkins master and to integrate various build tools, cloud providers,
analysis tools, and much more.

%prep


%build


%install
rm -rf %{buildroot}
%__install -d -m0755 %{buildroot}%{workdir}/plugins
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
%__install -D -m0644 %{SOURCE76} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE77} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE78} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE79} %{buildroot}%{workdir}/plugins/
%__install -D -m0644 %{SOURCE80} %{buildroot}%{workdir}/plugins/


%clean
%__rm -rf "%{buildroot}"


%files
%defattr(-,jenkins,jenkins)
%dir %{workdir}
%dir %{workdir}/plugins
%{workdir}/plugins/**.hpi


%changelog
* Tue Aug 25 2020 Eric Lemings <eric@lemings.com> - 2.235.5-1
- Update to 2.235.5

* Fri Feb 01 2019 Eric Lemings <eric@lemings.com> - 2.164.2.1552705448-1
- Update to 2.164.1.1552719454A

