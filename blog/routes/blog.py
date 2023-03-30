from fastapi import FastAPI, status, Response,HTTPException, APIRouter
from ..models import models
from ..database import client
from ..schemas.schema import Blog, Blogs
from bson import ObjectId
from typing import List

blog_api = APIRouter()

@blog_api.post('/', status_code=status.HTTP_201_CREATED)
async def  create_blog(request : models.Blog):
   client.blog.blog_col.insert_one(dict(request))
   return Blogs(client.blog.blog_col.find())


@blog_api.get('/')
async def show_blog():
   return Blogs(client.blog.blog_col.find())


@blog_api.get('/{id}/', response_model=models.Blog)
async def show_blog_byid(id : str, res:Response):
   oneuser = client.blog.blog_col.find_one({'_id' : ObjectId(id)})
   if oneuser:
      res.status_code = status.HTTP_200_OK
      return Blog(oneuser)
   else:
      # res.status_code = status.HTTP_404_NOT_FOUND
      # return {'message' : f'not found with id {id}'}
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'not found with id {id}')
   

@blog_api.delete('/{id}/', status_code=status.HTTP_200_OK)
def delete_blog(id):
   user_del = client.blog.blog_col.delete_one({'_id' : ObjectId(id)})
   if user_del.deleted_count==0:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'not found with id {id}')
   else:
      return {'message': f'data deleted with id {id}'}
   
   
@blog_api.put('/{id/}', status_code=status.HTTP_202_ACCEPTED)
def update_byid(id , blog:models.Blog):
   user = client.blog.blog_col.find_one_and_update({'_id' : ObjectId(id)}, {'$set' :dict(blog) })
   if user:
      return Blog(user)
   else:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'not found id {id}')
   