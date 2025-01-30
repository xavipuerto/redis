import redis

redis_host = "192.168.1.178"  # IP de tu Ubuntu en Parallels
redis_port = 6379  # Puerto estándar de Redis

try:
    r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)
    response = r.ping()
    if response:
        print("✅ Conexión exitosa a Redis")
except Exception as e:
    print(f"❌ Error al conectar: {e}")
