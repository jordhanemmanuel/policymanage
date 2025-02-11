from enum import Enum
from typing import List
from fastapi import APIRouter
from routes.policy_route import router as __policy_router

class RouterTag():
    def __init__(self, router: APIRouter, tags: List[str | Enum] | None):
        self.router = router
        self.tags = tags

def get_routes():
    routes = [
        RouterTag(router = __policy_router, tags = ["Policy"])
    ]
    return routes