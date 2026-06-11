# PORT-SCANNER# TCP SYN Port Scanner - Core de Red 🛡️🐍

Este proyecto es una herramienta de consola interactiva (CLI) desarrollada en **Python** utilizando la librería avanzada de manipulación de redes **Scapy**. Funciona como el motor base para auditorías de infraestructura, simulando el comportamiento de un escaneo sigiloso del tipo **TCP SYN Scan (`-sS`)** interactuando directamente con las Capas 3 y 4 del Modelo OSI [19.0, 22.0].

## ⚙️ ¿Cómo funciona la lógica de inyección de red?

El script automatiza un bucle secuencial sobre un rango de puertos ingresado por el usuario, analizando el comportamiento de las respuestas lógicas del objetivo:

```text
[ Tu Script Python ]  ────── Ether() / IP() / TCP(Flags="S") ──────>  [ Objetivo (Router) ]
         │                                                                     │
         │  <─── Caso A: Responde TCP(Flags="SA") ──> [ PUERTO ABIERTO ] ──────┤
         │  <─── Caso B: Responde TCP(Flags="RA") ──> [ Puerto Cerrado ] ──────┤
         ▼  <─── Caso C: No responde (None) ───────> [ Filtra/Firewall ] ──────┘
```

1. **Forja de Paquetes a Medida:** El script fabrica un paquete crudo apilando las capas del Modelo OSI (`Ether() / IP() / TCP()`). Forzar la Capa 2 con `Ether()` permite puentear las restricciones nativas de Windows para enviar paquetes modificados a mano [19.0].
2. **Bandera SYN (`flags="S"`):** Envía el saludo inicial simulando que se quiere iniciar una conexión [22.0]. Si el puerto del router está abierto, este responderá con una bandera `SA` (SYN-ACK) [22.0].
3. **Manejador de Objetos Vacíos (NoneType):** Implementa un bloque `if/else` inteligente para interceptar paquetes que son "dropeados" por el Firewall del objetivo, evitando falsos positivos o que el script colapse lógicamente.

## 🛠️ Atributos y Controles de la CLI

* **IP Objetivo Dinámica:** Permite ingresar cualquier dirección de red (Local o Externa) por consola para auditorías independientes [22.0].
* **Rango Personalizable:** El usuario define el puerto de inicio y fin, sumando automáticamente `+1` en el backend para incluir de forma estricta la última puerta analizada.
* **Control de Velocidad y Latencia (`timeout`):** Permite configurar los segundos de espera por puerto para realizar escaneos ultrarrápidos en redes locales estables o escaneos lentos de precisión en servidores remotos.

## 🚀 Requisitos Obligatorios de Ejecución (Windows)

Debido a las políticas de seguridad nativas de Windows sobre *Raw Sockets*, se requiere:
1. Tener instalado el driver de red de ciberseguridad [Npcap](https://npcap.com).
2. Ejecutar la consola o entorno de desarrollo (VS Code) con **clic derecho -> Ejecutar como Administrador**.

---
*Desarrollado de forma autodidacta como laboratorio práctico de automatización en redes informáticas, inyección lógica y ciberseguridad defensiva.*
