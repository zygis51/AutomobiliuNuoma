# Kursinio darbo ataskaita

## 1. Įvadas

### a. Kas yra jūsų programa?

Programa yra transporto priemonių nuomos sistema, kurioje vartotojai gali peržiūrėti galimas nuomoti transporto priemones ir jas išsinuomoti. Sistema palaiko dvi transporto priemonių rūšis: automobilius ir mikroautobusus. Ji suteikia funkcijas klientams nuomoti ir grąžinti transporto priemones, o administratoriui – sekti nuomos veiklą.

### b. Kaip paleisti programą?

Norėdami paleisti programą, atsisiųskite šį saugyklą į savo kompiuterį. Galite paleisti failą `main.py`, kad pradėtumėte naudoti sistemą. Įsitikinkite, kad jūsų kompiuteryje įdiegta Python 3.x versija.

```
git clone <repository_link>
cd <directory>
python main.py
```

### c. Kaip naudotis programa?

Programa turi meniu sąsają:
1. Peržiūrėti visas transporto priemones  
2. Peržiūrėti laisvas transporto priemones
3. Išnuomoti transporto priemonę
4. Peržiūrėti klientų nuomas
5. Išsaugoti duomenis ir išeiti

Norėdami pereiti tarp meniu pasirinkimų, naudokite skaitmeninius įvedimus.

## 2. Pagrindinė analizė


#### **1. Polimorfizmas**

Polimorfizmas yra naudojamas `gauti_tipą` metoduose, kuriuos realizuoja kiekviena transporto priemonė. Kiekviena klasė (`Automobilis`, `Mikroautobusas`) turi savo versiją šio metodo, kuris grąžina transporto priemonės tipą.

```python
# Automobilis.py
class Automobilis(TransportoPriemone):
    def gauti_tipą(self):
        return "automobilis"
```

Šiame pavyzdyje `Automobilis` klasė įgyvendina `gauti_tipą` metodą, kad grąžintų „automobilis“. Tai yra polimorfizmas, nes `gauti_tipą` metodas turi skirtingą įgyvendinimą priklausomai nuo objekto tipo.

#### **2. Abstrakcija**

Abstrakcija pasiekiama naudojant `TransportoPriemone` klasę, kuri yra abstrakti ir nustato bendrą sąsają (metodą `gauti_tipą`) visoms transporto priemonėms. Ši klasė slepia detales apie konkrečias transporto priemones ir leidžia joms bendrą sąsają.

```python
# TransportoPriemone.py
class TransportoPriemone(ABC):
    @abstractmethod
    def gauti_tipą(self):
        pass
```

Ši klasė užtikrina, kad visi `TransportoPriemone` klasės paveldėtojai turi įgyvendinti `gauti_tipą` metodą, bet konkretūs įgyvendinimai priklauso nuo transporto priemonės tipo (pvz., automobilio ar mikroautobuso).

#### **3. Paveldėjimas**

Paveldėjimas naudojamas `Automobilis` ir `Mikroautobusas` klasėse, kurios paveldi funkcionalumą iš `TransportoPriemone` klasės. Kiekviena iš šių klasių papildomai prideda savo unikalius duomenis (pvz., durų skaičius ar vietų skaičius).

```python
# Automobilis.py
class Automobilis(TransportoPriemone):
    def __init__(self, marke, modelis, metai, kaina, prieinamumas="laisva", duru_sk=5):
        super().__init__(marke, modelis, metai, kaina, prieinamumas)
        self.duru_sk = duru_sk
```

Šiame pavyzdyje `Automobilis` klasė paveldi visus `TransportoPriemone` klasės metodus ir atributus, tačiau taip pat prideda savo savybę (`duru_sk`), kuri yra specifinė tik automobiliui.

#### **4. Kapsuliavimas**

Kapsuliavimas pasiekiamas užtikrinant, kad duomenys apie transporto priemones ir nuomos informaciją būtų pasiekiami tik per metodus. Pavyzdžiui, `Klientas` ir `Nuoma` klasėse duomenys saugomi kaip atributai ir nėra tiesiogiai prieinami iš išorės.

```python
# Klientas.py
class Klientas:
    def __init__(self, vardas, pavarde):
        self.vardas = vardas
        self.pavarde = pavarde

    def __str__(self):
        return f"{self.vardas} {self.pavarde}"
```

Čia `Klientas` klasėje duomenys apie vardą ir pavardę yra kapsuliuojami. Prie šių duomenų galima prieiti tik naudojant metodus (pvz., `__str__`).

#### **5. Singleton dizaino šablonas**

Singleton dizaino šablonas naudojamas `DuomenuValdymas` klasėje, kad būtų užtikrinta, jog visa programoje naudojama duomenų valdymo logika remiasi tik viena instancija.

```python
# DuomenuValdymas.py
class DuomenuValdymas:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DuomenuValdymas, cls).__new__(cls)
        return cls._instance
```

Ši klasė garantuoja, kad visos programos dalys naudoja tą pačią `DuomenuValdymas` instanciją, taip užtikrinant duomenų nuoseklumą.


#`TransportoPriemonesFactory` klasė taiko **Factory dizaino šabloną**, kuris leidžia sukurti skirtingų tipų transporto priemones, remiantis pateiktu `tipas` parametru. Tai veikia šiame kode, nes `Factory` centralizuoja transporto priemonių kūrimą, taip užtikrindama, kad nesvarbu, ar kuriame automobilį, ar mikroautobusą, mes naudojame tą pačią sąsają ir logiką, tačiau skirtingi tipai sukuriami pagal jų specifiką. Tai leidžia lengvai pridėti naujus transporto priemonių tipus, nes reikia tik papildyti sąlygą...

```python
class TransportoPriemonesFactory:
    @staticmethod
    def sukurti_priemone(tipas, marke, modelis, metai, kaina, prieinamumas="laisva", **kwargs):
        if tipas == "automobilis":
            from Automobilis import Automobilis
            return Automobilis(marke, modelis, metai, kaina, prieinamumas, kwargs.get('duru_sk', 5))
        elif tipas == "mikroautobusas":
            from Mikroautobusas import Mikroautobusas
            return Mikroautobusas(marke, modelis, metai, kaina, prieinamumas, kwargs.get('vietu_sk', 8))
        else:
            raise ValueError(f"Nežinomas transporto priemonės tipas: {tipas}")
```
#### **6. Kompozicija ir agregacija**

Kompozicija naudojama `Nuoma` klasėje, kur transporto priemonė ir klientas yra objekto dalys, ir be šių elementų nuoma neegzistuotų.

```python
# Nuoma.py
class Nuoma:
    def __init__(self, klientas, transporto_priemone, kaina):
        self.klientas = klientas
        self.transporto_priemone = transporto_priemone
        self.kaina = kaina
```

Čia `Nuoma` klasė sudaro kompoziciją su `Klientas` ir `TransportoPriemone` objektais, nes nuomos operacija negalėtų vykti be šių elementų.

## 3. Rezultatai ir santrauka

### a. „Rezultatų“ funkciniai reikalavimai

Programa sėkmingai leidžia vartotojams peržiūrėti galimas transporto priemones, jas nuomoti ir grąžinti. Visi funkcionalumai veikia kaip tikėtasi, be rimtų klaidų.

### b. „Išvadas“ funkciniai reikalavimai

Sistema suteikia funkcionalią ir patogią vartotojo sąsają transporto priemonių nuomai. Ji atitinka objektinio programavimo principus, įskaitant kapsuliavimą, abstrakciją, paveldėjimą ir polimorfizmą.

### c. Kaip būtų galima išplėsti jūsų programą?

Sistema galėtų būti išplėsta pridedant daugiau transporto priemonių tipų (pvz., motociklus, dviračius) ir įgyvendinant pažangias užsakymų funkcijas, tokias kaip datos pasirinkimas, kelių dienų nuomos galimybė ir apmokėjimo apdorojimas.

