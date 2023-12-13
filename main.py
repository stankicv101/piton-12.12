from fastapi import FastAPI 
from database import engine
import models, routers
import uvicorn

#Kreiranje tabele u bazi, ako ne postoji
models.Base.metadata.create_all(bind=engine)

app=FastAPI()

#Ukljucivanje rutera u aplikaciju
app.include_router(routers.router)

#Dodavanje logike za pokretanje Uvicorn servera
if __name__ =="__main__":
    uvicorn.run(app, host= "0.0.0.0", port=8000)


#.env
#DB_USER=viktor
#DB_PASSWORD=viktor2023
#DB_HOST=192.168.104.11
#DB_NAME=viktor