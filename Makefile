PKG_NAME := mvn-kubernetes-client
URL = https://github.com/fabric8io/kubernetes-client/archive/v3.0.0.tar.gz
ARCHIVES = https://repo1.maven.org/maven2/io/fabric8/kubernetes-client/3.0.0/kubernetes-client-3.0.0.jar : https://repo1.maven.org/maven2/io/fabric8/kubernetes-client/3.0.0/kubernetes-client-3.0.0.pom : https://repo1.maven.org/maven2/io/fabric8/kubernetes-client-project/3.0.0/kubernetes-client-project-3.0.0.pom : https://repo.maven.apache.org/maven2/io/fabric8/kubernetes-model-generator/2.0.0/kubernetes-model-generator-2.0.0.pom : https://repo.maven.apache.org/maven2/io/fabric8/kubernetes-model/2.0.0/kubernetes-model-2.0.0.pom : https://repo.maven.apache.org/maven2/io/fabric8/kubernetes-model/2.0.0/kubernetes-model-2.0.0.jar :

include ../common/Makefile.common
