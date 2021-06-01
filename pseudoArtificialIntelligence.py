listDomande = []
listRisposte = []

def domanda():
    print("BOT > digita una domanda")
    strDomande = input("TU > ")
    if(strDomande not in listDomande):
        listDomande.append(strDomande)
        risposta()
    else:
        n = listDomande.index(strDomande)
        print("BOT > " + listRisposte[n])

def risposta():
    print("BOT > Non conosco la risposta, digita la risposta")
    strRisposta = input("TU > ")
    listRisposte.append(strRisposta)

def scambio():
    domanda()

while True:
    scambio()