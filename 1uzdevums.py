def lasit_drukat(fails):
    try:
        with open(fails, 'r', encoding='utf-8') as f:
            saturs = f.read()
            print("Failā atrodas:")
            print(saturs)
    except FileNotFoundError:
        print(f"Nevarēja atrast '{fails}' failu.")
    except Exception as e:
        print(f"Kļūda: {e}")

b = 'faila nosaukums.txt'
lasit_drukat(b)
