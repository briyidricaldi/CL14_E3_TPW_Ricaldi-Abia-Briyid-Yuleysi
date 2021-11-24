import random
def main():
    print("OBTENER VALOR (1,3,6)")
    numero = int(input("Número de jugadores: "))
    if numero < 1:
        print("¡Imposible!")
    else:
        objetivo = int(input("Valor a conseguir: "))
        if objetivo < 1 or objetivo > 6:
            print(f"¡Imposible conseguir un {objetivo}!")
        else:
            for i in range(numero):
                dado = random.randrange(1, 7)
                if dado == objetivo:
                    print(f"Jugador {i + 1}: {dado} ENCONTRADO")
                else:
                    print(f"Jugador {i + 1}: {dado}")

                        
if __name__ == "__main__":
    main()