class DuomenuValdymas:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DuomenuValdymas, cls).__new__(cls)
            cls._instance._init_data()
        return cls._instance
    
    def _init_data(self):
        # Inicijuojame tuščius failus, jei jų nėra
        for filename in ['transporto_priemones.txt', 'klientai.txt', 'nuomos.txt']:
            try:
                open(filename, 'x', encoding='utf-8').close()
            except FileExistsError:
                pass
    
    def _apdoroti_eilute(self, eilute):
        data = {}
        for item in eilute.strip().split(';'):
            key_value = item.split(':', 1)
            if len(key_value) == 2:
                key, value = key_value
                data[key.strip()] = value.strip()
        return data
    
    def gauti_klientus(self):
        klientai = []
        try:
            with open('klientai.txt', 'r', encoding='utf-8') as f:
                for line in f:
                    if line.strip():
                        data = self._apdoroti_eilute(line)
                        klientai.append(data)
        except FileNotFoundError:
            pass
        return klientai
    
    def prideti_klienta(self, klientas):
        with open('klientai.txt', 'a', encoding='utf-8') as f:
            f.write(f"vardas: {klientas.vardas}; pavarde: {klientas.pavarde}\n")
    
    def issaugoti_nuoma(self, nuoma):
        with open('nuomos.txt', 'a', encoding='utf-8') as f:
            data = {
                'kliento_vardas': nuoma.klientas.vardas,
                'kliento_pavarde': nuoma.klientas.pavarde,
                'transporto_marke': nuoma.transporto_priemone.marke,
                'transporto_modelis': nuoma.transporto_priemone.modelis,
                'pradzia': nuoma.pradzia,
                'pabaiga': nuoma.pabaiga or "",
                'kaina': str(nuoma.kaina)
            }
            eilute = '; '.join(f"{key}: {value}" for key, value in data.items())
            f.write(eilute + '\n')
    
    def gauti_nuomas(self):
        nuomos = []
        try:
            with open('nuomos.txt', 'r', encoding='utf-8') as f:
                for line in f:
                    if line.strip():
                        nuomos.append(self._apdoroti_eilute(line))
        except FileNotFoundError:
            pass
        return nuomos