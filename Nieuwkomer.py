from time import sleep
while True:
    print("De tweede wereld oorlog begint wanneer Adolf Hitler en zijn wehrmacht Tjecho-slowakije en Polen binnen valt in 1939")
    sleep(5)
    print("In 1940 vallen de duitsers Nederland binnen en na een wanhopige weerstand van de nederlanders hebben ze Nederland overgenomen")
    sleep(5)
    print("Jij bent een volwassen man wonend in Amsterdam")
    sleep(5)
    print("Je hebt 5 keuzes:")
    print("A: Je duikt onder")
    print("B: Je vecht terug met de verzetstrijders")
    print("C: Je vlucht naar het buitenland")
    print("D: Je gaat werken bij de SS")
    print("E: Je gaat werken in een werkkamp in Duitsland")
    print("Wat ga je doen?")
    k1 = input().capitalize()
    if k1 == "A":
        print("Je besluit onder te duiken")
        sleep(2)
        print("Bij wie ga je onderduiken?")
        sleep(2)
        print("A: Je familie")
        print("B: Je vrienden")
        k1a = input().capitalize()
        if k1a == "A":
            print("Je duikt onder bij je oma en opa")
            sleep(2)
            print("Je brengt veel tijd door op zolder")
            sleep(2)
            print("Alleen voor eten kom je naar beneden")
            sleep(2)
            print("Wat ga je doen?")
            print("A: Je blijft tot het einde van de oorlog")
            print("B: Je kiest ervoor om toch een beetje terug te vechten, door middel van 's nachts flyers op te hangen")
            print("C: Je vlucht naar het buitenland, want het wordt hier te druk qua Duitsers")
            k1aa = input().capitalize()
            if k1aa == "A":
                print("Je blijft tot het einde van de oorlog veilig bij je grootouders")
                print("Goed einde")
                break
            elif k1aa == "B":
                print("Je plakt 's avonds flyers op de muren om mensen aan te moedigen terug te vechten")
                sleep(4)
                print("Je word een avond betrapt en word naar duitsland gestuurd om te werken in een werkkamp tot het einde van de oorlog")
                print("Neutraal einde, opnieuw proberen? Y/N")
                k1aab = input().capitalize()
                if k1aab == "N":
                    break
            elif k1aa == "C":
                print("Je probeert te vluchten")
                sleep(3)
                print("Je wordt verraden en opgepakt.")
                sleep(4)
                print("Je wordt naar een werkkamp in Duitsland gestuurd en werkt daar tot het einde van de oorlog")
                sleep(4)
                print("Neutraal einde")
                break
        elif k1a == "B":
            print("Je duikt onder bij vrienden in hartje Amsterdam")
            sleep(3)
            print("Jij en je vrienden blijven uit het zicht door overdag op zolder te blijven. De vrouwen doen het meeste huishoudwerk")
            sleep(4)
            print("'S avonds kun je naar beneden komen om te eten en stiekem naar buiten te gaan")
            sleep(4)
            print("Wat ga je doen?")
            print("A: Blijven tot einde van de oorlog")
            print("B: Je kiest ervoor om toch een beetje terug te vechten, door middel van 's nachts flyers op te hangen")
            print("C: Je vlucht naar het buitenland, want het wordt hier te druk qua Duitsers")
            k1ab = input().capitalize()
            if k1ab == "A":
                print("Je blijft ondergedoken bij je vrienden tot het einde van de oorlog")
                sleep(3)
                print("Goed einde")
                break
            elif k1ab == "B":
                print("Je plakt 's avonds flyers op de muren om mensen aan te moedigen terug te vechten")
                sleep(4)
                print("Je word een avond betrapt en word naar duitsland gestuurd om te werken in een werkkamp tot het einde van de oorlog")
                print("Neutraal einde, opnieuw proberen? Y/N")
                k1abb = input().capitalize()
                if k1abb == "N":
                    break
            elif k1ab == "C":
                print("Jij en je vrienden kiezen ervoor om te vluchten")
                sleep(3)
                print("Een van je vrienden heeft het voor elkaar gekregen om 's nachts met een boot naar Engeland te varen")
                sleep(4)
                print("Je komt 's nachts aan in londen")
                sleep(3)
                print("Je krijgt eten en onderdak")
                sleep(3)
                print("Je kunt in Londen blijven of verder Engeland in trekken")
                print("A: In Londen blijven")
                print("B: Verder Engeland in gaan")
                k1aba = input().capitalize()
                if k1aba == "A":
                    print("Je blijft in Londen")
                    sleep(3)
                    print("Elke week komen er bommenwerpers langs die de stad bombarderen")
                    sleep(4)
                    print("Een week wordt het gebouw waar jij en je vrienden in verblijven geraakt door een bom")
                    sleep(4)
                    print("Je overleeft de inslag niet")
                    print("Slecht einde. Opnieuw proberen? Y/N")
                    k1abb = input().capitalize()
                    if k1abb == "N":
                        break
                elif k1aba == "B":
                    print("Je gaat verder Engeland in")
                    sleep(2)
                    print("Je verblijft op het platteland tot het einde van de oorlog")
                    sleep(1)
                    print("Goed einde")
                    break
    elif k1 == "B":
        print("Je gaat terug vechten bij een verzetsstrijders")
        sleep(3)
        print("Je maakt deel uit van een groep strijders met een basis in westpoort")
        sleep(3)
        print("Er zijn meerdere teams die verschillende manieren van terugvechten uitvoeren")
        sleep(3)
        print("Er is een team voor sabotages en een team voor propaganda")
        sleep(3)
        print("Welk team steun je?")
        sleep(3)
        print("A: Sabotage Team")
        print("B: Propaganda Team")
        k1b = input().capitalize()
        if k1b == "A":
            print("Je gaat het sabotage team ondersteunen")
            sleep(3)
            print("Er zijn een aantal targets om te saboteren:")
            sleep(3)
            print("A: Een munitie depot")
            print("B: Een Duitse propaganda post")
            print("Welke ga je saboteren?")
            k1ba = input().capitalize()
            if k1ba == "A":
                print("Je besluit het munitie depot op te blazen")
                sleep(2)
                print("Jij en je teamgenoten hebben aantal explosieven weten te verkrijgen en 's nachts gaan jullie langs bij het depot om het op te blazen")
                sleep(6)
                print("Helaas hebben de Duitsers je team gesnapt en opgepakt")
                sleep(4)
                print("Je wordt door het Duitse gerechtshof beoordeelt en je wordt publiekelijk geëxecuteerd")
                sleep(5)
                print("Slecht einde. Opnieuw proberen? Y/N")
                k1baa = input().capitalize()
                if k1baa == "N":
                    break
            elif k1ba == "B":
                print("Je besluit een Duitse propaganda post op te blazen")
                sleep(3)
                print("Je blijf zo door gaan tot het einde van de oorlog")
                print("Goed einde")
                break
        elif k1b == "B":
            print("Je gaat het propaganda team ondersteunen")
            sleep(2)
            print("Jij en je team houden een geheime publieke radio bij en verspreiden flyers en posters door de stad")
            sleep(4)
            print("Je blijft zo doorgaan tot het einde van de oorlog")
            sleep(2)
            print("Goed einde")
            break
    elif k1 == "C":
        print("Je besluit te vluchten")
        sleep(3)
        print("Je vlucht naar:")
        print("A: Frankrijk")
        print("B: Engeland")
        print("C: Amerika")
        k1c = input().capitalize()
        if k1c == "A":
            print("Je besluit naar Frankrijk te vluchten")
            sleep(2)
            print("Hoe ga je dit doen?")
            print("A: Te voet")
            print("B: Met de auto")
            k1ca = input().capitalize()
            if k1ca == "A":
                print("Je gaat te voet naar Frankrijk")
                sleep(2)
                print("Doordat je te voet gaat kan je niet veel meenemen, maar je blijft wel goed uit het zicht van de Duitsers")
                sleep(5)
                print("Je komt aan bij de Belgische grens, geen Duitsers in zicht, dus doorlopen")
                sleep(3)
                print("Je komt aan bij de Franse grens, ook hier geen Duitsers. ")
                sleep(3)
                print("Je trekt je route door tot Zuid-Frankrijk")
                sleep(2)
                print("Je blijft daar tot het einde van de oorlog")
                print("Goed einde")
                break
            elif k1ca == "B":
                print("Je gaat met de auto richting Frankrijk")
                sleep(3)
                print("Je komt een heel eind, maar bij de grens wordt je gezien door Duitsers en aangehouden")
                sleep(4)
                print("Je wordt naar Duitsland gestuurd om te werken in een werkkamp")
                print("Neutraal einde, opnieuw proberen? Y/N")
                k1caa = input().capitalize()
                if k1caa == "N":
                    break
        elif k1c == "B":
            print("Je wil naar Engeland")
            sleep(2)
            print("Je probeert een boot te vinden om naar Engeland te vluchten")
            sleep(3)
            print("Iemand rapporteerd je bij de SS en je wordt opgepakt")
            sleep(3)
            print("Je wordt naar Duitsland gestuurd om te werken in een werkkamp tot het einde van de oorlog")
            sleep(4)
            print("Neutraal einde, opnieuw proberen? Y/N")
            k1cb = input().capitalize()
            if k1cb == "N":
                break
        elif k1c == "C":
            print("Je wil naar Amerika vluchten")
            sleep(2)
            print("Via wat vrienden krijg je het voor elkaar om met de boot naar Engeland te gaan en vanuit Engeland ga je met een vliegtuig naar Amerika")
            sleep(5)
            print("Goed einde")
            break
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
    else :
        print("Dat is geen keuze, probeer opnieuw")