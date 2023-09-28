from fastapi import FastAPI,status,Response
from enum import Enum
from routers import blog_get
from routers import blog_post



app=FastAPI()

app.include_router(blog_get.router)
app.include_router(blog_post.router)
@app.get('/hello',tags=["Welcome to FastAPI"])
def hello():
    return {"message":"Hello world!"}
