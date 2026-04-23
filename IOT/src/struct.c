// Definición de la estructura optimizada para IoT
struct __attribute__((packed)) Telemetria {
    float temperatura;    // 4 bytes
    uint8_t humedad;      // 1 byte (0-100% no necesita un int de 4 bytes)
    bool valvulaAbierta;  // 1 byte
}; 