# 🛡️ Network Diff Scanner** is a Python-based tool for detecting changes in network attack surfaces by comparing scan results over time.

A cybersecurity tool written in Python to **detect changes in a host's attack surface** by comparing network scans over time.

Inspired by **Red Team fundamentals** and concepts from *The Hacker Playbook 3*.

---

## 🎯 Project Goal

This project was developed as part of a personal cybersecurity learning lab with the goal of:

- Automating network scans
- Keeping historical records of open ports per target
- Detecting **newly opened** and **closed ports**
- Simulating continuous attack surface monitoring
- Serving as a foundation for more advanced tools (alerts, C2, Blue Team, etc.)

---

## 🧠 How It Works

1. The script runs from an attacker machine (Kali Linux)
2. Uses `nmap` to scan specific ports on the target
3. Saves results in JSON files per IP
4. Compares the current scan with the previous one
5. Reports:
   - Newly detected ports
   - Closed ports
   - Or no changes detected

Each execution represents a **snapshot of the target's network state**.

---

## 🖥️ Lab Environment

- 🐧 **Attacker:** Kali Linux
- 🪟 **Target:** Windows VM
- 🌐 **Network:** VirtualBox Host-Only / NAT
- ⚙️ **Scanner Engine:** nmap
- 🐍 **Language:** Python 3

> ⚠️ This project was developed and tested **only in controlled lab environments**.

---

## 📂 Project Structure

# 🛡️ Network Diff Scanner

A cybersecurity tool written in Python to **detect changes in a host's attack surface** by comparing network scans over time.

Inspired by **Red Team fundamentals** and concepts from *The Hacker Playbook 3*.

---

## 🎯 Project Goal

This project was developed as part of a personal cybersecurity learning lab with the goal of:

- Automating network scans
- Keeping historical records of open ports per target
- Detecting **newly opened** and **closed ports**
- Simulating continuous attack surface monitoring
- Serving as a foundation for more advanced tools (alerts, C2, Blue Team, etc.)

### Features
- Nmap scan
- JSON history
- Port diff detection
- Alerts on changes

### Use case
Red Team & Blue Team fundamentals

---

## 🧠 How It Works

1. The script runs from an attacker machine (Kali Linux)
2. Uses `nmap` to scan specific ports on the target
3. Saves results in JSON files per IP
4. Compares the current scan with the previous one
5. Reports:
   - Newly detected ports
   - Closed ports
   - Or no changes detected

Each execution represents a **snapshot of the target's network state**.

---

## 🖥️ Lab Environment

- 🐧 **Attacker:** Kali Linux
- 🪟 **Target:** Windows VM
- 🌐 **Network:** VirtualBox Host-Only / NAT
- ⚙️ **Scanner Engine:** nmap
- 🐍 **Language:** Python 3

> ⚠️ This project was developed and tested **only in controlled lab environments**.

---

## 📂 Project Structure

network-diff-scanner/
├── scanner.py
├── targets.txt
├── scans/
│ └── <target_ip>.json
|── README_IN.md
|── README_ES.md

## 📚 Theoretical Background

### Network Reconnaissance
Network reconnaissance is the process of identifying active hosts, open ports, and exposed services within a network. It is a foundational phase in both offensive (Red Team) and defensive (Blue Team) security operations.

### Attack Surface Monitoring
An attack surface represents all the points where an attacker could interact with a system. Monitoring changes in the attack surface over time allows early detection of misconfigurations or newly exposed services.

### Diff-Based Detection
Diff-based detection involves comparing current system states against historical baselines to identify deviations. This technique is widely used in intrusion detection systems and continuous security monitoring.

This project applies diff-based detection to network port exposure using periodic scans.
