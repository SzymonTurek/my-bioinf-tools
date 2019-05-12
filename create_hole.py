from pymol import cmd
xyz, xyz2 = [],[]
cmd.iterate_state(1, "cholesterole", "xyz.append([resi,x,y,z])")
cmd.iterate_state(1, "blona_duza", "xyz2.append([resi,x,y,z])")
print("Maksimum X: " +str(max(xyz, key=lambda item: item[1])))
print("Minimum X: " +str(min(xyz, key=lambda item: item[1])))
print("Maksimum Y: " +str(max(xyz, key=lambda item: item[2])))
print("Minimum Y: " +str(min(xyz, key=lambda item: item[2])))
maksimum= max(xyz, key=lambda item: item[1])
minimum=min(xyz, key=lambda item: item[1])
maksimum_y=max(xyz, key=lambda item: item[2])
minimum_y=min(xyz, key=lambda item: item[2])

lista=[]
for i in range( len(xyz2)):
if (xyz2[i][1] <maksimum[1]-5 and xyz2[i][1] > minimum[1]+5 and
xyz2[i][2]<maksimum_y[2]-5 and xyz2[i][2]>minimum_y[2]+5):
#print xyz2[i]
lista.append(xyz2[i])
print("Reszty do usuniecia:")
zety=[]
for m in range(len(lista)):

11

zety.append(lista[m][3])
suma=0
for k in range(len(zety)): suma+=1
print suma
nowa_lista=[]
for z in range(len(lista)):
nowa_lista.append(int(lista[z][0]))
nowa_nowa_lista=set(nowa_lista)
do_usuniecia = sorted(nowa_nowa_lista)
print do_usuniecia
for j in do_usuniecia:
cmd.remove( "resi %d"% j)
