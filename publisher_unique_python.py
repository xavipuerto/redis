import redis
import time
import random

# Conectar a Redis con autenticación
r = redis.Redis(host="localhost", port=6379, password="password123", decode_responses=True)

# Publicar mensajes en un canal cada segundo
try:
    mensaje = f"Temperatura: {round(random.uniform(30.0, 40.0), 2)}°C"
    try:
        r.publish("canal_sensorica", mensaje)
        print(f"📤 Mensaje publicado: {mensaje}")
    except Exception as e:
        print(f"❌ Error al publicar: {e}")
    time.sleep(1)
except KeyboardInterrupt:
    print("🚀 Publicador detenido.")
