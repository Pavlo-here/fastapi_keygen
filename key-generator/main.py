from fastapi import FastAPI
from requests import post
from keygen_script import generate_rsa_keys

app = FastAPI()


@app.post("/key-generator")
def generate_keys(body: dict[str, str]):
    # generating rsa keys
    body["private_key"], body["public_key"] = generate_rsa_keys()

    # sending post request to elector commission service without private key
    post("http://0.0.0.0:8000/elector-commission/", {i: body[i] for i in body if i != 'private_key'})

    # returning private and public key attached to passport id back to election portal
    return body
