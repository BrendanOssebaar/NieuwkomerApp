from time import sleep
while True:
    print("De tweede wereld oorlog begint wanneer Adolf Hitler en zijn wehrmacht Tjecho-slowakije en Polen binnen valt in 1939")
    sleep(5)
    print("In 1940 vallen de duitsers Nederland binnen en na een wanhopige weerstand van de nederlanders hebben ze Nederland overgenomen")
    sleep(5)
    print("Jij bent een volwassen man wonend in Amsterdam")
    sleep(5)
    print("Je hebt 4 keuzes:")
    print("A: Je duikt onder")
    print("B: Je vecht terug bij met de verzetstrijders")
    print("C: Je vlucht naar het buitenland")
    print("D: Je gaat werken bij de SS")
    print("E: Je gaat werken in een werkkamp in Duitsland")
    print("Wat ga je doen?")
    k1 = input().capitalize()
    if k1 == "A":
        print("Je besluit onder te duiken")
        sleep(5)
        print("Bij wie ga je onderduiken?")
        sleep(5)
        print("A: Je familie")
        print("B: Je vrienden")
        k1a = input().capitalize()
        if k1a == "A":
            print("Je duikt onder bij je oma en opa")
            sleep(4)
            print("Je brengt veel tijd door op zolder")
            sleep(4)
            print("Alleen voor eten kom je naar beneden")
            sleep(4)
            print("Wat ga je doen?")
            sleep(3)
            print("A: Je blijft tot het einde van de oorlog")
            print("B: Je kiest ervoor om toch een beetje terug te vechten, door middel van 'snachts flyers op te hangen")
            print("C: Je verplaatst naar een ander deel van Nederland, want het wordt hier te druk qua Duitsers")
            k1aa = input().capitalize()
            if k1aa == "A":
                print("Je blijft tot het einde van de oorlog veilig bij je grootouders")
                print("Goed einde")
                break
            elif k1aa == "B":
                print("Je plakt 'savonds flyers op de muren om mensen aan te moedigen terug te vechten")
                sleep(4)
                print("Je word een avond betrapt en word naar duitsland gestuurd om te werken in een werkkamp tot het einde van de oorlog")
                print("Neutraal einde, opnieuw proberen? Y/N")
                k1aab = input().capitalize()
                if k1aab == "N":
                    break
            elif k1aa == "C":
                print("")
        elif k1a == "B":
            print("Je duikt onder bij vrienden in hartje Amsterdam")
            sleep(3)
            print("")
    elif k1 == "B":
        print("")
    elif k1 == "C":
        print("")
    elif k1 == "D":
        print("Je verraad je land en werkt voor de SS tot het einde van de oorlog")
        sleep(5)
        print("Na de oorlog ben je je Nederlandse nationaliteit kwijt")
        sleep(5)
        print("Slecht einde, opnieuw proberen? Y/N")
        k1d = input().capitalize()
        if k1d == "N":
            break
    elif k1 =="E":
        print("Je gaat met een trein naar Duitsland en gaat aan het werk in een werkkamp")
        sleep(3)
        print("Het zijn brute jaren, maar je werkt door")
        sleep(3)
        print("Aan het einde van de oorlog word je bevrijd en keert terug naar Nederland")
        sleep(3)
        print("Je hebt de oorlog overleeft")
        sleep(3)
        print("Neutraal einde")
        sleep(3)
        break