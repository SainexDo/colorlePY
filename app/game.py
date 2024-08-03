from colorama import Fore
from time import sleep
import keyboard
import random

class Game:
    #Juego, dividido en sus respectivas clases y métodos.
    def __init__(self, rojo, azul, verde, amarillo, reset):
        self.rojo = rojo
        self.azul = azul
        self.verde = verde
        self.amarillo = amarillo
        self.reset = reset
        #Declaramos variables privadas.
        self.secuencia = []
        self.intentoDeAdivinarSecuencia = []
    
    def elegirModo(self):
        while True:
            respuesta = input(f'¿Adivinas o creas la secuencia? (Adivinar / Crear): ').strip().lower()
            if respuesta not in ('adivinar', 'crear'):
                print("Agrega una respuesta correcta.")
            else:
                if respuesta == 'adivinar':
                    self.creaComputadora()
                elif respuesta == 'crear':
                    self.creaJugador()
                break
    
        
                
                
                
    def creaJugador(self):
        posiblesOpciones = (self.rojo, self.azul, self.amarillo, self.verde)
        while True:
            opcion = input("Elige los colores de tu secuencia (r/b/y/g)")
            if len(self.secuencia) <= 4:
                if opcion == "r":
                    self.secuencia.append(posiblesOpciones[0])
                    print("|", "".join(self.secuencia) + self.reset, "" + "|") 
                elif opcion == "b":
                    self.secuencia.append(posiblesOpciones[1])
                    print("|", "".join(self.secuencia) + self.reset, "" + "|")
                elif opcion == "y":
                    self.secuencia.append(posiblesOpciones[2])
                    print("|", "".join(self.secuencia) + self.reset, "" + "|")
                elif opcion == "g":
                    self.secuencia.append(posiblesOpciones[3])
                    print("|", "".join(self.secuencia) + self.reset, "|")
                if len(self.secuencia) == 4:
                    break
        
        

    def creaComputadora(self):
        while True:
            posiblesOpciones = (self.rojo, self.azul, self.amarillo, self.verde)
            self.secuencia.insert(1, random.choice(posiblesOpciones) + self.reset)
            if len(self.secuencia) == 4:
                print(''.join(self.secuencia) + self.reset)
                break

def main():
    Juego = Game(azul=(Fore.BLUE + " O "), rojo=(Fore.RED + " O "), amarillo=(Fore.YELLOW + " O "), verde=(Fore.GREEN + " O "), reset=Fore.RESET)
    Juego.elegirModo()

if __name__ == "__main__":
    # Inicializador del archivo.
    main()