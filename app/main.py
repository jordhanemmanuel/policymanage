import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from config.middleware import middleware_log
from config.routers import get_routes

app = FastAPI(
    title="Offline Challenge",
    description="Assess technical skills in a realistic scenario.",
    version="1.0",
    contact={"name": "Jordhan Emmanuel Marciano da Silva", "email": "jordhanemmanuel@gmail.com"}
)

origins = ["*", "0.0.0.0"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(BaseHTTPMiddleware, dispatch=middleware_log)

for route in get_routes():
    app.include_router(route.router, tags=route.tags, prefix="/api")

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=5000)
