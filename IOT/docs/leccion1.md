# 🚀 Mi Entrenamiento Elite en IoT 2026
> "La imprecisión es el enemigo del rendimiento."

## 🧠 Conceptos de Oro (Módulo 1)

### 1. Niveles de Calidad de Servicio (QoS) - MQTT
Para que un sistema sea robusto, debo elegir el nivel de entrega adecuado:
- **QoS 0:** "Enviar y olvidar". Máxima velocidad, mínima fiabilidad.
- **QoS 1:** "Entrega asegurada". El mensaje llega sí o sí, pero puede duplicarse.
- **QoS 2:** "Precisión quirúrgica". El mensaje llega una sola vez. Es el que usaré para **sistemas de seguridad y frenado industrial**.

### 2. Eficiencia de Datos (Payloads)
- **Regla de oro:** Nunca enviar JSON si puedes enviar Binario.
- **Impacto:** Reducir el payload un 80% salva la batería y reduce costes satelitales.
- **Técnica:** Uso de `struct` empaquetados (`__attribute__((packed))`) para evitar el desperdicio de memoria (padding).

### 3. El Trilema del Hardware
No existe el protocolo perfecto. Siempre debo elegir entre:
1. **Alcance** (Distancia).
2. **Consumo** (Batería).
3. **Ancho de Banda** (Velocidad de datos).
*Ejemplo: LoRaWAN es Rey en alcance/consumo, pero falla en ancho de banda.*

### 🔧 Ingeniería de Datos: Tipado y Empaquetamiento
Para maximizar la eficiencia en la transmisión de datos (Payload Optimization):

1. **Uso de C++ Estándar (`stdint.h`):** Evitar `int` genéricos. Usar `uint8_t` para ahorrar 3 bytes por variable en datos pequeños (0-250).

2. **Estructuras Empaquetadas:** La directiva `__attribute__((packed))` elimina el *padding* de memoria, reduciendo el tamaño del paquete a enviar por la red.

3. **Serialización Binaria:** Enviar el `struct` directamente como un chorro de bytes (*byte stream*) en lugar de convertirlo a texto (JSON). 

**Comparativa de eficiencia:**
| Formato | Tamaño (Aprox) | Consumo Radio | Coste Nube |
| :--- | :--- | :--- | :--- |
| JSON | ~50 bytes | Alto | Alto |
| Binario (Packed) | 6 bytes | Muy Bajo | Mínimo |

## 🏗️ Arquitectura de Comunicación (El Modelo de Capas)

Para entender cómo viaja la información desde mi sensor hasta la nube, utilizo la **Analogía de la Caja y el Camión**:

### 1. Capa de Transporte (El Camión 🚛)
Es el medio que mueve los datos. No le importa qué hay dentro, solo que llegue a su destino.
- **TCP (Transmission Control Protocol):** Conexión segura y verificada. Si un paquete se pierde, el camión vuelve a por él. (Usado en MQTT).
- **UDP (User Datagram Protocol):** Rápido y ligero. Envía el paquete y no mira atrás. Ideal para redes inestables o satelitales. (Usado en CoAP).

### 2. Capa de Aplicación (El Contenido de la Caja 📦)
Es el protocolo que define cómo se organizan los datos para que el servidor los entienda.
- **MQTT:** Estándar de la industria. Basado en Publicación/Suscripción.
- **HTTP:** Pesado, pero compatible con todo el ecosistema web.
- **CoAP:** El "HTTP" para dispositivos con recursos muy limitados.

### 3. Capa de Seguridad (El Blindaje 🔐)
> **Directiva 2026:** El uso de **TLS 1.3** (Transport Layer Security) es obligatorio. 
- Proporciona cifrado punto a punto, integridad de datos y autenticación. 
- Sin TLS, cualquier nodo intermedio puede leer mi "Telemetria" y hackear el actuador.

### 4. Diagnóstico: Heartbeat vs Last Will
Para saber si mi sistema está funcionando, implemento:
- **Heartbeat:** Un mensaje pequeño enviado cada X tiempo para decir "sigo vivo".
- **Last Will (LWT):** Una función de MQTT donde el servidor avisa automáticamente si el dispositivo se desconecta bruscamente.