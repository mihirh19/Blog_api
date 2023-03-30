def Blog(item)->dict:
   return{
      'id': str(item['_id']),
      'title' : item['title'],
      'desc' : item['desc']
   }
   
def Blogs(entity)->list:
   return [Blog(item) for item in entity]



def User(item)->dict:
   return{
      'name' : item['name'],
      'email': item['email']
   }

def Users(entity) ->list:
   return[User(item) for item in entity]
   