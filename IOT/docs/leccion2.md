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