import redis

# Conectar a Redis con autenticación
r = redis.Redis(host="localhost", port=6379, password="password123", decode_responses=True)

# Crear un suscriptor y suscribirse al canal
pubsub = r.pubsub()
pubsub.subscribe("canal_sensorica")

print("📡 Suscriptor escuchando en 'canal_sensorica'...")

try:
    for mensaje in pubsub.listen():
        if mensaje["type"] == "message":
            print(f"📥 Mensaje recibido: {mensaje['data']}")
except Exception as e:
    print(f"❌ Error al recibir mensaje: {e}")
except KeyboardInterrupt:
    print("🚀 Suscriptor detenido.")
    