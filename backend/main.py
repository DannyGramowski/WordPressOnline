from fastapi import FastAPI
from fileManagment import *



app = FastAPI()

@app.get("/")
def get_file_list():
    return get_user_files()

#for f in get_file_list():
 #    print(f)