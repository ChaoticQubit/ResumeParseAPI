from classes.APIParser import APIParser
import json
from config import settings
from datetime import datetime, timedelta
from urllib.parse import urlparse
from azure.storage.blob import (
    BlobSasPermissions, 
    generate_blob_sas
)

def __parseAzureParams(filepath):
    url = urlparse(filepath)
    account = url.netloc.split('.')[0]
    container = url.path.split('/')[1]
    return account, container

def __generateSASTokenForBlob(filepath, filename) -> str:
    try:
        AZURE_ACC_NAME, AZURE_CONTAINER = __parseAzureParams(filepath)
        AZURE_PRIMARY_KEY = settings.azure_primary_key
        AZURE_BLOB = filename
        AZURE_SAS_EXPIRY = settings.azure_sas_expiry

        sas = generate_blob_sas(
            account_name=AZURE_ACC_NAME,
            container_name=AZURE_CONTAINER,
            blob_name=AZURE_BLOB,
            account_key=AZURE_PRIMARY_KEY,
            permission=BlobSasPermissions(read=True),
            expiry=datetime.utcnow() + timedelta(hours=AZURE_SAS_EXPIRY)
        )
        return 'https://'+AZURE_ACC_NAME+'.blob.core.windows.net/'+AZURE_CONTAINER+'/'+AZURE_BLOB+'?'+sas

    except Exception as ex:
        print('Exception:')
        print(ex)

def __getParsedAffindaData(sas_url) -> dict:
    doc = APIParser(sas_url).getResume()
    file = open('Tests/output.json', 'w')
    file.write(json.dumps(doc))
    file.close()
    return doc