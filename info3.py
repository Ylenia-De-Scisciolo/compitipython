numerocifre = int(input("Da quante cifre e composto il numero binario?"))
print("Digitare le cifre binarie una alla volta a partire da destra")
elevatorepotenze = 0
numerodecimale = 0
for i in range(numero_cifre):
    cifra=int(input())
    numerodasommare = cifra*(2 ** elevatorepotenze)
    numerodecimale += numerodasommare
    elevatorepotenze += 1
numerobinario=input("Non sono sicuro di aver fatto giusto, potresti riscrivere il numero da sinistra verso destra?")
numerocerto = int(numero_binario, 2)
if numerodecimale == numerocerto:
    print("Il numero decimale e ", numerodecimale)
else:
    print("Il numero decimale e sbagliato")