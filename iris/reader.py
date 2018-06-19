print("Lendo Dataset")
with open ('dataset.txt', 'r') as arq:
	dataset = arq.readlines()
print("%d registros carregados" % len(dataset))

#debuging
for linha in dataset:
	print(linha)
