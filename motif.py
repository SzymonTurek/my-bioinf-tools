def reada(filename):
	with open(filename) as file:
		seq=''
		line = file.readline()
		while line :
			if line[0]==">":

				seq+=","
				line = file.readline().rstrip()
			else:
				seq+=line
				line = file.readline().rstrip()
			
		lista = seq.split(",")	
		lista.pop(0)

		slowo = ''
		longest = ''
		a = lista[1]
		for i in range(len(a)):
			for x in range(len(a)):
	
				slowo = (a[i:x])

				if all(lista[z].__contains__(slowo) for z in range(len(lista))) and len(slowo)>=len(longest):
						longest = slowo

	return( longest)
	
print(reada('rosalind_lcsm.txt'))


