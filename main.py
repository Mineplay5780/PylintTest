'''
Test document
'''
from fastapi import FastAPI

app = FastAPI()

@app.get("/Test")
async def readtest():
    '''
    
    Testing function
    
    '''
    return { "Hello", "World" }
