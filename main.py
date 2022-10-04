import nest_asyncio
from fastapi import FastAPI, Depends

from application.dependencies import get_service
from application.service import Service

app = FastAPI()
nest_asyncio.apply()


@app.get("/asyncio-demo")
async def get_cat_facts(service: Service = Depends(get_service)):
    return {"facts": (service.collect_cat_facts())}
