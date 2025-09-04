import requests


class extract:

    def __init__(self):
        pass

    def extrac_data(self,country: str) -> list[dict]:    
        """
        Método responsável por extrair os dados da API e transfromar em uma lista

        Args:
            country: list - Nome do país que será pesquisado na API.
        """

        url = f"http://universities.hipolabs.com/search?country={country}"


        response = requests.get(url)
        response.raise_for_status()  
        universities = response.json()

        return universities