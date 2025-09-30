# variable tipo de texto
dispositivo = "Computador"
print(dispositivo)
print(type(dispositivo))

# variable de tipo entero
cantidad = 45
print(cantidad)
print(type(cantidad))

# variable de tipo decimal / flotante
precio = 14.99
print(precio)
print(type(precio))

# variable de tipo decimal / cadena
precio = "14.99"
print(precio)
print(type(precio))

is_active_client = True
print(is_active_client)
print(type(is_active_client))

# Trabajando con fecha
from datetime import date
fecha_clase = date(1987, 5, 31) # (yyyy, mm, dd)
print(fecha_clase)
print(f"la fecha de hoy: {fecha_clase}")
print(type(fecha_clase))