import redis
import sys

# Conectar a Redis con autenticación
r = redis.Redis(host="localhost", port=6379, password="password123", decode_responses=True)

# Nombre del stream y del grupo de consumidores
STREAM_NAME = "sensorica_stream_persistent"
GROUP_NAME = "mi_grupo"

# Obtener el nombre del consumidor desde el argumento de línea de comandos
consumer_id = sys.argv[1] if len(sys.argv) > 1 else "consumidor_default"

# Asegurar que el grupo de consumidores existe antes de leer
try:
    r.xgroup_create(STREAM_NAME, GROUP_NAME, id="$", mkstream=True)
    print(f"✅ Grupo de consumidores '{GROUP_NAME}' creado en {STREAM_NAME}")
except redis.exceptions.ResponseError:
    print(f"ℹ️ El grupo '{GROUP_NAME}' ya existe en {STREAM_NAME}")

print(f"📡 {consumer_id} escuchando en '{STREAM_NAME}' dentro del grupo '{GROUP_NAME}'...")

try:
    while True:
        # Leer mensajes del stream en el grupo de consumidores
        mensajes = r.xreadgroup(GROUP_NAME, consumer_id, {STREAM_NAME: ">"}, block=5000)
        
        for stream, data in mensajes:
            for msg_id, valores in data:
                print(f"📥 {consumer_id} recibió: {valores}")
                
                # Confirmar que el mensaje ha sido procesado
                r.xack(STREAM_NAME, GROUP_NAME, msg_id)

except KeyboardInterrupt:
    print(f"🚀 {consumer_id} detenido.")
