with open("sekwencje", "r")  as s:
	lista = []
	data = s.read()
	data=data.split()
	for line in data:	
		lista.append(line.rstrip())
		
	for y in range(1,len(lista),1):
		print(lista[y], "\n")
	macierz = [[i for i in lista[y]] for y in range(1,len(lista),2)]
 
	mac = [[0 for i in range(0,len(lista)+3,2)] for y in range(4)]

	
	for i in range(0,len(macierz[1]),1):
		for y in range(len(macierz)):
			if macierz[y][i] == "A":
				mac[0][i+1] += 1 
			elif macierz[y][i] == "C":
				mac[1][i+1] +=1
			elif macierz[y][i] == "G":
				mac[2][i+1] +=1
			elif macierz[y][i] == "T":
				mac[3][i+1] +=1
			
	mac[0][0] = "A:"
	mac[1][0] = "C:"
	mac[2][0] = "G:"
	mac[3][0] = "T:"
	print("\n".join(["".join(["{:4}".format(item) for item in row]) for row in mac]))
	
