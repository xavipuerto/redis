import redis
import time

# Conexión a Redis en el Docker con autenticación
r = redis.Redis(host='localhost', port=6379, password='password123', decode_responses=True)

# Función para purgar elementos antiguos
def purgar_lista(max_edad_segundos=60):
    ahora = int(time.time())
    elementos = r.lrange("historico_sensorica", 0, -1)  # Obtener todos los valores
    
    eliminados = []
    for elem in elementos:
        partes = elem.split(":")  # Separar timestamp del valor
        if len(partes) < 2:
            continue  # Evitar errores si el formato no es correcto

        timestamp = int(partes[0])
        if ahora - timestamp > max_edad_segundos:  # Si el dato es demasiado viejo
            eliminados.append(elem)

    if eliminados:
        print(f"🗑️ Se eliminarán los siguientes datos: {eliminados}")
        for item in eliminados:
            r.lrem("historico_sensorica", 0, item)  # Borrar elemento

try:
    while True:
        purgar_lista(60)  # Mantener solo datos de los últimos 60 segundos
        print("✅ Datos purgados correctamente")
        time.sleep(10)
except Exception as e:
    print(f"❌ Error al purgar datos: {e}")
except KeyboardInterrupt:
    print("⏹️ Proceso de purga detenido por el usuario")
