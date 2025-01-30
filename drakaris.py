import redis

# Conectar a Redis con autenticación
r = redis.Redis(host="localhost", port=6379, password="password123", decode_responses=True)

# Nombre del Stream a eliminar
STREAM_NAME = "sensorica_stream_persistent"

try:
    # Obtener los grupos de consumidores y eliminarlos
    grupos = r.xinfo_groups(STREAM_NAME)
    for grupo in grupos:
        group_name = grupo["name"]
        r.xgroup_destroy(STREAM_NAME, group_name)
        print(f"🔥 Grupo de consumidores '{group_name}' eliminado.")

    # Eliminar el Stream completamente
    r.delete(STREAM_NAME)
    print(f"🔥 Stream '{STREAM_NAME}' eliminado por completo.")

    # Opcional: Borrar TODAS las claves de Redis (⚠️ BORRARÁ TODO en Redis)
    borrar_todo = input("⚠️ ¿Quieres eliminar TODA la base de datos de Redis? (sí/no): ").strip().lower()
    if borrar_todo == "sí":
        r.flushall()
        print("🔥🔥🔥 ¡DRAKARIS! 🔥🔥🔥 Toda la base de datos de Redis ha sido eliminada.")

except redis.exceptions.ResponseError as e:
    print(f"❌ Error al eliminar: {e}")

print("🚀 Purga completa.")
