import redis

r = redis.Redis(host='192.168.1.178', port=6379, decode_responses=True)

# Guardar un string
try:
    r.set('name', 'Peter')
    print("✅ Valor guardado correctamente")    
except Exception as e:
    print(f"❌ Error al guardar: {e}")  


# Guardar un hash individual
r.hset('person', 'name', 'Peter')
r.hset('person', 'age', 25)
r.hset('person', 'city', 'New York')

# Guardar múltiples valores en un hash correctamente
r.hmset('humans', {'Peter': 25, 'John': 30, 'Sara': 22})

# Otra forma correcta de agregar más datos al mismo hash
r.hmset('humans', {'ted': 20, 'jane': 24})

# Obtener valores
print("\n Name")
print(r.get('name'))            # "Peter"
print("\n Person")
print(r.hgetall('person'))      # {'name': 'Peter', 'age': '25', 'city': 'New York'}
print("\n Humans")
print(r.hgetall('humans'))      # {'Peter': '25', 'John': '30', 'Sara': '22', 'ted': '20', 'jane': '24'}
