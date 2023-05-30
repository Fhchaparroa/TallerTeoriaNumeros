numeros25 = []
numeros16 = []
numeros9 = []
numerosFinal = []
for i in range(1, 1000): numeros25.append((25*i)+23) , numeros16.append((16*i)+15) , numeros9.append((9*i))
for i in numeros9:
    if i in numeros16 and i in numeros25: numerosFinal.append(i)
print(numerosFinal)