from typing import Union
import cv2
import numpy as np
from fastapi import FastAPI, HTTPException, status
from fastapi.responses import StreamingResponse
import io

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hi! Welcome to my API.The Solar System API provides information for thousands of all solar system planets and their moons."}

@app.get("/planets")
def planets():
    list = ["Neptune", "Venus","Jupiter", "Earth", "Mars", "Saturn", "Uranus", "Mercury"]
    return {"list of all solar system planets": list}

@app.get("/planets/{planet_name}")
def planet_info(planet_name: str):
    if planet_name == "mercury":
        information = "Mercury is the closest planet to the Sun, and the smallest planet in our solar system "
    elif planet_name == "venus":
        information = "Venus is the second planet from the Sun, and the sixth largest planet. "
    elif planet_name == "earth":
        information = "Earth – our home planet – is the third planet from the Sun, and the fifth largest planet. It's the only place we know of inhabited by living things. "
    elif planet_name == "mars":
        information = "Mars is the fourth planet from the Sun, and the seventh largest. It’s the only planet we know of inhabited entirely by robots. "
    elif planet_name == "jupiter":
        information = "Jupiter is the fifth planet from the Sun, and the largest in the solar system – more than twice as massive as the other planets combined."
    elif planet_name == "saturn":
        information = "Saturn is the sixth planet from the Sun, and the second largest in the solar system. It’s surrounded by beautiful rings. "
    elif planet_name == "uranus":
        information = "Uranus is the seventh planet from the Sun, and the third largest planet in our solar system. It appears to spin sideways."
    elif planet_name == "neptune":
        information = "Neptune is the eighth, and most distant planet from the Sun. It’s the fourth-largest, and the first planet discovered with math. "
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                             detail="The names of the planets should be chosen from the opposite names: mercury, venus, earth, mars, jupiter, saturn, uranus, neptune.")

    return{f"Information of {planet_name}" : information} 

@app.get("/planets/{planet_name}/image")
def planet_info(planet_name: str):
    if planet_name == "mercury":
        img = cv2.imread("io/planets/mercury.jpg")
    elif planet_name == "venus":
        img = cv2.imread("io/planets/venus.jpg")
    elif planet_name == "earth":
        img = cv2.imread("io/planets/earth.jpg")
    elif planet_name == "mars":
        img = cv2.imread("io/planets/mars.jpg")
    elif planet_name == "jupiter":
        img = cv2.imread("io/planets/jupiter.jpg")
    elif planet_name == "saturn":
        img = cv2.imread("io/planets/saturn.jpg")
    elif planet_name == "uranus":
        img = cv2.imread("io/planets/uranus.jpg")
    elif planet_name == "neptune":
        img = cv2.imread("io/planets/neptune.jpg")
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                              detail="The names of the planets should be chosen from the opposite names: mercury, venus, earth, mars, jupiter, saturn, uranus, neptune.")
    
    _, encode_img = cv2.imencode(".png", img)
    return StreamingResponse(content=io.BytesIO(encode_img.tobytes()), media_type = "image/png")