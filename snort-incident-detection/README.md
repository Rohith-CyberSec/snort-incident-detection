# Snort Incident Detection Lab

## Project Overview
This repo demonstrates basic incident detection using Snort IDS. Custom rules detect ICMP floods, suspicious HTTP traffic, and Telnet connections.

## Setup Instructions
1. Install Snort on your lab environment.
2. Copy `snort_rules.conf` to your Snort rules directory.
3. Start Snort in IDS mode:
```
snort -c /path/to/snort_rules.conf -i <network_interface>
```
4. Generate traffic to trigger the alerts (lab environment only).

## Sample Alerts
- ICMP flood alert when pinging rapidly.
- HTTP alert when accessing the suspicious IP 192.168.1.100.
- Telnet connection alert on port 23.

## Skills Demonstrated
- Threat detection
- Incident response
- Network security monitoring

## Lessons Learned
- Writing effective Snort rules.
- Threshold tuning to reduce false positives.
- Understanding IDS alerts and response planning.