names = []
print (names)

# Método append para agregar elementos al final de la lista
names.append("Charly")
names.append("Mar")
names.append("Daniel")
names.append("Mancilla")

print(names)
print(type(names))
print(len(names))

# método insert para agregar elementos en una posición deseada (primero indice y despues el elemento que quiero agregar)
names.insert(1,"Héctor")
print(names)

# Método pop() sin indice para eliminar el ultimo elemento de la lista
names.pop()
print(names)

# Metodo pop() sin indice para eliminar el ultimo elemento deseado
names.pop(2)
print(names)

# Metodo remove(val) para eliminar elementos por valor
names.remove("Charly")
print(names)