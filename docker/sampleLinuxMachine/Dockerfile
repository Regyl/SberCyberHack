# File: Dockerfile
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# Install essential tools
RUN apt-get update && apt-get install -y \
    python3 python3-pip net-tools netcat curl \
    openssh-server sudo procps iputils-ping vim \
    rsyslog file\
    && apt-get clean

# Create test user
RUN useradd -ms /bin/bash tester && echo 'tester:password' | chpasswd && adduser tester sudo

# Setup SSH (optional for real log entries)
RUN mkdir /var/run/sshd

# Setup dummy auth.log
RUN touch /var/log/auth.log && chown syslog:adm /var/log/auth.log

# Copy scripts
WORKDIR /home/tester
COPY . /home/tester/app
RUN chown -R tester:tester /home/tester/app

USER tester
WORKDIR /home/tester/shared
ENV PATH="/home/tester/.local/bin:${PATH}"

CMD ["tail", "-f", "/dev/null"]
