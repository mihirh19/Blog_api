from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
app = FastAPI()


@app.get('/')
def index():
   return {'name' :'mihir'}

@app.get('/blog')
def blog(limit = 10, published: bool = True, sort :Optional[str] = None ):
   if published:
      return {'data': f'blog limit is  {limit}'}
   else:
      return {'data' : 'blog is unpublished'}

@app.get('/blog/{id}/')
def blog_id(id : int):
   return {'data' : f'blog with id {id}'}




@app.get('/blog/unpublished')
def blog_id():
   return {'data' : 'blog is unpublished'}

@app.get('/blog/{id}/comments')
def blog_id_comments(id : int):
   return {'data' : f'blog with id {id} with comments'}


@app.get('/about')
def about():
   return {'name' : 'about page'}

class Blog(BaseModel):
   title : str
   desc : str


@app.post('/blog')
def create_blog(blog  : Blog):
   return {'data' : blog}