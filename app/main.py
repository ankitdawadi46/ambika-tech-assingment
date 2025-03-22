import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from app.db import database
from app.schemas.mutation import Mutation
from app.schemas.query import Query

schema = strawberry.Schema(query=Query, mutation=Mutation)

app = FastAPI()


@app.on_event("startup")
async def startup_db():
    await database.connect()


@app.on_event("shutdown")
async def shutdown_db():
    await database.disconnect()


app.include_router(GraphQLRouter(schema), prefix="/graphql")


@app.get("/")
def health_check():
    return {"status": "ok"}
