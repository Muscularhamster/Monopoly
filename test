class Konto:

    def __init__(self, startguthaben):
        self.guthaben = startguthaben

    def abheben(self, betrag):
        if betrag > self.guthaben:
            raise ValueError("Es ist nicht genug Geld auf dem Konto")
        self.guthaben -= betrag

    def einzahlen(self, betrag):
        self.guthaben += betrag


konto = Konto(100)
konto.abheben(50)
print(konto.guthaben)
# 50

konto.einzahlen(20)
print(konto.guthaben)
# 70
