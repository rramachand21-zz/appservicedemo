import logging
import ptvsd
import os

import azure.functions as func

debug_port = int(os.environ['APPSVC_TUNNEL_PORT'])
ptvsd.enable_attach("my_secret", address = ('0.0.0.0', debug_port))

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello {name}!")
    else:
        return func.HttpResponse(
             "Please pass a name on the query string or in the request body",
             status_code=400
        )