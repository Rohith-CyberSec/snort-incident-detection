#!/usr/bin/env python3
"""snort_simulator.py
Simple Snort-like alert simulator that can print alerts and optionally log them to a file.
"""
import time
import random
import argparse
import json
from datetime import datetime

EVENTS = [
    {"type": "ICMP", "src": "192.168.1.10", "dst": "192.168.1.100", "details": "High-rate ICMP requests"},
    {"type": "HTTP", "src": "10.0.0.5", "dst": "192.168.1.100", "details": "Suspicious User-Agent and payload"},
    {"type": "Telnet", "src": "172.16.0.7", "dst": "192.168.1.50", "details": "Telnet service connection attempt"}
]

def format_alert(event):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {
        "timestamp": ts,
        "alert": event["type"],
        "src": event["src"],
        "dst": event["dst"],
        "details": event["details"]
    }

def print_alert(alert):
    print(f"{alert['timestamp']} [ALERT] {alert['alert']} from {alert['src']} -> {alert['dst']} | {alert['details']}")

def append_log(path, alert):
    with open(path, 'a', encoding='utf-8') as f:
        f.write(json.dumps(alert) + '\n')

def run_simulation(count, delay, logfile=None):
    print("Starting Snort-like alert simulator...\n")
    for i in range(count):
        event = random.choice(EVENTS)
        alert = format_alert(event)
        print_alert(alert)
        if logfile:
            append_log(logfile, alert)
        time.sleep(delay)

def main():
    parser = argparse.ArgumentParser(description='Snort Lab Simulator')
    parser.add_argument('-n', '--count', type=int, default=10, help='Number of events to simulate')
    parser.add_argument('-d', '--delay', type=float, default=1.0, help='Delay (seconds) between events')
    parser.add_argument('-l', '--logfile', type=str, default=None, help='Optional path to append JSON alerts')
    args = parser.parse_args()
    run_simulation(args.count, args.delay, args.logfile)

if __name__ == '__main__':
    main()
