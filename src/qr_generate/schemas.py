from util.rgb_model import RGBModel
from pydantic import BaseModel

class QRCode(BaseModel):
    content: str
    image_bytes: str

### models for generate static(without video) qr code / png
class StaticQRCodeRequest(BaseModel):
    content: str
    border_size: int = 1
    scale: int = 15
    qr_code_color: RGBModel = RGBModel(red=0, green=0, blue=0)
    data_color: RGBModel = RGBModel(red=0, green=0, blue=0)
    border_color: RGBModel

class StaticQRCodeResponseModel(BaseModel):
    status: str
    data: QRCode
### end


### models for generate static(without video) qr code / png
class AnimatedQRCodeRequest(BaseModel):
    content: str
    scale: int = 15
    background_video_link: str

class AnimatedQRCodeResponseModel(BaseModel):
    status: str
    data: QRCode
### end