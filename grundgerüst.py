import random
import time
#Einleitung
def start():
    print("Willkommen bei Monopoly")
    anzahl = int(input("Wie viele Spieler spielen mit (2-4): "))
    return anzahl

#Die Würfel und Paschprüfung
def rolldice():
    global wurf1
    global wurf2
    global wurf
    wurf1 = random.randint(1,6)
    wurf2 = random.randint(1,6)
    wurf = wurf1 + wurf2


#Ausgabe der gewürfelten Zahlen
def wurfausgabe():
    global pasch;
    pasch = False;
    print("Sie haben eine " + str(wurf1) + " und eine " + str(wurf2) + " gewürfelt.")
    if wurf1 == wurf2:
        print("Sie haben einen Pasch gewürfelt!")
        pasch = True;


def initia():
    sp1.position = 0;
    sp2.position = 0;
    sp3.position = 0;
    sp4.position = 0;
    sp1.konto = 20000

def neueposition(x):
    global ueberlos;
    ueberlos = False;
    x.position = x.position + wurf
    if x.position > 39:
        x.position = x.position - 40;
        ueberlos = True;

def geld(x, g):
    x.konto = x.konto + g

def zahlen(x, g):
    x.konto = x.konto - g

"""
def werk():
    if was.bestizer == ele.besitzer:
        x = 200*wurf
    else:
        x = 80*wurf
    return x
"""
    
def kaufprüfung(y, x):
    if y.verkauft == False:
        print("Wollen Sie die/den " + y.name + " kaufen?")
        kaufen = eingabe()
        if kaufen == "Ja" and x.konto >= int(y.kaufpreis):
            x.konto = x.konto - y.kaufpreis;
            y.besitzer = x.name;
            y.verkauft = True;
            print(x.name + " hat die/den " + y.name + " gekauft.")
        elif kaufen == "Ja" and x.konto <= y.kaufpreis:
            print("Leider haben Sie nicht genug Geld auf ihrem Konto, um diese Straße zu kaufen.")
        elif kaufen == "Nein":
            print("Sie haben sich dagegen entschieden diese Straße zu kaufen.")
    elif y.verkauft == True and y.besitzer == x.name:
        print("Sie besitzen diese Straße schon.")
    elif y.verkauft == True and y.besitzer != x.name:
        if y.besitzer == sp1.name and int(x.konto) >= int(y.miete):
            x.konto = x.konto - y.miete
            print("Diese Straße wird schon von " + sp1.name + " besessen. Sie müssen " + y.miete + "€ Miete zahlen.")
            sp1.konto = sp1.konto + y.miete
        elif y.besitzer == sp2.name and int(x.konto) >= int(y.miete):
            x.konto = x.konto - y.miete
            print("Diese Straße wird schon von " + sp2.name + " besessen. Sie müssen " + y.miete + "€ Miete zahlen.")
            sp2.konto = sp2.konto + y.miete
        elif y.besitzer == sp3.name and int(x.konto) >= int(y.miete):
            x.konto = x.konto - y.miete
            print("Diese Straße wird schon von " + sp3.name + " besessen. Sie müssen " + y.miete + "€ Miete zahlen.")
            sp3.konto = sp3.konto + y.miete
        elif y.besitzer == sp4.name and int(x.konto) >= int(y.miete):
            x.konto = x.konto - y.miete
            print("Diese Straße wird schon von " + sp4.name + " besessen. Sie müssen " + y.miete + "€ Miete zahlen.")
            sp4.konto = sp4.konto + y.miete
        elif int(y.miete) > int(x.konto):
            print("Sie sind pleite!")

def gemeinschaft(x):
    z = random.randint(1, 17);
    if z == 1:
        print(x.name + ": Einkommenssteuerrückzahlung. Ziehe 400€ ein.")
        geld(x, 400)
    elif z == 2:
        print(x.name + ": Rücke vor bis auf Los.")
        x.position = 0
        geld(x, 4000)
    elif z == 3:
        print(x.name + ": Du wirst zu Straßenausbesserungsarbeiten herangezogen.")
        print("           Zahle für deine Häuser und Hotels:")
        print("           - 800€  je Haus")
        print("           - 2300€ je Hotel")
        print("           an die Bank.")
        x.konto = x.konto - (x.haus * 800) - (x.hotel * 2300)
    elif z == 4:
        print(x.name + ": Du bekommst eine Gefängnisfreikarte.")
        x.freikarte = True
    elif z == 5:
        print(x.name + ": Die Jahresrente wird fällig. Ziehe 2000€ ein.")
        geld(x, 2000)
    elif z == 6:
        print(x.name + ": Du erhälst auf Vorzugs-Aktien 7% Dividende. 900€")
        geld(x, 900)
    elif z == 7:
        print(x.name + ": Bank-Irrtum zu Deinen Gunsten. Ziehe 4000€ ein.")
        geld(x, 4000)
    elif z == 8:
        print(x.name + ": Zahle an das Krankenhaus: 2000€.")
        zahlen(x, 2000)
    elif z == 9:
        print(x.name + ": Arzt-Kosten. Zahle 1000€")
        zahlen(x, 1000)
    elif z == 10:
        print(x.name + ": Du hast den 2. Preis in einer Schönheitskonkurenz gewonnen.")
        print("           Ziehe 200€ ein.")
        geld(x, 200)
    elif z == 11:
        print(x.name + ": Aus Lagerverkäufen erhälst Du 500€.")
        geld(x, 500)
    elif z == 12:
        print(x.name + ": Du erbst 2000€.")
        geld(x, 2000)
    elif z == 13:
        print(x.name + ": Zahle 3000€ Schulgeld.")
        zahlen(x, 3000)
    elif z == 14:
        print(x.name + "Gehe in das Gefängnis.")
        x.position = 10
        x.gefängnis = True
    elif z == 15:
        print(x.name + "Es ist Dein Geburtstag. Ziehe von jedem Spieler 1000€ ein.")
        zahlen(sp1, 1000)
        zahlen(sp2, 1000)
        zahlen(sp3, 1000)
        zahlen(sp4, 1000)
        if k == 2:
            geld(x, 2000)
        elif k == 3:
            geld(x, 3000)
        elif k == 4:
            geld(x, 4000)
    elif z == 16:
        print(x.name + "Du hast in einem Kreuzworträtselwettbewerb gewonnen. Ziehe 2000€ ein.")
        geld(x, 2000)

def ereignis(x):
    z = random.randint(1, 16);
    if z == 1:
        print(x.name + ": Lasse alle Deine Häuser renovieren.")
        print("           Zahle an die Bank:")
        print("           - 500€  je Haus")
        print("           - 2000€ je Hotel")
        print("           an die Bank.")
        x.konto = x.konto - (x.haus * 500) - (x.hotel * 2000)
    elif z == 2:
        print(x.name + ": Mache einen Ausflug zum Südbahnhof.")
        if x.position < 6:
            x.position = 5
        else:
            x.position = 5
            geld(x, 4000) #Weitere Aktion einprogrammieren
    elif z == 3:
        print(x.name + ": Miete und Anleihezinsen werden fällig. Die Bank zahlt Dir 3000€.")
        geld(x, 3000)
    elif z == 4:
        print(x.name + ": Gehe 3 Felder zurück.")
        x.position = x.position - 3 #Weitere Aktion einprogrammieren.  
    elif z == 5:
        print(x.name + ": Du wurdest zum Vorstand gewählt. Zahle jedem Spieler 1000€.")
        geld(sp1, 1000)
        geld(sp2, 1000)
        geld(sp3, 1000)
        geld(sp4, 1000)
        if k == 2:
            zahlen(x, 2000)
        elif k == 3:
            zahlen(x, 3000)
        elif k == 4:
            zahlen(x, 4000)
    elif z == 6:
        print(x.name + ": Die Bank zahlt Dir eine Dividende von 1000€.")
        geld(x, 1000)  
    elif z == 7:
        print(x.name + ": Gehe in das Gefängnis.")
        x.gefängnis = True
        x.position = 10
    elif z == 8:
        print(x.name + ": Rücke bis auf Los vor.")
        x.position = 0
        geld(x, 4000)
    elif z == 9:
        print(x.name + ": Gehe zurück nach der Badstraße.")
        x.position = 1
        #weitere Aktion einprogrammieren
    elif z == 10:
        print(x.name + ": Rücke vor bis zur Seestraße.") 
        if x.position < 12:
            x.position = 11
            # Weitere Aktion einprogrammieren
        else:
            x.positon = 11
            geld(x, 4000)
    elif z == 11:
        print(x.name + ": Rücke vor bis zum Opernplatz")
        if x.position < 25:
            x.position = 24
            # Weitere Aktion einprogrammieren
        else:
            x.positon = 24
            geld(x, 4000)
    elif z == 12:
        print(x.name + ": Du bekommst eine Gefängnisfreikarte.")
        x.freikarte = True
    elif z == 13:
        print(x.name + ": Rücke vor bis zur Schlossalle.")
        x.position = 39
        #weitere Aktion einprogrammieren
    elif z == 14:
        print(x.name + ": Strafe für zu schnelles Fahren. 300€")
        zahlen(x, 300)
    elif z == 15:
        print(x.name + ": Zahle eine Strafe von 200€.")  
        zahlen(x, 200)

"""
def bahnhof(v):
    c = 0
    if v.besitzer == süd.besitzer:
        c = c + 1
    if v.besitzer == wes.besitzer:
        c = c + 1
    if v.besitzer == nor.besitzer:
        c = c + 1
    if v.besitzer == hab.besitzer:
        c = c + 1
    if c == 1:
        return 500
    elif c == 2:
        return 1000
    elif c == 3:
        return 2000
    elif c == 4:
        return 4000
"""

def eingabe():
    while True:
        kaufen = str(input("Ja/Nein: "))
        try:
            kaufen = "Ja" or "Nein"
        except ValueError:
            print("Bitte geben Sie nur Ja oder Nein ein")
        else:
            return kaufen

def aktion(x):
    if x.position == 0:
        print(x.name + ": Sie sind auf Los gekommen")
        x.konto = x.konto + 4000;
        print("Ihr neuer Kontostand ist: " + str(x.konto) + "€")
    elif x.position == 1:
        print(x.name + ": Sie sind auf der Badstraße gelandet.")
        kaufprüfung(bad, x)
    elif x.position == 3:
        print(x.name + ": Sie sind auf der Turmstraße gelandet.")
        kaufprüfung(turm, x)
    elif x.position == 4:
        print(x.name + ": Sie sind auf dem Feld Einkommenssteuer gelandet.")
        if x.konto < 4000:
            print("Sie sind pleite!")
        else:
            x.konto = x.konto - 4000
    elif x.position == 5:
        print(x.name + ": Sie sind auf dem Südbahnhof gelandet.")
        kaufprüfung(süd, x)
    elif x.position == 6:
        print(x.name + ": Sie sind auf der Chausseestraße.")
        kaufprüfung(cha, x)
    elif x.position == 8:
        print(x.name + ": Sie sind auf der Elisenstraße.")
        kaufprüfung(eli, x)
    elif x.position == 9:
        print(x.name + ": Sie sind auf der Poststraße.")
        kaufprüfung(pos, x)
    elif x.position == 10:
        if x.gefängnis == True:
            print("s")
        else:
            print(x.name + ": Sie sind zu Besuch im Gefängnis.")
    elif x.position == 11:
        print(x.name + ": Sie sind auf der Seestraße.")
        kaufprüfung(see, x)
    elif x.position == 12:
        print(x.name + ": Sie sind auf dem Elektrizitätswerk.")
        kaufprüfung(ele, x)
    elif x.position == 13:
        print(x.name + ": Sie sind auf der Hafenstraße.")
        kaufprüfung(haf, x)
    elif x.position == 14:
        print(x.name + ": Sie sind auf der Neuen Straße.")
        kaufprüfung(neu, x)
    elif x.position == 15:
        print(x.name + ": Sie sind auf dem Westbahnhof.")
        kaufprüfung(wes, x)
    elif x.position == 16:
        print(x.name + ": Sie sind auf der Münchener Straße.")
        kaufprüfung(mün, x)
    elif x.position == 18:
        print(x.name + ": Sie sind auf der Wiener Straße.")
        kaufprüfung(wie, x)
    elif x.position == 19:
        print(x.name + ": Sie sind auf der Berliner Straße.")
        kaufprüfung(ber, x)
    elif x.position == 20:
        print(x.name + ": Sie sind auf Frei Parken.")
    elif x.position == 21:
        print(x.name + ": Sie sind auf der Theaterstraße.")
        kaufprüfung(the, x)
    elif x.position == 23:
        print(x.name + ": Sie sind auf der Museumstraße.")
        kaufprüfung(mus, x)
    elif x.position == 24:
        print(x.name + ": Sie sind auf dem Opernplatz.")
        kaufprüfung(ope, x)
    elif x.position == 25:
        print(x.name + ": Sie sind auf dem Nordbahnhof.")
        kaufprüfung(nor, x)
    elif x.position == 26:
        print(x.name + ": Sie sind auf der Lessingstraße.")
        kaufprüfung(les, x)
    elif x.position == 27:
        print(x.name + ": Sie sind auf der Schillerstraße.")
        kaufprüfung(sch, x)
    elif x.position == 28:
        print(x.name + ": Sie sind auf dem Wasser Werk.")
        kaufprüfung(was, x)
    elif x.position == 29:
        print(x.name + ": Sie sind auf der Goethestraße.")
        kaufprüfung(got, x)
    elif x.position == 30:
        print(x.name + ": Sie müssen sich sofort ins Gefängnis begeben.")
    elif x.position == 31:
        print(x.name + ": Sie sind auf dem Rathausplatz.")
        kaufprüfung(rat, x)
    elif x.position == 32:
        print(x.name + ": Sie sind auf der Hauptstraße.")
        kaufprüfung(hau, x)
    elif x.position == 34:
        print(x.name + ": Sie sind auf der Bahnhofstraße.")
        kaufprüfung(bah, x)
    elif x.position == 35:
        print(x.name + ": Sie sind auf dem Hauptbahnhof.")
        kaufprüfung(hab, x)
    elif x.position == 37:
        print(x.name + ": Sie sind auf der Parkstraße.")
        kaufprüfung(par, x)
    elif x.position == 38:
        print(x.name + ": Sie sind auf dem Feld Zusatzsteuer gelandet.")
        print("Sie müssen 2000€ Zusatzsteuer zahlen")
        if x.konto < 2000:
            print("Sie sind pleite!")
        else:
            x.konto = x.konto - 2000
    elif x.position == 39:
        print(x.name + ": Sie sind auf der Schlossallee.")
        kaufprüfung(schl, x)
    elif x.position == 2 or x.position == 17 or x.position == 33:
        print(x.name + ": Sie sind auf einem Gemeinschaftsfeld gelandet.")
        gemeinschaft(x)
    elif x.position == 8 or x.position == 22 or x.position == 36:
        print(x.name + ": Sie sind auf einem Ereignisfeld gelandet.")
        ereignis(x)


#def weiter(g):
#    if an > g:
 #       g = g + 1
 #   else:
  #      g = 1
   # return k

def ausgabe(x):
    print(x.name + ":")
    print("Kontostand:           " + str(x.konto))
    print("Straßen:              ")

class Spielfeld():
    name = {};
    nummer = None;
    verkauft = False;
    kaufpreis = int;
    miete = int;
    haus0 = None;
    haus1 = None;
    haus2 = None;
    haus3 = None;
    haus4 = None;
    haus5 = None;
    anzahlhaus = None;
    kostenhaus = None;
    bahnhof = None;
    besitzer = None;

class Spieler():
    name = {};
    position = None;
    konto = int;
    haus = int;
    hotel = int;
    freikarte = None;
    gefängnis = False;

#Klassifizierung fü die Spieler
sp1 = Spieler()
sp2 = Spieler()
sp3 = Spieler()
sp4 = Spieler()

sp1.konto = 20000;
sp1.position = 0;
sp1.haus = 0;
sp1.hotel = 0;

sp2.konto = 20000;
sp2.position = 0;
sp2.haus = 0;
sp2.hotel = 0;

sp3.konto = 20000;
sp3.position = 0;
sp3.haus = 0;
sp3.hotel = 0;

sp4.konto = 20000;
sp4.position = 0;
sp4.haus = 0;
sp4.hotel = 0;

#Klassifizierung für die Spielfelder
bad = Spielfeld()
bad.name = "Badstraße"
bad.nummer = 1
bad.kaufpreis = 1200
bad.verkauft = False
bad.haus0 = 40
bad.haus1 = 200
bad.haus2 = 600
bad.haus3 = 1800
bad.haus4 = 3200
bad.haus5 = 5000
bad.kostenhaus =1000 

turm = Spielfeld()
turm.name = "Turmstraße"
turm.nummer = 3
turm.kaufpreis = 1200
turm.verkauft = False
turm.haus0 = 80
turm.haus1 = 400
turm.haus2 = 1200
turm.haus3 = 3600
turm.haus4 = 6400
turm.haus5 = 9000
turm.kostenhaus = 1000

süd = Spielfeld()
süd.name = "Südbahnhof"
süd.nummer = 5
süd.kaufpreis = 4000
süd.verkauft = False
süd.bahnhof = True 
süd.miete = 1000
süd.besitzer = None;

cha = Spielfeld()
cha.name = "Chausseestraße"
cha.nummer = 6
cha.kaufpreis = 2000
cha.verkauft = False
cha.haus0 = 120
cha.haus1 = 600
cha.haus2 = 1800
cha.haus3 = 5400
cha.haus4 = 8000
cha.haus5 = 11000
cha.kostenhaus = 1000

eli = Spielfeld()
eli.name = "Elisenstraße"
eli.nummer = 8
eli.kaufpreis = 2000
eli.haus0 = 120
eli.haus1 = 600
eli.haus2 = 1800
eli.haus3 = 5400
eli.haus4 = 8000
eli.haus5 = 11000
eli.kostenhaus = 1000

pos = Spielfeld()
pos.name = "Poststraße"
pos.nummer = 9
pos.kaufpreis = 2400
pos.haus0 = 160
pos.haus1 = 800
pos.haus2 = 2000
pos.haus3 = 6000
pos.haus4 = 9000
pos.haus5 = 12000
pos.kostenhaus = 1000

see = Spielfeld()
see.name = "Seestraße"
see.nummer = 11
see.kaufpreis = 2800
see.haus0 = 200
see.haus1 = 1000
see.haus2 = 3000
see.haus3 = 9000
see.haus4 = 12500
see.haus5 = 15000
see.kostenhaus = 2000

ele = Spielfeld()
ele.name = "Elektrizitätswerk"
ele.nummer = 12
ele.kaufpreis = 3000
#ele.miete = werk()

haf = Spielfeld()
haf.name = "Hafenstraße"
haf.nummer = 13
haf.kaufpreis = 2800
haf.haus0 = 200
haf.haus1 = 1000
haf.haus2 = 3000
haf.haus3 = 9000
haf.haus4 = 12500
haf.haus5 = 15000
haf.kostenhaus = 2000

neu = Spielfeld()
neu.name = " Neue Straße"
neu.nummer = 14
neu.kaufpreis = 3200
neu.haus0 = 240
neu.haus1 = 1200
neu.haus2 = 3600
neu.haus3 = 10000
neu.haus4 = 14000
neu.haus5 = 18000
neu.kostenhaus = 2000

wes = Spielfeld()
wes.name = "Westbahnhof"
wes.nummer = 15
wes.kaufpreis = 4000
wes.miete = 1000
wes.besitzer = None;

mün = Spielfeld()
mün.name = "Münchener Straße"
mün.nummer = 16
mün.kaufpreis = 3600
mün.haus0 = 280
mün.haus1 = 1400
mün.haus2 = 4000
mün.haus3 = 11000
mün.haus4 = 15000
mün.haus5 = 19000
mün.kostenhaus = 2000

wie = Spielfeld()
wie.name = "Wiener Straße"
wie.nummer = 18
wie.kaufpreis = 3600
wie.haus0 = 280
wie.haus1 = 1400
wie.haus2 = 4000
wie.haus3 = 11000
wie.haus4 = 15000
wie.haus5 = 19000
wie.kostenhaus = 2000

ber = Spielfeld()
ber.name = "Berliner Straße"
ber.nummer = 19
ber.kaufpreis = 4000
ber.haus0 = 320
ber.haus1 = 1600
ber.haus2 = 4400
ber.haus3 = 12000
ber.haus4 = 16000
ber.haus5 = 20000
ber.kostenhaus = 2000

fre = Spielfeld()
fre.name = "Frei Parken"
fre.nummer = 20

the = Spielfeld()
the.name = "Theaterstraße"
the.nummer = 21
the.kaufpreis = 4400
the.haus0 = 360
the.haus1 = 1800
the.haus2 = 5000
the.haus3 = 14000
the.haus4 = 17500
the.haus5 = 21000
the.kostenhaus = 3000

mus = Spielfeld()
mus.name = "Museumsstraße"
mus.nummer = 23
mus.kaufpreis = 4400
mus.haus0 = 360
mus.haus1 = 1800
mus.haus2 = 5000
mus.haus3 = 14000
mus.haus4 = 17500
mus.haus5 = 21000
mus.kostenhaus = 3000

ope = Spielfeld()
ope.name = "Opernplatz"
ope.nummer = 24
ope.kaufpreis = 4800
ope.haus0 = 400
ope.haus1 = 2000
ope.haus2 = 6000
ope.haus3 = 15000
ope.haus4 = 18500
ope.haus5 = 22000
ope.kostenhaus = 3000

nor = Spielfeld()
nor.name = "Nordbahnhof"
nor.nummer = 25
nor.kaufpreis = 4000
nor.bahnhof = True
nor.miete = 1000;
nor.besitzer = None;

les = Spielfeld()
les.name = "Lessingstraße"
les.nummer = 26
les.kaufpreis = 5200
les.haus0 = 440
les.haus1 = 2200
les.haus2 = 6600
les.haus3 = 16000
les.haus4 = 19500
les.haus5 = 23000
les.kostenhaus = 3000

sch = Spielfeld()
sch.name = "Schillerstraße"
sch.nummer = 27
sch.kaufpreis = 5200
sch.haus0 = 440
sch.haus1 = 220
sch.haus2 = 6600
sch.haus3 = 16000
sch.haus4 = 19500
sch.haus5 = 23000
sch.kostenhaus = 3000

was = Spielfeld()
was.name = "Wasserwerk"
was.nummer = 28
was.kaufpreis = 3000
#was.miete = werk()


got = Spielfeld()
got.name = "Goethestraße"
got.nummer = 29
got.kaufpreis = 5600
got.haus0 = 580
got.haus1 = 2400
got.haus2 = 7200
got.haus3 = 17000
got.haus4 = 20500
got.haus5 = 24000
got.kostenhaus = 3000

geh = Spielfeld()
geh.name = "Gehe in das Gefängnis"
geh.nummer = 30

rat = Spielfeld()
rat.name = "Rathausplatz"
rat.nummer = 31
rat.kaufpreis = 6000
rat.haus0 = 520
rat.haus1 = 2600
rat.haus2 = 7800
rat.haus3 = 18000
rat.haus4 = 22000
rat.haus5 = 25500
rat.kostenhaus = 4000

hau = Spielfeld()
hau.name = "Hauptstraße"
hau.nummer = 32
hau.kaufpreis = 6000

bah = Spielfeld()
bah.name = "Bahnhofstraße"
bah.nummer = 34
bah.kaufpreis = 6400
bah.haus0 = 560
bah.haus1 = 3000
bah.haus2 = 9000
bah.haus3 = 20000
bah.haus4 = 24000
bah.haus5 = 28000
bah.kostenhaus = 4000

hab = Spielfeld()
hab.name = "Hauptbahnhof"
hab.nummer = 35
hab.kaufpreis = 4000
hab.bahnhof = True
hab.miete = 1000;
hab.besitzer = None;

par = Spielfeld()
par.name = "Parkstraße"
par.nummer = 37
par.kaufpreis = 7000
par.haus0 = 700
par.haus1 = 3500
par.haus2 = 1000
par.haus3 = 22000
par.haus4 = 26000
par.haus5 = 30000
par.kostenhaus = 4000

schl = Spielfeld()
schl.name = "Schlossallee"
schl.nummer = 39
schl.kaufpreis = 8000
schl.haus0 = 1000
schl.haus1 = 4000
schl.haus2 = 12000
schl.haus3 = 28000
schl.haus4 = 34000
schl.haus5 = 40000
schl.kostenhaus = 4000

gem = Spielfeld()
gem.name = "Gemeinschaftsfeld"
gem.nummer = 2, 17, 33

ere = Spielfeld()
ere.name = "Ereignisfeld"
ere.nummer = 7, 22, 36


x = 0
if x == 0:
    an = start()
    if an != 4 and an != 3 and an != 2:
        print("Die Anzahl der Spieler ist ungültig!")
        print("Bitte starten Sie das Spiel erneut.")
    sp1.name = str(input("Name des ersten Spielers: "))
    sp2.name = str(input("Name des zweiten Spielers: "))
    if an != 2:
        sp3.name = str(input("Name des dritten Spielers: "))
    elif an != 3 and an != 2:
        sp4.name = str(input("Name des vierten Spielers: "))
    x = 1

initia()

def spiel(c):
    ausgabe(c)
    rolldice()
    wurfausgabe()
    neueposition(c)
    aktion(c)
    print(c.position)
    time.sleep(2)


def spil(c):
    if pasch == True:
        spiel(c)
        print(c.position)
        time.sleep(2)
    if pasch == True:
        ausgabe(c)
        rolldice()
        wurfausgabe()
        time.sleep(2)
        if pasch == True:
            print("Sie müssen ins Gefängnis gehen!!!!!!")
            c.gefängnis = True;
        else:
            neueposition(c)
            aktion(c)
            print(c.position)
            time.sleep(2)

def beak():
    print("--------------------------------------")

k = 1
while x == 1:
    if k == 1:
        spiel(sp1)
        spil(sp1)
        k = 2
        beak()
    elif k == 2:
        spiel(sp2)
        spil(sp2)
        if an == 2:
            k = 1
        else:
            k = 3
        beak()
    elif k == 3:
        spiel(sp3)
        spil(sp3)
        if an == 3:
            k = 1
        else:
            k = 4
        beak()
    elif k == 4:
        spiel(sp4)
        spil(sp4)
        k = 1
        beak()
