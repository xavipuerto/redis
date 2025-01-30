import redis
import random
import time

# Con la función de streams se almacena la data con timestamps

# Conexión a Redis
r = redis.Redis(host='localhost', port=6379, password='password123', decode_responses=True)

def generar_valores_sensor():
    return {
        'temperatura': round(random.uniform(20.0, 30.0), 2),
        'humedad': round(random.uniform(30.0, 60.0), 2),
        'presion': round(random.uniform(1000.0, 1020.0), 2)
    }

try:
    while True:
        valores = generar_valores_sensor()
        r.xadd("sensorica_stream", {"temperatura": valores["temperatura"], 
                                    "humedad": valores["humedad"], 
                                    "presion": valores["presion"]}, "*")  
        print(f"✅ Valor agregado al Stream: {valores}")
        time.sleep(1)
except Exception as e:
    print(f"❌ Error al enviar valores: {e}")
except KeyboardInterrupt:
    print("⏹️ Proceso detenido por el usuario")
