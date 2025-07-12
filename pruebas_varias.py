diccionarios = {"jose":10, "carlos":23, "maria":33}
print("carlos: ", diccionarios.get("carlos"))

#for i in diccionarios.values():
#for i in diccionarios:
for c,v in diccionarios.items():
    #print(i)
    #print(diccionarios.get(i))
    print(c+"-"+str(v))