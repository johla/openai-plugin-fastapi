from fastapi import FastAPI
from routers.wellknown import wellknown
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()
app.include_router(wellknown)
app.add_middleware(CORSMiddleware, allow_origins=["https://chat.openai.com"])


@app.get("/role", summary="Get a role to play", operation_id="getRole")
async def get_role():
    """
    Returns a role to play
    """
    return "You are an elite linguistic professor who is trying to teach a new language to a group of students."
