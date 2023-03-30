from fastapi import FastAPI, status
from .routes import blog, user
app = FastAPI()

app.include_router(blog.blog_api, prefix='/blog', tags=['blog'])
app.include_router(user.user_api, prefix='/user', tags=['user'])

@app.get('/', status_code=status.HTTP_200_OK, tags=['server'])
def index():
    return {'message' :'server is running' }
   
   


