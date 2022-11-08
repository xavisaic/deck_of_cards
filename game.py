from classes.deck import Deck

bicycle = Deck()

bicycle.show_cards()
victoria_CPU = 0
victorias_Usuario = 0
while True:
    print("estamos jugando a la carta mayor\n")

    mazo = Deck()
    cartaCPU = mazo.dame_carta()
    carta_usuario = mazo.dame_carta()

    print("la carta de la CPU es")
    cartaCPU.card_info()

    print("la carta del usuario es")
    carta_usuario.card_info()

    if cartaCPU.comparar(carta_usuario):
        print('la casa gana')
        victoria_CPU += 1
    else:
        victorias_Usuario += 1
        print('gana el usuario')

    respuesta = input('''desea continuar otro juego?:
    *presione 's' para continuar
    *presione 'n' para salir\n''')

    if respuesta == 'n':
        print("hasta la proxima")
        break
    elif respuesta == 's':
        print("A Jugar!")
    else:
        print("respuesta invalida")
        







# import pdb
# pdb.set_trace()





