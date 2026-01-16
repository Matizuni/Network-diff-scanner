# 🛡️ Network Diff Scanner** Es una herramienta basada en Python para detectar cambios en las superficies de ataque de la red comparando los resultados de los escaneos a lo largo del tiempo.

Herramienta de ciberseguridad desarrollada en Python para **detectar cambios en la superficie de ataque de un host**, comparando escaneos de red a lo largo del tiempo.

Inspirada en **fundamentos de Red Team** y en conceptos de *The Hacker Playbook 3*.

---

## 🎯 Objetivo del Proyecto

Este proyecto fue creado como parte de un laboratorio personal de aprendizaje en ciberseguridad con el objetivo de:

- Automatizar escaneos de red
- Mantener un historial de puertos por objetivo
- Detectar **puertos nuevos** y **puertos cerrados**
- Simular monitoreo continuo de superficie de ataque
- Servir como base para herramientas más avanzadas (alertas, C2, Blue Team, etc.)

---

## 🧠 ¿Cómo Funciona?

1. El script se ejecuta desde una máquina atacante (Kali Linux)
2. Utiliza `nmap` para escanear puertos específicos del objetivo
3. Guarda los resultados en archivos JSON por IP
4. Compara el escaneo actual con el anterior
5. Reporta:
   - Puertos nuevos detectados
   - Puertos cerrados
   - O ausencia de cambios

Cada ejecución representa un **snapshot del estado de red del objetivo**.

---

## 🖥️ Entorno de Laboratorio

- 🐧 **Atacante:** Kali Linux
- 🪟 **Objetivo:** Windows (VM)
- 🌐 **Red:** VirtualBox Host-Only / NAT
- ⚙️ **Motor de escaneo:** nmap
- 🐍 **Lenguaje:** Python 3

> ⚠️ Proyecto desarrollado y probado **exclusivamente en entornos controlados (lab)**.

---

## 📂 Estructura del Proyecto

network-diff-scanner/
├── scanner.py
├── targets.txt
├── scans/
│ └── <ip_objetivo>.json
└── README_ES.md
|── README_IN.md

## 📚 Marco Teórico

### Reconocimiento de Red
El reconocimiento de red es el proceso de identificar hosts activos, puertos abiertos y servicios expuestos dentro de una red. Es una fase fundamental tanto en operaciones ofensivas (Red Team) como defensivas (Blue Team).

### Superficie de Ataque
La superficie de ataque representa todos los puntos por los cuales un sistema puede ser atacado. Monitorear cambios en la superficie de ataque permite detectar configuraciones inseguras o servicios expuestos de forma temprana.

### Detección Basada en Diferencias (Diff)
La detección basada en diferencias consiste en comparar estados actuales con una línea base histórica para identificar desviaciones. Esta técnica es ampliamente utilizada en sistemas de detección y monitoreo continuo.

Este proyecto aplica detección por diferencias al monitoreo de puertos de red.
