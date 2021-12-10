from fastapi import APIRouter
from modelos import *
from typing import Optional
import database

user = APIRouter()

@user.get("/")
def inicio():
    return "Inicio del FastApi"