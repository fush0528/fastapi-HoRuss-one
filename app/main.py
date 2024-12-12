from fastapi import FastAPI
from .routers import router
from .database import Base, engine
#Initialize FastAPI
app = FastAPI()

# Initialize Database's Table
Base.metadata.create_all(bind=engine)

#Register Router
app.include_router(router=router, prfix="/api", tags="[todos]")