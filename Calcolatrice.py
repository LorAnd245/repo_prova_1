print("Benvenuto nella nostra calcolatrice")
a = int(input("Inserisci il primo numero: "))
operazione = input("Inserisci l'operazione da effettuare: ")
b = int(input("Inserisci il secondo numero: "))
risultato = 0
if operazione == "+":
    risultato = a + b
elif operazione == "-":
    risultato = a - b
elif operazione == "/":
    risultato = a / b
elif operazione == "*":
    risultato = a * b
else:
    risultato = "error"

print(f"{a} {operazione} {b} = {risultato}")