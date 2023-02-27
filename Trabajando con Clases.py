class Motocicleta:
    def __init__(   self, color, matricula, marca, modelo, fecha_fabricacion, velocidad_punta, peso):
        self.nueva = True
        self.color = color
        self.matricula = matricula
        self.combustible_litos = 10
        self.numero_ruedas = 2
        self.marca = marca
        self.modelo = modelo
        self.fecha_fabricacion = fecha_fabricacion
        self.velocidad_punta = velocidad_punta
        self.peso = peso
        self.motor = False

    def arrancar(self):
        if self.motor == True:
            print("El motor ya ha arrancado")
        else:
            self.motor=True
            print("El motor ha arrancado")
    def detener(self):
        if self.motor == False:
            print ("El motor está apagado")
        else:
            self.motor = False
            print ("El motor se ha apagado")
    def consulta_precio(self):
        print ("El precio de la motocicleta es de", self.precio, "pesos colombianos")

MotoCarlos = Motocicleta(matricula='Hola', marca="Bugati",modelo="1920",fecha_fabricacion="1915",velocidad_punta=150,peso=50,color="verde")
MotoCarlos.arrancar()
MotoCarlos.arrancar()
MotoCarlos.detener()
MotoCarlos.arrancar()
MotoCarlos.detener()
MotoCarlos.detener()
print(MotoCarlos.numero_ruedas)
MotoCarlos.precio = 10000000
MotoCarlos.consulta_precio()