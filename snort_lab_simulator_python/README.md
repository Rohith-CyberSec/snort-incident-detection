# Snort Lab Simulator

A Python simulator that mimics Snort-like alerts for lab demonstrations.

## Files
- `snort_simulator.py` : Python script that prints simulated IDS alerts and can log JSON alerts to a file.

## Requirements
- Python 3.6+

## How to run
1. Clone or download this folder.
2. In a terminal, run:
   ```bash
   python snort_simulator.py
   ```
   Optional arguments:
   - `-n`, `--count` : number of events to simulate (default 10)
   - `-d`, `--delay` : seconds between events (default 1.0)
   - `-l`, `--logfile`: path to append JSON lines of alerts

## Example
```bash
python snort_simulator.py -n 20 -d 0.5 -l alerts.jsonl
```
