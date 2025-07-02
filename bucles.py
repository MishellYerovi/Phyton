my_list = ["Génesis""", "Éxodo", "Levítico", "Números","Deutoronomio"]
for index in (my_list):
    print ("Hay: ",len(my_list), "elementos en la lista")
    #Para imprimir la posición, se manda a  buscar el elemento 
    #que se va a imprimir dentro de la misma lista y se obtiene la posición
    #NO ES TAN EFICAZ porque puede existir dos o más elementos iguales dentro de la lista
    print ("El libro número ",my_list.index(index)+1,"del pentateuco es: ", index)
    
