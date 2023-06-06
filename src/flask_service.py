from PIL import Image
import pytesseract
import extraction
from contract import Contract
from flask import Flask, request, abort, jsonify
import settings
import repository
import sys
from bson import json_util

SEARCH_PROJETISTA = 'Projetista'
SEARCH_DATA = 'Data'
SEARCH_CONTRATO = 'Contrato'
SEARCH_CONTRATANTE = 'CONTRATANTE'
SEARCH_ENDERECO = 'ENDEREÇO'
SEARCH_EMAIL = 'e-mail'
SEARCH_CPFCNPJ = 'CNPJ/CPF'

app = Flask(__name__)

@app.route('/contract/extraction', methods=['POST'])
def new_contract():
    if 'image' in request.files:
        image = request.files['image']
        text = pytesseract.image_to_string( Image.open(image), lang='por')
        contract_data = extract_contract_data(text)
        print(contract_data)
        return contract_data.to_dict()
    else:
        abort(400, 'no image sent')

@app.route('/contract', methods=['POST'])
def save_contract():
        json_data = request.json
        contract_data = Contract(
             json_data.get('projetista'), 
             json_data.get('data'), 
             json_data.get('contrato'), 
             json_data.get('contratante'), 
             json_data.get('endereco'), 
             json_data.get('email'), 
             json_data.get('cpfcnpj')
             )
        mongo_client = repository.MongoRespository(settings.DB_MONGO_URL, settings.DB_MONGO_DATABASE, settings.DB_MONGO_COLLECTION)
        inserted_id = mongo_client.insert_contract(contract_data)
        inserted_contract = mongo_client.get_contract(inserted_id)
        inserted_contract["_id"] = str(inserted_contract["_id"])
        result_dict = json_util.dumps(inserted_contract, default=str)
        result_dict = json_util.loads(result_dict)

        return jsonify(result_dict)

def extract_contract_data(text):
        projetista = extraction.filter_from_text(text, SEARCH_PROJETISTA)
        data = extraction.filter_from_text(text, SEARCH_DATA)
        contrato = extraction.filter_from_text(text, SEARCH_CONTRATO)
        contratante = extraction.filter_from_text(text, SEARCH_CONTRATANTE)
        endereco = extraction.filter_from_text(text, SEARCH_ENDERECO)
        email = extraction.filter_from_text(text, SEARCH_EMAIL)
        cpfcnpj = extraction.remove_spaces(extraction.filter_from_text(text, SEARCH_CPFCNPJ))
        return Contract(projetista, data, contrato, contratante, endereco, email, cpfcnpj)

def run_local():
    # used just for testing
    print('extracting data...')
    text = pytesseract.image_to_string( Image.open('resources/images/3.jpeg'), lang='por')
    contract_data = extract_contract_data(text)
    print('saving data...')
    mongo_client = repository.MongoRespository(settings.DB_MONGO_URL, settings.DB_MONGO_DATABASE, settings.DB_MONGO_COLLECTION)
    inserted_id = mongo_client.insert_contract(contract_data)
    print(mongo_client.get_contract(inserted_id))

if __name__ == "__main__":
    if '--local' in sys.argv:
        run_local()
    else: 
        app.run()


