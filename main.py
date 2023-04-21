valor = float(input("Digite um valor"))
valor = int(valor)
if(valor<0):
    print("impossível!")
    print("não precisa se alistar.")
elif(valor<18 and valor>0):
    print("não precisa se alistar.")
elif(valor>18 and valor<65):
    print("Não esqueça de votar na próxima eleição.")
else:
    print("eita!")
