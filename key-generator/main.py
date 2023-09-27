from fastapi import FastAPI

from keygen_script import generate_rsa_keys

app = FastAPI()


@app.post("/key-generator")
def generate_keys(body: dict[str, str]):
    body["private_key"], body["public_key"] = generate_rsa_keys()
    return body
