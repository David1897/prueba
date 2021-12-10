from pydantic import BaseModel


class pokemones(BaseModel):
    id:int
    nombre: str
    tipo: str
    color: str
    nivel: int
    comentario: str