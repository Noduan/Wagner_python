subtotal = float(input("Ingresa el total"))

monto_igv = float(subtotal) * 0.18

monto_pagar = float(subtotal) + monto_igv

print(f"MONTO DE SUBTOTAL : {subtotal}")
print(f"MONTO DE IGV 18% : {monto_igv}")
print(f"MONTO TOTAL A PAGAR : {monto_pagar}")