from abc import ABC, abstractmethod
from datetime import datetime

class TransportoPriemone(ABC):
    def __init__(self, marke, modelis, metai, kaina, prieinamumas="laisva"):
        self.marke = marke
        self.modelis = modelis
        self.metai = metai
        self.kaina = kaina
        self.prieinamumas = prieinamumas
    
    @abstractmethod
    def gauti_tipą(self):
        pass
    
    def __str__(self):
        return f"{self.marke} {self.modelis} ({self.metai}), Kaina: {self.kaina}€/d., Būsena: {self.prieinamumas}"
    
    @classmethod
    def gauti_visas(cls):
        priemones = []
        try:
            with open('transporto_priemones.txt', 'r', encoding='utf-8') as f:
                for line in f:
                    if line.strip():
                        data = cls._apdoroti_eilute(line)
                        if data['tipas'] == 'automobilis':
                            from Automobilis import Automobilis
                            priemones.append(Automobilis(
                                data['marke'],
                                data['modelis'],
                                int(data['metai']),
                                float(data['kaina']),
                                data['prieinamumas'],
                                int(data.get('duru_sk', 5))
                            ))
                        elif data['tipas'] == 'mikroautobusas':
                            from Mikroautobusas import Mikroautobusas
                            priemones.append(Mikroautobusas(
                                data['marke'],
                                data['modelis'],
                                int(data['metai']),
                                float(data['kaina']),
                                data['prieinamumas'],
                                int(data.get('vietu_sk', 8))
                            ))
        except FileNotFoundError:

            pass
        return priemones
    
    @staticmethod
    def _apdoroti_eilute(eilute):
        data = {}
        for item in eilute.strip().split(';'):
            key_value = item.split(':', 1)
            if len(key_value) == 2:
                key, value = key_value
                data[key.strip()] = value.strip()
        return data
    
    @classmethod
    def gauti_laisvas(cls):
        return [tp for tp in cls.gauti_visas() if tp.prieinamumas == 'laisva']
    
    def _sukurti_eilute(self):
        data = {
            'marke': self.marke,
            'modelis': self.modelis,
            'metai': str(self.metai),
            'kaina': str(self.kaina),
            'prieinamumas': self.prieinamumas,
            'tipas': self.gauti_tipą()
        }
        if hasattr(self, 'duru_sk'):
            data['duru_sk'] = str(self.duru_sk)
        if hasattr(self, 'vietu_sk'):
            data['vietu_sk'] = str(self.vietu_sk)
        return '; '.join(f"{key}: {value}" for key, value in data.items())
    
    def išsaugoti(self):
        with open('transporto_priemones.txt', 'a', encoding='utf-8') as f:
            f.write(self._sukurti_eilute() + '\n')
    
    def atnaujinti_prieinamumą(self, nauja_būsena):
        self.prieinamumas = nauja_būsena
        visos_priemones = self.__class__.gauti_visas()
        with open('transporto_priemones.txt', 'w', encoding='utf-8') as f:
            for tp in visos_priemones:
                if tp.marke == self.marke and tp.modelis == self.modelis and tp.metai == self.metai:
                    tp.prieinamumas = nauja_būsena
                f.write(tp._sukurti_eilute() + '\n')
