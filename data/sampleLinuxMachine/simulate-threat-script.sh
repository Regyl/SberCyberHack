#!/bin/bash
# File: simulate_threats.sh

# Simulate failed SSH attempts
for i in {1..5}; do
  echo "Jul 29 10:45:0$i ubuntu sshd[1234$i]: Failed password for invalid user hacker$i from 192.168.1.$i port 22 ssh2" >> /var/log/auth.log
done

# Start a dummy process
while true; do sleep 100; done &
