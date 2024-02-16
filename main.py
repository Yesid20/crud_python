import modulo as mo


print("Quieres ayudarme con una encuesta?")
question = int(input("Marca 1 para si o 2 para no: "))

if question == 1:
    mo.registro()
    print("Se registro exitosamente")
    ques = int(input("Quieres ver a los registrados?, marca 1 para si o 2 para actualizar o 3 para eliminar"))
    if  ques == 1:
        mo.leer()
    elif ques == 2:
        mo.actualizar()
    elif ques == 3:
        mo.eliminar_registro()
elif question == 2:
    print("Muchas gracias por intentarlo")