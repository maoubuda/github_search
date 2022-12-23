import requests
import json


class ListaDeRepositorios():

    def __init__(self, usuario):
        self._usuario = usuario

    def requisicao_api(self):
        resposta = requests.get(
            f'https://api.github.com/users/{self._usuario}/repos')

    def requisicao_api(self):
        resposta = requests.get(
            f'https://api.github.com/users/{self._usuario}/repos')
        if resposta.status_code == 200:
            return resposta.json()
        else:
            return resposta.status_code

    def post_api(self):
        dados_api = self.requisicao_api()
        if type(dados_api) is not int:
            for i in range(len(dados_api)):
                data = {
                    'id': dados_api[i]['id'],
                    'name': dados_api[i]['name'],
                }
                requests.post(
                    url="http://127.0.0.1:8000/api/v1/repos",
                    data=data,
                )
        else:
            print(dados_api)

    def delete_api(self):
        dados_api = self.requisicao_api()
        if type(dados_api) is not int:
            for i in range(len(dados_api)):
                data = dados_api[i]['id']
                requests.delete(
                    url=f"http://127.0.0.1:8000/api/v1/repos/{data}",
                )
        else:
            print(dados_api)

    def imprime_repositorios(self):
        dados_api = self.requisicao_api()
        if type(dados_api) is not int:
            for i in range(len(dados_api)):
                print(dados_api[i]['name'])
        else:
            print(dados_api)


repositorios = ListaDeRepositorios('maoubuda')
repositorios.delete_api()
# repositorios.post_api()
# repositorios.imprime_repositorios()
