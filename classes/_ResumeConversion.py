from affinda import AffindaAPI, TokenCredential
from config import settings
import json

API_TOKEN = settings.affinda_token
credential = TokenCredential(token = API_TOKEN)
client = AffindaAPI(credential = credential)

class _ResumeConversion:
    def __init__(self, sas_url):
        self.sas_url = sas_url
        self.resume = self.__getAffindaResume()
        self.resumeJson = json.loads(self.__convertToJSON())

    def __getAffindaResume(self):
        try:  
            return client.create_resume(url=self.sas_url).as_dict()["data"]
        except Exception as ex:
            print('Exception:')
            print(ex)

    def __convertToJSON(self):
        return json.dumps(self.resume)