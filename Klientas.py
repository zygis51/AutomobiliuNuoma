class Klientas:
    def __init__(self, vardas, pavarde):
        self.vardas = vardas
        self.pavarde = pavarde
        self.nuomos = []
    
    def prideti_nuoma(self, nuoma):
        self.nuomos.append(nuoma)
    
    def gauti_aktyvias_nuomas(self):
        return [n for n in self.nuomos if n.pabaiga is None]
    
    def __str__(self):
        return f"{self.vardas} {self.pavarde}"