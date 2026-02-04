#!/bin/bash

echo "Checking system health"

uptime
df -h
free -m
top -b -n1 | head -15
