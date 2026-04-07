pip install -r requirements.txt

## Running the tool
python main.py
Targets configuration

Edit the file:

targets.txt

Add one IP per line:

192.168.1.1
192.168.1.10
Output
Scan results are stored in the /scans directory
Each target has its own JSON file
The tool compares current and previous scans
Detection capabilities

The tool detects:

Newly opened ports
Closed ports
No changes in attack surface
Recommended environment
Kali Linux (attacker)
VirtualBox lab
Controlled environments only
Notes

This tool is intended for educational purposes and controlled security testing only.


---

## 💬 COMMIT

### Message:
```bash
docs: add usage documentation
Description:
Added detailed usage guide including installation, execution and configuration instructions.
