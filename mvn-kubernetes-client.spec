#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-kubernetes-client
Version  : 3.0.0
Release  : 1
URL      : https://github.com/fabric8io/kubernetes-client/archive/v3.0.0.tar.gz
Source0  : https://github.com/fabric8io/kubernetes-client/archive/v3.0.0.tar.gz
Source1  : https://repo1.maven.org/maven2/io/fabric8/kubernetes-client/3.0.0/kubernetes-client-3.0.0.jar
Source2  : https://repo1.maven.org/maven2/io/fabric8/kubernetes-client/3.0.0/kubernetes-client-3.0.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-kubernetes-client-data = %{version}-%{release}

%description
# Kubernetes & OpenShift 3 Java Client [![Join the chat at https://gitter.im/fabric8io/kubernetes-client](https://badges.gitter.im/fabric8io/kubernetes-client.svg)](https://gitter.im/fabric8io/kubernetes-client?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
This client provides access to the full [Kubernetes](http://kubernetes.io/) &
[OpenShift 3](http://openshift.org/) REST APIs via a fluent DSL.

%package data
Summary: data components for the mvn-kubernetes-client package.
Group: Data

%description data
data components for the mvn-kubernetes-client package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/io/fabric8/kubernetes-client/3.0.0
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/io/fabric8/kubernetes-client/3.0.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/io/fabric8/kubernetes-client/3.0.0
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/io/fabric8/kubernetes-client/3.0.0


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/io/fabric8/kubernetes-client/3.0.0/kubernetes-client-3.0.0.jar
/usr/share/java/.m2/repository/io/fabric8/kubernetes-client/3.0.0/kubernetes-client-3.0.0.pom
