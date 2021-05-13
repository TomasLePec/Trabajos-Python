import json

registros = json.loads(open("regisxday.txt", "r").read()) #En estas dos lineas cargo los datos de las comidas y de los registros ya guardados.
comidas = json.loads(open("listaComidas.txt", "r").read())



def desayunar(fecha,comida,cant):
	registros.get(fecha)[0][0] = registros.get(fecha)[0][0] + porcant(comidas.get(comida)[0],cant)
	registros.get(fecha)[0][1] = registros.get(fecha)[0][1] + porcant(comidas.get(comida)[1],cant)
	registros.get(fecha)[0][2] = registros.get(fecha)[0][2] + porcant(comidas.get(comida)[2],cant)
	registros.get(fecha)[4][0] = registros.get(fecha)[4][0] + porcant(comidas.get(comida)[0],cant)
	registros.get(fecha)[4][1] = registros.get(fecha)[4][1] + porcant(comidas.get(comida)[1],cant)
	registros.get(fecha)[4][2] = registros.get(fecha)[4][2] + porcant(comidas.get(comida)[2],cant)
def almorzar(fecha,comida,cant):
	registros.get(fecha)[1][0] = registros.get(fecha)[1][0] + porcant(comidas.get(comida)[0],cant)
	registros.get(fecha)[1][1] = registros.get(fecha)[1][1] + porcant(comidas.get(comida)[1],cant)
	registros.get(fecha)[1][2] = registros.get(fecha)[1][2] + porcant(comidas.get(comida)[2],cant)
	registros.get(fecha)[4][0] = registros.get(fecha)[4][0] + porcant(comidas.get(comida)[0],cant)
	registros.get(fecha)[4][1] = registros.get(fecha)[4][1] + porcant(comidas.get(comida)[1],cant)
	registros.get(fecha)[4][2] = registros.get(fecha)[4][2] + porcant(comidas.get(comida)[2],cant)
def merendar(fecha,comida,cant):
	registros.get(fecha)[2][0] = registros.get(fecha)[2][0] + porcant(comidas.get(comida)[0],cant)
	registros.get(fecha)[2][1] = registros.get(fecha)[2][1] + porcant(comidas.get(comida)[1],cant)
	registros.get(fecha)[2][2] = registros.get(fecha)[2][2] + porcant(comidas.get(comida)[2],cant)
	registros.get(fecha)[4][0] = registros.get(fecha)[4][0] + porcant(comidas.get(comida)[0],cant)
	registros.get(fecha)[4][1] = registros.get(fecha)[4][1] + porcant(comidas.get(comida)[1],cant)
	registros.get(fecha)[4][2] = registros.get(fecha)[4][2] + porcant(comidas.get(comida)[2],cant)
def cenar(fecha,comida,cant):
	registros.get(fecha)[3][0] = registros.get(fecha)[3][0] + porcant(comidas.get(comida)[0],cant)
	registros.get(fecha)[3][1] = registros.get(fecha)[3][1] + porcant(comidas.get(comida)[1],cant)
	registros.get(fecha)[3][2] = registros.get(fecha)[3][2] + porcant(comidas.get(comida)[2],cant)
	registros.get(fecha)[4][0] = registros.get(fecha)[4][0] + porcant(comidas.get(comida)[0],cant)
	registros.get(fecha)[4][1] = registros.get(fecha)[4][1] + porcant(comidas.get(comida)[1],cant)
	registros.get(fecha)[4][2] = registros.get(fecha)[4][2] + porcant(comidas.get(comida)[2],cant)

def total(fecha):
	return registros.get(fecha)[4]

def desayuno(fecha):
	return registros.get(fecha)[0]

def almuerzo(fecha):
	return registros.get(fecha)[1]

def merienda(fecha):
	return registros.get(fecha)[2]

def cena(fecha):
	return registros.get(fecha)[3]

	
def porcant(x,y):
	return (y*x)/100

def caloriasDiarias(fecha):
	return (total(fecha)[0]*4 + total(fecha)[1] + total(fecha)[2]*9)
	


def agregarComida(nombre,carb,prot,gras): #agrega una comida al dict en el cual se guardan los datos, tener en cuenta que la cantidad de carb, prot, y gras, tienen que ser en gramos y la cantidad en 100g de dicho alimento
	comidas[nombre] = [carb,prot,gras]
	open("listaComidas.txt", "w").write(json.dumps(comidas)) 

def nuevaComida(fecha): #Agrega un dia al registro, una tupla de 5 array con 3 numeros, inicialmente 0 y se le suman dependiendo la cantidad de comida y qu comida se consume.
	registros[fecha] = ([0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0])
    open("regisxday.txt", "w").write(json.dumps(registros))


def borrarDia(fecha):
	registros.pop(fecha)
	open("regisxday.txt", "w").write(json.dumps(registros))

def borrarComida(nomre):
	comidas.pop(nombre)
	open("listaComidas.txt", "w").write(json.dumps(comidas)) 
	


def comer(fecha,n,quecomo,cant): #dependiendo el numero, suma a la respectiva comida.
	if n==1:
		desayunar(fecha,quecomo,cant)
	if n==2:
		almorzar(fecha,quecomo,cant)
	if n==3:
		merendar(fecha,quecomo,cant)
	if n==4:
		cenar(fecha,quecomo,cant)
