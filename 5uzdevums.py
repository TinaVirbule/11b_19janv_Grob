try:
    vards = input("Ievadiet savu vārdu: ")
    
    faila_nosaukums = "ista faila nosakuma.txt"

    with open(faila_nosaukums, "w") as fails:
        fails.write(vards)
    print(f"Izdevās ierakstīt vārdu failā {faila_nosaukums}.")

except IOError as nesanaca:
    print(f"Nesanāca, kaut kas nogāja greizi {nesanaca}")
except Exception as a:
    print(f"Atkal nesanāca {a}")
 