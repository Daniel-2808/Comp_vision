#Este programa pide al usuario una cantidad en pesos mexicanos.
# También pide el porcentaje de iva y el porcentaje de propiba.
# El programa debe calcular el monto total a pagar por el cliente.

subtotal_txt = input("Subtotal(mxn):")
iva_txt = input("IVA(%) ej. 16:")
propina_txt = input("Propina(%)rj. 10:")

try:
    # Metodo built-in float - convierte a un dato del tipo flotante
    subtotal = float(subtotal_txt)
    iva = float(iva_txt)/100
    propina = float(propina_txt)/100

    
