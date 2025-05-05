from datetime import datetime

class Nuoma:
    def __init__(self, klientas, transporto_priemone, kaina):
        self.klientas = klientas
        self.transporto_priemone = transporto_priemone
        self.kaina = kaina
        self.pradzia = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.pabaiga = None
    
    def baigti_nuoma(self):
        self.pabaiga = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def __str__(self):
        return (f"Nuoma: {self.transporto_priemone.marke} {self.transporto_priemone.modelis}\n"
                f"Klientas: {self.klientas.vardas} {self.klientas.pavarde}\n"
                f"Kaina: {self.kaina}€\n"
                f"Pradžia: {self.pradzia}\n"
                f"Pabaiga: {self.pabaiga or 'nebaigta'}\n"
                f"{'-'*30}")