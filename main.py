from TransportoPriemone import TransportoPriemone
from DuomenuValdymas import DuomenuValdymas
from Klientas import Klientas
from Nuoma import Nuoma

def rodyti_meniu():
    print("\n=== AUTOMOBILIŲ NUOMOS SISTEMA ===")
    print("1. Peržiūrėti visas transporto priemones")
    print("2. Peržiūrėti laisvas transporto priemones")
    print("3. Išnuomoti transporto priemonę")
    print("4. Peržiūrėti klientų nuomas")
    print("5. Išsaugoti duomenis ir išeiti")

def vykdyti_pasirinkima(pasirinkimas):
    duomenys = DuomenuValdymas()
    
    if pasirinkimas == '1':
        print("\nVisos transporto priemonės:")
        for idx, tp in enumerate(TransportoPriemone.gauti_visas(), 1):
            print(f"{idx}. {tp}")
    
    elif pasirinkimas == '2':
        print("\nLaisvos transporto priemonės:")
        for idx, tp in enumerate(TransportoPriemone.gauti_laisvas(), 1):
            print(f"{idx}. {tp}")
    
    elif pasirinkimas == '3':
        print("\n=== TRANSPORTO PRIEMONĖS NUOMA ===")
        vardas = input("Įveskite savo vardą: ").strip()
        pavarde = input("Įveskite savo pavardę: ").strip()
        
        if not vardas or not pavarde:
            print("Vardas ir pavardė negali būti tušti!")
            return
        
        klientas = Klientas(vardas, pavarde)
        duomenys.prideti_klienta(klientas)
        
        laisvos_priemones = TransportoPriemone.gauti_laisvas()
        if not laisvos_priemones:
            print("Šiuo metu nėra laisvų transporto priemonių.")
            return
        
        print("\nPasirinkite transporto priemonę:")
        for idx, tp in enumerate(laisvos_priemones, 1):
            print(f"{idx}. {tp}")
        
        try:
            pasirinkimas = int(input("Pasirinkite transporto priemonę (numerį): ")) - 1
            if pasirinkimas < 0 or pasirinkimas >= len(laisvos_priemones):
                print("Netinkamas pasirinkimas.")
                return
            
            pasirinkta_priemone = laisvos_priemones[pasirinkimas]
            print(f"\nJūs pasirinkote: {pasirinkta_priemone}")
            print(f"Nuomos kaina: {pasirinkta_priemone.kaina}€ per dieną")
            
            patvirtinimas = input("Ar norite tęsti nuomą? (taip/ne): ").lower()
            if patvirtinimas == 'taip':
                nuoma = Nuoma(klientas, pasirinkta_priemone, pasirinkta_priemone.kaina)
                klientas.prideti_nuoma(nuoma)
                pasirinkta_priemone.atnaujinti_prieinamumą("užimta")
                duomenys.issaugoti_nuoma(nuoma)
                print("\nSėkmingai išnuomota transporto priemonė!")
                print(nuoma)
            else:
                print("Nuoma atšaukta.")
        except ValueError:
            print("Įvestas netinkamas skaičius.")
    
    elif pasirinkimas == '4':
        print("\n=== KLIENTŲ NUOMOS ===")
        vardas = input("Įveskite kliento vardą: ").strip()
        pavarde = input("Įveskite kliento pavardę: ").strip()
        
        if not vardas or not pavarde:
            print("Vardas ir pavardė negali būti tušti!")
            return
        
        nuomos = duomenys.gauti_nuomas()
        kliento_nuomos = [n for n in nuomos 
                         if n['kliento_vardas'].lower() == vardas.lower() 
                         and n['kliento_pavarde'].lower() == pavarde.lower()]
        
        if not kliento_nuomos:
            print("Klientas nerastas arba neturi nuomų.")
            return
        
        print(f"\nKliento {vardas} {pavarde} nuomos:")
        for nuoma in kliento_nuomos:
            print(f"Transporto priemonė: {nuoma['transporto_marke']} {nuoma['transporto_modelis']}")
            print(f"Nuomos pradžia: {nuoma['pradzia']}")
            print(f"Nuomos pabaiga: {nuoma['pabaiga'] or 'nebaigta'}")
            print(f"Kaina: {nuoma['kaina']}€")
            print("-" * 30)
    
    elif pasirinkimas == '5':
        print("\nDuomenys išsaugoti. Programa baigia darbą.")
        return True
    else:
        print("Netinkamas pasirinkimas. Bandykite dar kartą.")
    return False

def main():
    
    duomenys = DuomenuValdymas()
    
    if not TransportoPriemone.gauti_visas():
        from Automobilis import Automobilis
        from Mikroautobusas import Mikroautobusas
        
        Automobilis("Toyota", "Corolla", 2020, 50).išsaugoti()
        Automobilis("Volkswagen", "Golf", 2019, 45).išsaugoti()
        Mikroautobusas("Mercedes", "Sprinter", 2021, 80, vietu_sk=12).išsaugoti()
    
    while True:
        rodyti_meniu()
        pasirinkimas = input("Pasirinkite veiksmą (1-5): ").strip()
        if vykdyti_pasirinkima(pasirinkimas):
            break

if __name__ == "__main__":
    main()
