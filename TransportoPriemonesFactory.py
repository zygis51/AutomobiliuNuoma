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