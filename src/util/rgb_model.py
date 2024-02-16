from pydantic import BaseModel

class RGBModel(BaseModel):
    red: int = 255
    green: int = 255
    blue: int = 255