FROM centos:7

COPY ./elasticsearch.repo /etc/yum.repos.d/

RUN yum update && \
    yum -y install --enablerepo=elasticsearch elasticsearch
COPY ./conf/elasticsearch.yml /etc/elasticsearch/
RUN chown elasticsearch:elasticsearch /etc/elasticsearch/elasticsearch.yml && \
mkdir /usr/share/elasticsearch/snapshots

WORKDIR /usr/share/elasticsearch

USER elasticsearch

ENTRYPOINT ["./bin/elasticsearch"]

EXPOSE 9200 9300