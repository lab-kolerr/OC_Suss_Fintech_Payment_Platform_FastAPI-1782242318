from fastapi import APIRouter

router = APIRouter()

@router.get("/users/")
async def read_users():
    return ["user1", "user2", "user3"]