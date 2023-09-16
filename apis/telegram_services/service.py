from ast import alias
from http.client import NOT_FOUND
import json
import requests
from django.conf import settings
from apis.api_services.config import *

from mcapi.models import Recette


class bot_api:
    #recuperer les requettes depuis l'api
    def get_response_json(self, url):
        response = requests.request("GET", url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("response.text")
    # recuperer sous forme de dict
    def get_requets_dict(self, url, Model):
        data= self.get_response_json(url)
        data_list = [Model.from_dict(model) for model in data]
        return data_list
    # recuperer sous forme de json
    def get_requets_simple(self, url, Model):
        data= self.get_response_json(url)
        return data
    
    #filter les donnes selon un index
    def get_requets_with_index(self, url, Model, type, index, ):
        data= self.get_response_json(url)
        response = [Model for model in data if model[type] == index]
        return response
        
        