import requests

def main():
    print("Bienvenido a la API de NASA")
    print("Menú de opciones:")
    print("1. APOD")
    print("2. Earth")
    print("3. Mars rover photos")
    print("4. Exit")
    opcion= int(input("Elija una opcion: "))

while opcion != 4:
    if opcion == 1:
        callAPOD()
    
    elif opcion == 2:
        callEARTH()
    
    elif opcion == 3:
        callMARS()
    
    elif opcion == 4:
        print("Gracias por utilizar la api de NASA")
        print("Recuerda, \n esto es un pequeño paso para el hombre pero un gran paso para la humanidad")
    
    else:
        print("Opcion no valida")

    print("Menú de opciones:")
    print("1. APOD")
    print("2. Earth")
    print("3. Mars rover photos")
    print("4. Exit")
    opcion= int(input("Elija una opcion: "))

def callAPOD():

    # introduzco la clave de acceso de la api
    api_key = "6emoPuOxQti3D0zHnB99O58fdlaCcfi3necgMgHz"  
    
    #Defino la direccion de la api y le paso por parametro la clave de acceso
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}" 

    #Realizo la peticion a la api
    response = requests.get(url)

    #Verifico si la peticion fue exitosa, en caso contrario nos da un valor diferente de 200
    if response.status_code == 200:
        
        # Convierto la respuesta en JSON para poder utilizarlo
        datos = response.json()

        # Muestro la informacion obtenida
        print("Esta es la fotografía astronomica del día:")
        print("Título:", datos['title'])
        print("Fecha:", datos['date'])
    
def callEARTH():

    #se le pide al usuario los datos a consultar
    lon= float(input("Introduzca la longitud: "))
    lat= float(input("Introduzca la latitud: "))
    date= input("Introduzca la fecha (YYYY-MM-DD): ")

    # introduzco la clave de acceso de la api
    api_key = "6emoPuOxQti3D0zHnB99O58fdlaCcfi3necgMgHz"  
    
    #Defino la direccion de la api y le paso por parametro la clave de acceso
    url = f"https://api.nasa.gov/planetary/earth/imagery?lon={lon}&lat={lat}&date={date}&api_key={api_key}" 

    #Realizo la peticion a la api
    response = requests.get(url)

    #Verifico si la peticion fue exitosa, en caso contrario nos da un valor diferente de 200
    if response.status_code == 200:
        
        # Convierto la respuesta en JSON para poder utilizarlo
        datos = response.json()

        # Muestro la informacion obtenida
        print("Esta es la imagen de la tierra:")
        print("Título:", datos['title']) # muestro el titulo
        print("Fecha:", datos['date']) # muestro la fecha
        print("Url:", datos['url']) # muestro la url de la imagen

def callMARS():

    #se le pide al usuario los datos a consultar
    sol= int(input("Introduzca el sol: "))

    #introduzco la clave de acceso de la api
    api_key = "6emoPuOxQti3D0zHnB99O58fdlaCcfi3necgMgHz"

    #Defino la direccion de la api y le paso por parametro la clave de acceso
    url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol={sol}&api_key={api_key}" 

    #Realizo la peticion a la api
    response = requests.get(url)

    #Verifico si la peticion fue exitosa, en caso contrario nos da un valor diferente de 200
    if response.status_code == 200:
        
        # Convierto la respuesta en JSON para poder utilizarlo
        datos = response.json()

        # Muestro la informacion obtenida
        print("Esta es la imagen sacada por la rover:")
        print("Título:", datos['name']) # muestro el titulo
        print("Fecha:", datos['earth_date']) # muestro la fecha
        print("Url:", datos['img_src']) # muestro la url de la imagen