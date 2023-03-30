from fastapi import APIRouter, status, HTTPException
from ..models import models
from ..database import client
from ..schemas.schema import User, Users
from ..hashing import Hash
from bson import ObjectId
user_api = APIRouter()





@user_api.post('/', status_code=status.HTTP_201_CREATED)
def create_user(request : models.User):
   hash =Hash.bcrypt(request.password)
   request.password = hash
   client.blog.user_col.insert_one(dict(request))
   
   return Users(client.blog.user_col.find())
   



@user_api.get('/{id}', status_code=status.HTTP_202_ACCEPTED)
def get_user(id):
   one = client.blog.user_col.find_one({'_id':ObjectId(id) })
   if one:
      return User(one)
   else:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'no user avilable with id {id}')