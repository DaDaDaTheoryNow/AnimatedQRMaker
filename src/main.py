from fastapi import FastAPI

from qr_generate.router import router as qr_generate_router

app = FastAPI(
    title="Animated QR Maker"
)

app.include_router(qr_generate_router)