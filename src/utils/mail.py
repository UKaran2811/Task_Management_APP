from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from fastapi import FastAPI
from pydantic import EmailStr, BaseModel
from typing import List


conf = ConnectionConfig(
    MAIL_USERNAME = "techsimplus@gmail.com",
    MAIL_PASSWORD = "kjvd ywia mmln ooir",
    MAIL_FROM = "mrcr123073@gmail.com",
    MAIL_PORT = 587,
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_FROM_NAME = "Mr. CR",
    MAIL_STARTTLS = True,
    MAIL_SSL_TLS = False,
    USE_CREDENTIALS =True,
    VALIDATE_CERTS = True

)

app = FastAPI()

@app.post("/email")
async def send_mail(email:List[str]):
    html = """<p>Hi, thanks for registration</p>"""

    message = MessageSchema(
        subject="Task Management app Registration",
        recipients = email,
        body=html,
        subtype=MessageType.html
    )

    fm = FastMail(conf)
    await fm.send_message(message)
    return {"message": "email has been sent"}