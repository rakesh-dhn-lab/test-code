FROM centos:7
# Install  java , wget
# gcc and make to build python and epel enable to install mongodb
RUN yum install gcc make zlib-devel epel-release java wget -y

#Install Mongodb
RUN yum -y install mongodb-server
RUN mkdir -p /data/db
RUN mkdir -p /data/logs

# Install python
RUN cd /usr/src
RUN wget  https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tgz > /dev/null && \
tar xzf Python-3.6.5.tgz && \
cd Python-3.6.5 && \
./configure --enable-optimizations > /dev/null && \
make altinstall > /dev/null

# Install tomcat8
RUN mkdir /opt/tomcat
RUN wget http://mirrors.estointernet.in/apache/tomcat/tomcat-8/v8.5.46/bin/apache-tomcat-8.5.46.tar.gz -O /tmp/tomcat.tar.gz > /dev/null
RUN cd /tmp && tar xfz tomcat.tar.gz
RUN cp -Rv /tmp/apache-tomcat-8.5.46/* /opt/tomcat

# Expose the Tomcat port to host
EXPOSE 8080

# Setup starting script
RUN echo 'mongod --fork --dbpath=/data/db --logpath=/data/logs/mongo.log &' >> /start.sh
RUN echo '/bin/bash /opt/tomcat/bin/startup.sh &' >> /start.sh
RUN chmod a+x /start.sh

CMD ["/start.sh"]

ENTRYPOINT ["/bin/bash"]

