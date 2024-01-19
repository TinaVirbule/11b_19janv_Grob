def lasit_failu(faila_nosaukums):
    try:
        with open(faila_nosaukums, 'r') as fails:
            a = fails.read()
        return a
    except FileNotFoundError:
        print(f"Nevarēja atrast failu ar nosaukumu: {faila_nosaukums}.")
    except Exception as e:
        print(f"Nesanāca {e}")
    return None

def main():
    try:
        faila_nosaukums = input("Faila nosaukums: ")
        b = input("Faila formāts: ")

        c = f"{faila_nosaukums}{b}"
        saturs = lasit_failu(c)

        if saturs is not None:
            print(f"Faila {c} saturs:")
            print(saturs)
    except Exception as e:
        print(f"Nu nesanāca {e}")

if __name__ == "__main__":
    main()
