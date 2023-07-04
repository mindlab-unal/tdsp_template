# -*- coding: utf-8 -*-
import argparse
import base64
import json
import requests
import datetime

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def send_image(image_path, service_url):
    encoded_image = encode_image(image_path)
    payload = {
        "image": f"data:image/jpeg;base64,{encoded_image}"
    }
    start_time = datetime.datetime.now()
    response = requests.post(service_url, json=payload)
    print("time = ",(datetime.datetime.now() - start_time).total_seconds())
    return response.json()

def main():
    parser = argparse.ArgumentParser(description="Enviar una imagen a un servicio FastAPI.")
    parser.add_argument("image_path", type=str, help="Ruta de la imagen a enviar.")
    parser.add_argument("service_url", type=str, help="URL del servicio FastAPI.")

    args = parser.parse_args()

    response = send_image(args.image_path, args.service_url)
    print(json.dumps(response, indent=2))

if __name__ == "__main__":
    main()
