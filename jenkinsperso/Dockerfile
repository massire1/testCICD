FROM jenkins/jenkins:lts-jdk17

USER root

# Installer curl, unzip, et docker CLI
RUN apt-get update && \
    apt-get install -y curl unzip

# Télécharger le binaire Docker officiel (version stable)
RUN curl -fsSL https://download.docker.com/linux/static/stable/x86_64/docker-24.0.5.tgz | tar -xzvf - --strip-components=1 -C /usr/local/bin docker/docker

# Vérifier l'installation de Docker
RUN docker --version

USER jenkins