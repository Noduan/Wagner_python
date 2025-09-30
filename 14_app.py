# Estructura condicional if (si) - else (si no)
# Sintaxis
# if condicion
#   instrucciones a ejecutarse si la condicon es vedadera
# elif:
#   instrucciones a ejecutarse en la siguiente condicion
# else:
#   instrucciones a ejercuratse si la condición es falsa
# ejemplo
# nota 0 - 12.4 : desaprobado
# nota 12.5 - 16 : Aprobado
# nota 17 - 20 : Muy bien sigue así
nota = 19
if nota <=12.4:
    print(f"Ud. a desaprobado el curso , su nota es : {nota}")
elif nota <=16:
    print(f"Ud. a aprobado el curso, su nota es : {nota}")
else:
    print(f"Muy bien, sigue así, su nota es : {nota}")