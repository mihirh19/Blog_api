from pydantic import BaseModel
from bson import ObjectId
class Blog(BaseModel):
   title : str
   desc :str


class ShowBlog(Blog):

   class Config():
      orm_mode : True



class User(BaseModel):
   name : str
   email : str
   password : str