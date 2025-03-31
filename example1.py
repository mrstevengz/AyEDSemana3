#Leer x cantidad de edad y calcular la media

class Edad:
    def __init__(self, edad):
        self.edad = edad

    def calcular_media(self):
        return sum(self.edad) / len(self.edad)

    def mostrar_media(self):
        media = self.calcular_media()
        return f"La media de las edades es: {media:.2f}"

def main():
    edades = []
    
    while True:
        try:
            edad = int(input("Ingrese una edad (o -1 para terminar): "))
            if edad == -1:
                break
            edades.append(edad)
        except ValueError:
            print("Por favor, ingrese un número válido.")

    if (not edades):
        print("No se ingresaron edades.")
        return
    else:    
        edad_obj = Edad(edades)
        print(edad_obj.mostrar_media())

if __name__ == "__main__":
    main()