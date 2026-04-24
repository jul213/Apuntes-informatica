# 🔌 Módulo 2: Ingeniería de Hardware y Gestión Energética

Un experto en IoT no solo programa; diseña sistemas físicos resilientes. Este módulo cubre la intersección entre el electrón y el dato.

## 1. El Abismo de los Voltajes (3.3V vs 5V)
La mayoría de los microcontroladores modernos (ESP32, STM32, RP2040) operan a **3.3V**. 
- **El Peligro:** Muchos sensores antiguos o industriales operan a **5V**. 
- **La Solución:** - **Divisor de Tensión:** Dos resistencias en serie para bajar el voltaje.
    - **Logic Level Shifter:** Un pequeño chip (MOSFET) que traduce niveles lógicos de forma bidireccional sin riesgo.

## 2. Conversión Analógica-Digital (ADC)
El mundo es analógico (infinitas variaciones), pero el procesador es digital (ceros y unos).
- **Resolución:** El ADC del ESP32 es de **12 bits**. Esto significa que divide el rango de 0V a 3.3V en 4096 pasos ($2^{12}$).
- **Precisión:** Si el ADC lee un valor de `2048`, sabemos que hay exactamente **1.65V** en el pin.

## 3. Protocolos de Comunicación Interna (Buses)
| Protocolo | Cables | Velocidad | Distancia | Uso Principal |
| :--- | :--- | :--- | :--- | :--- |
| **I2C** | 2 (SDA/SCL) | Media | < 2 metros | Múltiples sensores, pantallas OLED. |
| **SPI** | 4 (MOSI/MISO/SCK/SS) | Muy Alta | < 1 metro | Tarjetas SD, pantallas TFT a color. |
| **UART** | 2 (TX/RX) | Variable | < 15 metros | GPS, módems celulares, comunicación con PC. |

## 4. Gestión de Energía Crítica (Deep Sleep)
Para que un dispositivo IoT dure años con una batería, el código debe ser "pasivo".
- **Ciclo de Vida:** Despertar -> Leer Sensores -> Conectar Red -> Enviar Dato -> Dormir.
- **Corriente Quiescente:** Es el consumo del dispositivo mientras duerme. Un buen diseño baja de los **20µA**.

## 5. Protecciones Esenciales
- **Resistencia Pull-up/Pull-down:** Garantiza que un pin digital no esté "flotando" (recogiendo ruido electromagnético) cuando no hay nada conectado.
- **Capacitores de Desacoplo:** "Tanques" de energía minúsculos colocados cerca del chip para evitar reinicios por caídas bruscas de voltaje.

## 📡 6. Protocolos de Comunicación Local (Buses de Datos)

En el diseño de hardware IoT, la elección del bus determina la velocidad del sistema y la complejidad del cableado.

### 🔵 I2C (Inter-Integrated Circuit) - "El Bus Eficiente"
Protocolo síncrono de **dos hilos** diseñado para conectar múltiples periféricos de baja/media velocidad.

- **Líneas de conexión:**
    - **SDA (Serial Data):** Transmisión bidireccional de datos.
    - **SCL (Serial Clock):** Sincronización generada por el Maestro.
- **Arquitectura:** Maestro-Esclavo. El maestro gestiona el tráfico mediante **Direccionamiento** (cada sensor tiene una ID única, ej: `0x3C`).
- **Ventaja:** Ahorro masivo de pines. Puedes conectar hasta 128 dispositivos usando solo 2 cables.
- **Uso ideal:** Sensores de temperatura, presión, pantallas OLED.

### 🔴 SPI (Serial Peripheral Interface) - "El Bus de Alta Velocidad"
Protocolo síncrono de **cuatro hilos** (mínimo) para transferencia de datos masivos sin retardo.

- **Líneas de conexión:**
    - **MOSI (Master Out Slave In):** Salida de datos del maestro.
    - **MISO (Master In Slave Out):** Entrada de datos al maestro.
    - **SCK (Serial Clock):** Reloj de sincronización.
    - **CS/SS (Chip Select):** Un cable extra por cada esclavo para "activarlo".
- **Características:**
    - **Full-Dúplex:** Envía y recibe datos al mismo tiempo.
    - **Velocidad:** Muy alta (80 MHz+). Supera con creces al I2C.
- **Uso ideal:** Lectores de tarjetas SD, pantallas TFT a color, módulos Ethernet o Cámaras.

---

### ⚖️ Comparativa Rápida para Toma de Decisiones

| Característica | I2C | SPI |
| :--- | :--- | :--- |
| **Hilos necesarios** | 2 | 4 + N (esclavos) |
| **Velocidad** | Media (hasta 3.4 MHz) | Muy Alta (100 MHz+) |
| **Multiesclavo** | Sí (por dirección software) | Sí (por cable hardware CS) |
| **Distancia** | Muy corta (< 2m) | Muy corta (< 1m) |
| **Simplicidad** | Alta (fácil de cablear) | Baja (muchos cables) |

### 🟢 UART (Universal Asynchronous Receiver-Transmitter) - "El Protocolo Universal"
No es un bus como tal, sino una comunicación **punto a punto** (de uno a uno) sin necesidad de reloj compartido.

- **Líneas de conexión:** - **TX (Transmit):** Envío de datos.
    - **RX (Receive):** Recepción de datos.
    - *Importante:* El TX de uno va al RX del otro.
- **Características:** - **Asíncrono:** No hay cable de reloj; ambos dispositivos deben acordar la misma velocidad (**Baud Rate**).
    - **Simplicidad máxima:** Solo 2 cables para comunicación total.
- **Uso ideal:** Depuración (Monitor Serie), Módems GPS, módulos Bluetooth (HC-05/06) y comunicación entre dos microcontroladores.

### 🟡 1-Wire (Dallas Semiconductor) - "El Bus de Larga Distancia"
Diseñado para situaciones donde quieres ahorrar cables al máximo y tienes sensores esparcidos por una casa o industria.

- **Líneas de conexión:** **¡Solo 1 cable!** (Más tierra). Los datos y la alimentación pueden ir por el mismo hilo (*Parasite Power*).
- **Ventaja:** Puede cubrir distancias de hasta **100 metros**, algo que I2C o SPI jamás podrían hacer sin quemarse.
- **Uso ideal:** El famoso sensor de temperatura **DS18B20**.

### 🏗️ CAN Bus (Controller Area Network) - "El Estándar Industrial/Automotriz"
Si el sistema debe ser inmune al ruido eléctrico extremo (motores, fábricas).

- **Características:** Diferencial (usa dos cables que se comparan entre sí para evitar interferencias). Es extremadamente robusto.
- **Uso ideal:** Sensores en motores de coches, maquinaria pesada y robótica avanzada.
