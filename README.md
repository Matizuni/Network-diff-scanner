# 🛡️ Network Diff Scanner

Herramienta de ciberseguridad desarrollada en Python para detectar cambios en la superficie de ataque de un host mediante la comparación de escaneos de red a lo largo del tiempo.

Inspirada en fundamentos de Red Team y metodologías descritas en *The Hacker Playbook 3*.

---

## 🎯 Objetivo

Este proyecto forma parte de un laboratorio personal de ciberseguridad enfocado en:

- Automatización de escaneos de red
- Monitoreo de superficie de ataque
- Detección de cambios en servicios expuestos
- Aplicación de técnicas Red Team / Blue Team

---

## 🚀 Características

- Escaneo de red usando Nmap
- Almacenamiento de resultados en JSON
- Comparación entre escaneos (baseline vs actual)
- Detección de:
  - Puertos nuevos
  - Puertos cerrados
- Generación de alertas básicas

---

## ⚙️ Tecnologías

- Python 3
- Nmap
- JSON

---

## ▶️ Uso rápido

```bash
pip install -r requirements.txt
python main.py
