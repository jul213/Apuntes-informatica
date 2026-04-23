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

