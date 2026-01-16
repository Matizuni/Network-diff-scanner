#!/usr/bin/env python3

import subprocess
import json
from pathlib import Path
from datetime import datetime

SCANS_DIR = Path("scans")
SCANS_DIR.mkdir(exist_ok=True)

PORTS = "22,80,443,445,3389,8080"


def load_targets():
    with open("targets.txt") as f:
        return [line.strip() for line in f if line.strip()]


def run_nmap(target_ip):
    print("[*] Ejecutando nmap...")
    cmd = [
        "nmap",
        "-Pn",
        "-p", PORTS,
        target_ip
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout


def parse_nmap(output):
    ports = {}

    for line in output.splitlines():
        if "/tcp" in line and ("open" in line or "filtered" in line):
            parts = line.split()
            port = parts[0].split("/")[0]
            state = parts[1]
            ports[port] = state

    return ports


def load_previous_scan(scan_file):
    if not scan_file.exists():
        return None
    with open(scan_file) as f:
        return json.load(f)


def save_scan(scan_file, target_ip, ports):
    data = {
        "target": target_ip,
        "timestamp": datetime.now().isoformat(),
        "ports": ports
    }
    with open(scan_file, "w") as f:
        json.dump(data, f, indent=4)


def compare_scans(old_ports, new_ports):
    opened = []
    closed = []

    for port in new_ports:
        if port not in old_ports:
            opened.append(port)

    for port in old_ports:
        if port not in new_ports:
            closed.append(port)

    return opened, closed


def run_scan_for_target(target_ip):
    print(f"\n🎯 Escaneando objetivo: {target_ip}")

    scan_file = SCANS_DIR / f"{target_ip}.json"

    previous_scan = load_previous_scan(scan_file)

    output = run_nmap(target_ip)
    current_ports = parse_nmap(output)

    if previous_scan is None:
        print("[*] Primer escaneo del objetivo")
    else:
        old_ports = previous_scan.get("ports", {})
        opened, closed = compare_scans(old_ports, current_ports)

        if opened:
            print("[+] Puertos NUEVOS detectados:")
            for port in opened:
                print(f"    + {port}/tcp ({current_ports[port]})")

        if closed:
            print("[-] Puertos CERRADOS detectados:")
            for port in closed:
                print(f"    - {port}/tcp")

        if not opened and not closed:
            print("[=] No se detectaron cambios")

    save_scan(scan_file, target_ip, current_ports)
    print("[*] Escaneo guardado correctamente")


def main():
    targets = load_targets()
    for target_ip in targets:
        run_scan_for_target(target_ip)


if __name__ == "__main__":
    main()
