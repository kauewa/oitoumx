import requests

#/overallresults/latest/XC/s1 - s1 = supercross
#overallresults/latest/XC/x1 - x1 = supermotocross
#overallresults/latest/XC/m1 - m1 = motocross

#https://data-aws.amaproracing.com/api/pointstandings/series/2023/m1
#https://data-aws.amaproracing.com/api/overallresults/M2305/m1

#https://data-aws.amaproracing.com/api/apps/event/mx/M2305/1

#https://data-aws.amaproracing.com/api/pointstandings/smxcombined/2023/x1
#https://data-aws.amaproracing.com/api/pointstandings/series/thin/2023/X1



# FUNÇÕES
    # TODAS EQUIPES() -> EQUIPES []
    # TODOS PILOTOS() -> PILOTOS []
    # PONTUAÇÃO SMX() -> PILOTOS []
    # PONTUAÇÃO SX() -> PILOTOS []
    # PONTUAÇÃO MX() -> PILOTOS []
    # PONTUAÇÃO EQUIPES() -> EQUIPES []
    # ETAPAS SX() -> ETAPA []
    # ETAPAS MX() -> ETAPA []
    # ETAPAS SMX() -> ETAPA []
    # PILOTO(piloto) -> PILOTO  OBS: fuzzywuzzy
    # ETAPA(numero_etapa) -> ETAPA --- PROCURA LISTA COM NOMES ETAPAS, OU FAZER PRÉ-REQ EM TODAS ETAPAS, PARA FAZER A LISTA POR NOME


# ORGANIZAR EM CLASSES ----- SMX - PAI
                        #    SX  - FILHO
                        #    MX  - FILHO





CAMPEONATOS = {
    'SX1': 's1',
    'SX2': 's2',
    'MX1': 'm1',
    'MX2': 'm2',
    'SMX1':  'x1',
    'SMX2': 'x2' 
}

class Smx:
    def __init__(self):
        self.headers = {
            'authority': 'data-aws.amaproracing.com',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
            'origin': 'https://www.supermotocross.com',
            'referer': 'https://www.supermotocross.com/',
            'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
        }
        self.link = 'https://data-aws.amaproracing.com/api/'

    def __request(self, path):
        response = requests.get(self.link + path, headers=self.headers)
        if response.status_code == 200:
            return response.content
        return None

    def ultimos_resultados(self, campeonato:str):
        path = 'overallresults/latest/XC/' + CAMPEONATOS[campeonato]
        results = self.__request(path)
        return results


smx = Smx()

results = smx.ultimos_resultados('SX1')
print(results)