from fastapi import FastAPI
from json import dumps
from random import randint, choice, shuffle

app = FastAPI()

lib=dict()

@app.get('/')
#This happens when loading the page
def index():
    """Returns all available objects"""
    return eval(dumps(lib, indent=4))

@app.get('/only_one')
def get_this(this: int):
    """Returns an specific object"""
    return eval(dumps(lib[this], indent=4))

@app.get('/new')
def get_new_random():
    """Posts a new object"""
    key=len(lib)+1
    value=list(choice(str("BNnb1001191743"+"$%&/#@=?*, ")) for i in range(randint(16,32)))
    shuffle(value)
    value=''.join(value)
    lib[key]=value
    return {
        key:value
    }
