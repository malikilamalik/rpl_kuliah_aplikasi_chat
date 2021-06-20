from dotenv import load_dotenv
import os

class AppEnv:
    def __init__(self):
        load_dotenv()

    def SECRET_KEY(self):
        return os.getenv("SECRET_KEY")

    def JWT_SECRET_KEY(self):
        return os.getenv("JWT_SECRET_KEY")
    
    def DB_USER(self):
        return os.getenv("DB_USER")

    def DB_PASSWORD(self):
        return os.getenv("DB_PASSWORD")
    
    def DB_HOST(self):
        return os.getenv("DB_HOST")
    
    def DB_NAME(self):
        return os.getenv("DB_NAME")
    
    def DB_PORT(self):
        return os.getenv("DB_PORT")
    
    def DB_SQL_URI(self):
        URI = "mysql+pymysql://%s:%s@%s:%s/%s" % (self.DB_USER(), self.DB_PASSWORD(),self.DB_HOST(), self.DB_PORT(), self.DB_NAME())
        return URI
