from fastapi import FastAPI
from random import randint, choice, shuffle
from pydantic import BaseModel
from typing import List

app = FastAPI()


class PassWord(BaseModel):
    __slots__=["id", "value"]

    id:int
    value:str
    
    def __gt__(self, other):
        return (dict(self).get("id")>dict(other).get("id"))

    def __eq__(self, other):
        dict(self).get("id")==dict(other).get("id")


lib: List[PassWord]=list()

@app.get('/')
@app.get('/all')
#This happens when loading the page
def index():
    """Returns all available objects"""
    return {
        "values": lib
    }

@app.get('/only_one')
def get_this(this: int):
    """Returns an specific object"""
    got = {
        "msg": "Failed to accomplish the task"
    }
    try:
        got=lib[this]
    except:
        pass
        

    return got


@app.get('/put_new_random')
@app.get('/new_random')
def put_new_random():
    """Puts a new random"""
    key=len(lib)+1
    value=list(choice(str("BNnb1001191743"+"$%&/#@=?*, ")) for i in range(randint(16,32)))
    shuffle(value)
    value=''.join(value)
    the_new=PassWord(id=key, value=value)
    lib.append(the_new)
    return the_new

@app.get('/get_new_random')
def get_new_random():
    """Gets a new random"""
    key=len(lib)+1
    value=list(choice(str("BNnb1001191743"+"$%&/#@=?*, ")) for i in range(randint(16,32)))
    shuffle(value)
    value=''.join(value)
    the_new=PassWord(id=key, value=value)
    return the_new

@app.put('/add')
def put_one(this: PassWord):
    
    if (this not in lib):
        got=this
        lib.append(got)
        lib.sort()
    else:
        got={
            "msg": "An object with the specified ID already exists in DB"
        }
    return got