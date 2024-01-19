import csv

def lasit_otro_kolonnu(csv_fails):
    try:
        with open(csv_fails, 'r', newline='', encoding='utf-8') as f:
            b = csv.reader(f)
            print("Otrā kolonna: ")
            for rinda in b:
                if len(rinda) > 1:
                    print(rinda[1])
    except FileNotFoundError:
        print(f"Nevar atrast {csv_fails} failu.")
    except Exception as e:
        print(f"Kļūda: {e}")

a = 'faila nosaukums.csv'
lasit_otro_kolonnu(a)
