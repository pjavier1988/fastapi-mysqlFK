from fastapi import APIRouter

from .index import router as docs
from .users import router as users
from .persons import router as persons

router = APIRouter()
router.include_router(docs)
router.include_router(users)
router.include_router(persons)