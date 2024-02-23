#Titel: Varuprisdatabas
#Uppgiftens nr: 145
#Författare: William Ramsfeldt
#Datum: 2024-01-17

class Vara:

    def __init__(self, kod, namn, pris, antal):
        """Skapar en ny vara.
        Inparametrar: self, kod (int), namn (sträng), pris (float) och antal (int)"""
        self.kod = kod
        self.namn = namn
        self.pris = pris
        self.antal = antal

    def __str__(self):
        """Returnerar en sträng som beskriver varan.
        Inparametrar: self
        Returnerar: en sträng som beskriver varan"""
        return f"{self.namn} kod: {self.kod} pris: {self.pris} antal: {self.antal}"
 

    def köp(self, antal): 
        """Minskar antalet av en varutyp om det finns tillräckligt med varor i lagret. 
        Inparameter: self, antal (int)
        Returnerar: inget""" 
        self.antal -= antal
   
def läs_in(filnamn):
    """läser från fil och skapar en varu-lista som returnerars, 
    Inparameter: filnamn (sträng)
    Returnerar: varu_lista (lista) """
    varulista = []
    attributsträng = ""
    varufil = open(filnamn, "r", encoding = "utf-8")
    while True:
        for i in range(4):
            rad = varufil.readline().strip()
            attributsträng += f"{rad} "
        if rad == "":
            break        
        attributsträng = attributsträng.split()
        vara = Vara(int(attributsträng[0]), attributsträng[1], float(attributsträng[2]), int(attributsträng[3]))
        varulista.append(vara)
        attributsträng = ""
    varufil.close()
    return varulista

def spara(filnamn, varulista): 
    """Sparar alla varor i varu-listan till en fil. 
    Inparameter: filnam (sträng), varu-lista (lista)
    Returnerar: ingenting""" 
    varufil = open(filnamn, "w", encoding = "utf-8")
    for vara in varulista:
        varufil.write(f"{vara.kod}\n{vara.namn}\n{vara.pris}\n{vara.antal}\n")
    varufil.close()

def huvud_meny(filnamn, varulista): 
    """Skriver ut valmenyn med huvudvalen
    Inparameter: ingenting
    Returnerar: ingenting """
    fortsätt = True
    while fortsätt:
        print("(1) Registrera ett nytt köp\n(2) Avsluta programmet.")
        val = välj()
        if  val == "1":
            varulista = registrera_nytt_köp(varulista)
        elif val == "2":
            spara(filnamn, varulista)
            print("Nu avslutas programmet och varudatabasen sparas.")
            fortsätt = False
  
def registrera_nytt_köp(varulista): 
    """Ger användaren möjlighet att mata in data för ett nytt köp.
    Inparameter: ingenting
    Returnerar: varu_lista"""
    rad = [""]
    summa_pris = 0.0
    summa_antal = 0
    kvittosträng = "{:<10} {:<5} {:>10} {:>10} ".format("Varunamn", "Antal", "A-pris", "Summa",) + "\n" + "-"*38
    print("Registrera en köpt vara genom att skriva varans kod. För köp av mer än en vara med samma varukod, gör ett mellanslag efter varukoden följt av antalet av denna vara. Efter att alla varor har matats in, skriv # på en tom rad.")
    while rad[0] != "#":
        rad = input().split()
        for vara in varulista:
            if str(vara.kod) == rad[0]:
                try:
                    antal = int(rad[1])
                except IndexError:
                    antal = 1
                vara.köp(antal)
                summa_antal += antal
                summa_pris += antal*vara.pris
                kvittosträng += "\n" + "{:<10} {:<5} {:>10} {:>10}".format(vara.namn, antal, format(vara.pris,".2f"), format(antal*vara.pris,".2f"))
    kvittosträng += "\n" + "="*38 + "\n" + "{:<10} {:<5} {:>21} ".format("Total", summa_antal, format(summa_pris,".2f"))
    input(f"\nNu har detta köp registreras. Kvittot ser ut såhär:\n\n{kvittosträng}\n\nTryck enter för att komma tillbaka till huvudmenyn.\n\n\n")
    return varulista

def välj(): 
    """ Läser in och returnerar användarens val. 
    Inparameter: ingenting
    Returnerar: val (str)"""
    val = input("Välj en av siffrorna i menyn: ")
    return val
    

# Huvudprogram
def huvudprogram():
    """Algoritm:
    1. Hälsar välkommen
    2. Läser in filen med alla varor och skapar varu-objekt som sedan skickas med för att skapa en varu_lista.
    3. Presenterar en meny
    4. Låter användare välja ett menyval eller att avsluta
    5. Om användaren inte väljer att avsluta, utför det valda menyvalet
    6. Upprepar steg 3-5, tills det att användaren väljer att avsluta
    7. Sparar till fil
    8. Avslutar programmet
    """
    filnamn = "Varuprisdatabas.txt"
    varulista = läs_in(filnamn) 
    print("Hej och välkommen till varuprisdatabasen.\n")
    huvud_meny(filnamn, varulista)

huvudprogram()