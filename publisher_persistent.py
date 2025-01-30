import redis
import time
import random

# Conectar a Redis con autenticación
r = redis.Redis(host="localhost", port=6379, password="password123", decode_responses=True)

# Nombre del stream
STREAM_NAME = "sensorica_stream_persistent"

# Intentar crear el stream si no existe
try:
    r.xgroup_create(STREAM_NAME, "mi_grupo", id="$", mkstream=True)
    print(f"✅ Grupo de consumidores 'mi_grupo' creado en {STREAM_NAME}")
except redis.exceptions.ResponseError:
    print(f"ℹ️ El grupo 'mi_grupo' ya existe en {STREAM_NAME}")

print(f"🚀 Publicador enviando datos a {STREAM_NAME}...")

# Publicar mensajes en el Stream
try:
    while True:
        mensaje = {
            "temperatura": round(random.uniform(20.0, 30.0), 2),
            "humedad": round(random.uniform(30.0, 60.0), 2)
        }
        try:
            # Publicar mensaje en el Stream
            r.xadd(STREAM_NAME, mensaje)
            print(f"📤 Mensaje publicado en stream: {mensaje}")
        except Exception as e:
            print(f"❌ Error al publicar en Redis: {e}")
        time.sleep(1)  # Esperar 5 segundos antes del próximo envío
except KeyboardInterrupt:
    print("🚀 Publicador detenido.")
