def lasit_treso_rindu(fails):
    try:
        with open(fails, 'r', encoding='utf-8') as f:
            rindas = f.readlines()
            if len(rindas) >= 3:
                tresa_rinda = rindas[2].strip()
                print("Teksts, kas atrodas trešajā rindā ir:")
                print(tresa_rinda)
            else:
                print(f"Nevarēja idrukāt {fails} failā nav pietikemas rindu skaits")
    except FileNotFoundError:
        print(f" Nevarēja atrast {fails} failu")
    except Exception as e:
        print(f"Kļūda failā{e}")

c = 'piemers.txt'
lasit_treso_rindu(c)
