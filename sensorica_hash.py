import redis
import random
import time

# Con la funcion del hash solo se persiste el ultimo valor

# Conexión a Redis
r = redis.Redis(host='localhost', port=6379, password='password123', decode_responses=True)

# Función para generar valores aleatorios de sensórica
def generar_valores_sensor():
    return {
        'temperatura': round(random.uniform(20.0, 30.0), 2),
        'humedad': round(random.uniform(30.0, 60.0), 2),
        'presion': round(random.uniform(1000.0, 1020.0), 2)
    }

# Enviar valores a Redis cada segundo
try:
    while True:
        valores = generar_valores_sensor()
        r.hset('sensorica', mapping=valores)  # ⚡ Usar `hset()` en vez de `hmset()`
        print(f"✅ Valores enviados: {valores}")
        time.sleep(1)
except Exception as e:
    print(f"❌ Error al enviar valores: {e}")
except KeyboardInterrupt:
    print("⏹️ Proceso detenido por el usuario")
