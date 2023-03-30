from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
class Hash():
   def bcrypt(passw:str):
      return pwd_context.hash(passw)