

try:
    # 10/0
    print(d['indice_no_existente'])
except ZeroDivisionError:
    print("No se puede dividir entre cero.")
except Exception:
    print("Se ha dado otro tipo de error descnocido")

print("hola que tal")