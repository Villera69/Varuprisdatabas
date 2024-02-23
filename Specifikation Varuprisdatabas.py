#Titel: Varuprisdatabas
#Uppgiftens nr: 145
#Författare: William Ramsfeldt
#Datum: 2024-01-17


#Det här är ett program för hantering av varor.
#Programmet lagrar varor som finns i en butik i en fil med namnet "varor.txt" mellan körningarna av programmet.

#Varu-objekten lagras i en lista varu_lista som är ett attribut i klassen butik

#En klass som beskriver en vara:
#   kod - en varuspecifik kod som identifierar vilken vara det är
#   namn - namnet på varan
#   pris;antal - priset på varan samt antalet av varan

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
        return sträng

    def köp(self, antal): 
        """Minskar antalet av en varutyp om det finns tillräckligt med varor i lagret. 
        Inparameter: self, antal (int)
        Returnerar: inget""" 
        pass

# En klass som beskriver en Butik:
#   varu_lista - en lista som innehåller samtliga varor.
    
class Butik:
    def __init__(self, alla_varor):
        """Skapar ett Butik-objekt med alla_varor som inparameter.
        Inparametrar: self, alla_varor (lista med varu-objekt)
        Returnerar: inget """
        self.varu_lista = alla_varor
        
    def __str__(self):
      """Returnerar en sträng som beskriver butikens alla varor.
        Inparametrar: self
        Returnerar: en sträng som beskriver butikens varor"""
        #return sträng

    def lägg_till_vara(self, vara):
        """Lägger till en ny vara, 
        Inparameter: self, vara (varu-objekt)"""
    pass


#------Funktioner------------

def läs_in(filnamn):
    """läser från fil och skapar en varu-lista som returnerars, 
    Inparameter: filnamn (sträng)
    Returnerar: varu_lista (lista) """
    return varu_lista

def spara(filnamn, varu_lista): 
    """Sparar alla varor i varu-listan till en fil. 
    Inparameter: filnam (sträng), varu-lista (lista)
    Returnerar: ingenting""" 
    pass

def huvud_meny(): 
    """Skriver ut valmenyn med huvudvalen
    Inparameter: ingenting
    Returnerar: ingenting """
    pass
  
def registrera_nytt_köp(varu_lista): 
    """Ger användaren möjlighet att mata in data för ett nytt köp.
    Inparameter: ingenting
    Returnerar: varu_lista"""
    return varu_lista

def välj(): 
    """ Läser in och returnerar användarens val. 
    Inparameter: ingenting
    Returnerar: val (str)"""
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
pass


"""

TIDSPLAN

Vecka 3: Välja uppgift och börja fundera över datastrukturer och klasser.

Vecka 4 och 5: Arbeta med Specifikationen

Vecka 6: Redovisa Specifikation, börja med första prototypen.

Vecka 7-8: Jobba med prototyp 1, se till att klasserna finns och filinläsning/skrivning till fil fungerar.

Vecka 9: Redovisa prototyp 1

Vecka 10-11: Tentaperiod, fokusera på andra kurser

Vecka 12-13: Jobba med prototyp 2, se till att grundläggande funktionalitet finns.

Vecka 14: Redovisa prototyp 2.

Vecka 15: Jobba med att implementera C-kravet.

Vecka 16: jobba med att implementera B-kravet.

Vecka 17-18: Jobba med att implementera A-kravet.

Vecka 19: Göra granskningen, boka redovisningstid.

Vecka 20: Lämna in och redovisa.

"""