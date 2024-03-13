# minus muss noch rein
#prüfen, ob man sachen überhaupt kaufen kann

Bank_Account = 0
Item = "Item"
Item_Value = 1000

try:

    def doMath(Bank_Account, Item_Value):

        answer1 = str(input(f"Möchten Sie das folgende Item verkaufen oder kaufen? Geben Sie k/K ein, um das Item zu kaufen. Geben Sie v/V ein, um das Item zu verkaufen.\n"))
        if answer1 == "K":
            Item_Value = 1000 * -1
            answer2 = str(input(f"Glückwunsch, {Item} wurde gekauft! das Geld wird ihrem Kontostand nun abgezogen. Fortfahren?\n"))
            if answer2 == "Ja":
                Bank_Account = Bank_Account + Item_Value
                if Bank_Account < 0:
                    print(f"{Item} konnte nicht gekauft werden, sie besitzen nicht genügend Geld auf ihrem Kontostand.")
                else:
                    print(f"Kontostand: {Bank_Account}")
        elif answer1 == "k":
            Item_Value = 1000 * -1
            answer2 = str(input(f"Glückwunsch, {Item} wurde gekauft! das Geld wird ihrem Kontostand nun abgezogen. Fortfahren?\n"))
            if answer2 == "ja":
                Bank_Account = Bank_Account + Item_Value
                if Bank_Account < 0:
                    print(f"{Item} konnte nicht gekauft werden, sie besitzen nicht genügend Geld auf ihrem Kontostand.")
                else:
                    print(f"Kontostand: {Bank_Account}")
            elif answer2 == "Nein":
                print("Der Vorgang wurde abgebrochen.")
            elif answer2 == "nein":
                print("Der Vorgang wurde abgebrochen.")
        

        elif answer1 == "v":
            Item_Value = 1000
            answer = str(input(f"Glückwunsch, {Item} wurde verkauft! das Geld wird ihrem Kontostand nun hinzugefügt. Fortfahren?\n"))
            if answer == "Ja":
                Bank_Account = Bank_Account + Item_Value
                print(f"Kontostand: {Bank_Account}")
            elif answer == "ja":
                Bank_Account = Bank_Account + Item_Value
                print(f"Kontostand: {Bank_Account}")
            elif answer == "Nein":
                print("Der Vorgang wurde abgebrochen.")
            elif answer == "nein":
                print("Der Vorgang wurde abgebrochen.")

        elif answer1 == "V":
            Item_Value = 1000
            answer = str(input(f"Glückwunsch, {Item} wurde verkauft! das Geld wird ihrem Kontostand nun hinzugefügt. Fortfahren?\n"))
            if answer == "Ja":
                Bank_Account = Bank_Account + Item_Value
                print(f"Kontostand: {Bank_Account}")
            elif answer == "ja":
                Bank_Account = Bank_Account + Item_Value
                print(f"Kontostand: {Bank_Account}")
            elif answer == "Nein":
                print("Der Vorgang wurde abgebrochen.")
            elif answer == "nein":
                print("Der Vorgang wurde abgebrochen.")

except ValueError:
    print("Bitte geben sie entweder Ja/ja oder Nein/nein ein.\n")

doMath(Bank_Account, Item_Value)