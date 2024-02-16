import base64
import io
from fastapi import APIRouter
from qr_generate.schemas import QRCode, StaticQRCodeRequest, StaticQRCodeResponseModel, AnimatedQRCodeRequest, AnimatedQRCodeResponseModel
from urllib.request import urlopen

import segno

router = APIRouter(
    prefix="/qr_generate",
    tags=["Generate QR Code"]
)


@router.post("/static", response_model=StaticQRCodeResponseModel)
def generate_static_qr_code(qr_request: StaticQRCodeRequest):
    qrcode = segno.make_qr(qr_request.content)
    image_buffer = io.BytesIO()

    qrcode.save(image_buffer,
                kind="png",
                scale=qr_request.scale,
                dark=(qr_request.qr_code_color.red, qr_request.qr_code_color.green, qr_request.qr_code_color.blue),
                border=qr_request.border_size,
                light=(qr_request.border_color.red, qr_request.border_color.green, qr_request.border_color.blue),
                data_dark=(qr_request.data_color.red, qr_request.data_color.green, qr_request.data_color.blue))
    
    image_buffer.seek(0)
    return StaticQRCodeResponseModel(status="success", data=QRCode(image_bytes=base64.b64encode(image_buffer.read()),
                                                                   content=qr_request.content))
    
@router.post("/animated", response_model=AnimatedQRCodeResponseModel)
def generate_animated_qr_code(qr_request: AnimatedQRCodeRequest):
        qrcode = segno.make_qr(qr_request.content)
        image_buffer = io.BytesIO()
        
        video_url = urlopen(qr_request.background_video_link)
        qrcode.to_artistic(
            background=video_url,
            target=image_buffer,
            scale=qr_request.scale,
            kind='gif'
        )
        
        image_buffer.seek(0)
        return AnimatedQRCodeResponseModel(status="success", data=QRCode(image_bytes=base64.b64encode(image_buffer.read()),
                                                                        content=qr_request.content))