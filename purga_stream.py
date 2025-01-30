import redis
import time

# Conectar a Redis con autenticación
r = redis.Redis(host="localhost", port=6379, password="password123", decode_responses=True)

# Nombre del stream
STREAM_NAME = "sensorica_stream_persistent"

# Límite de mensajes permitidos en el Stream
NUM_MENSAJES = 100

try:
    while True:
        try:
            # Obtener los mensajes que serán eliminados (todos los que están por encima del límite)
            mensajes_totales = r.xlen(STREAM_NAME)  # Cuántos mensajes hay en total
            if mensajes_totales > NUM_MENSAJES:
                # Calcular cuántos mensajes van a ser eliminados
                mensajes_a_eliminar = mensajes_totales - NUM_MENSAJES
                
                # Obtener los mensajes más antiguos que serán eliminados
                mensajes_borrados = r.xrange(STREAM_NAME, count=mensajes_a_eliminar)
                
                # Imprimir los mensajes que serán eliminados
                print("\n🗑️  Mensajes eliminados:")
                for msg_id, valores in mensajes_borrados:
                    print(f"  🗑️ ID: {msg_id}, Datos: {valores}")

                # Ejecutar el recorte del stream
                resultado = r.xtrim(STREAM_NAME, maxlen=NUM_MENSAJES)
                print(f"✅ Stream '{STREAM_NAME}' limitado a los últimos {NUM_MENSAJES} mensajes (eliminados {resultado} mensajes antiguos).")

        except Exception as e:
            print(f"❌ Error al recortar el Stream: {e}")

        time.sleep(10)  # Espera 10 segundos antes de volver a ejecutar la purga

except KeyboardInterrupt:
    print("🚀 Proceso de purga detenido.")
