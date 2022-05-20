# Valbarometer
Mitt slutprojekt i Programmering 1. Här gör jag en valbarometer. 

Alexander Rehnman
•
13:00

NL_README.md
Text
Klasskommentarer


## Beskrivning

Mitt program är en valbarometer som är skrivet i programmeringsspråket Python. Programmet har i uppgift att med hjälp av filhantering och klasser att välja ut ett av tre olika "partier" som du mest hör samman med.

## Byggt med

- Python

## Krav

- Python 3.9+

## Installation

Detta projekt är testat på Python 3.9+. För att installera Python kan du besöka (https://www.python.org/downloads/)[följande länk för senaste versionen.]

## exempelkörning + hur den fungerar.


Exempel på koden:
        n = 0
        tie = False
        global winningParty 
        for i in range(len(points)-1) :
            if points[i+1] > points[i]:
                n = i +1
                tie == False
            if points[i+1] == points[i] and points[n] <= points[i]:
                tie = True

Här går jag de olika partierna och gämför vardera parti med varandra. Ifall ett parti har mer poäng än det två andra patrierna så är det vinnaren och skrivs ut.

<img src ="./img/bild1.jpg">
<img src ="./img/bild2.jpg">


## Att göra/Plan

- [x] Påbörja exempelreadme
- [ ] Hitta fler exempelrubriker
- [ ] Kom på bättre exempel
- [ ] Ge exempel på projekt med fullständig readme
- [ ] Ytterligare språk
    - [x] Svenska
    - [x] Engelska

## Changelog

Inget har ändrats.

### Version 1.0.1

#### Tillagt eller ändrat

- La till avsnitt om changelog
- La till avsnitt om kodkonventioner

#### Borttaget

- Tog bort tidigare kommentarer som inte passade in.

## Att bidra 

Då bedömning ännu ej är gjord på uppgiften så tillåts inga pull requests. Så fort bedömning är gjord kommer detta tillåtas.  

Vid större förändringar önskar jag att en issue öppnas för diskussion om vad som ska förändras.

## Licens

[MIT](https://choosealicense.com/licenses/mit/)

## Kontakt

Kan bli kontaktad på följande plattformar:

- Snapchat: Alexander2004r2
- Instagram:@Alexanderrehnman
- Gmail:Alexanderrehnman2004@gmail.com

Projektlänk: https://github.com/ditt_anv/reponamn

## Erkännanden

- Niclas Lund
- https://www.w3schools.com/

