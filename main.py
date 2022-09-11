from fastapi import FastAPI, Body, Depends
import schemas
import models

from databse import Base, engine, SessionLocal
from sqlalchemy.orm import Session


Base.metadata.create_all(engine)

def get_session():
    session = SessionLocal()
    try:
        yield session

    finally:
        session.close()


app = FastAPI()

fateDatabse = {
    1:{'task':'clean car'},
    2:{'task':'clean understanding'},
    3:{'task':'people power '},
}


@app.get('/')
def get_items(session: Session = Depends(get_session)):
    items = session.query(models.Item).all()
    return items



@app.get('/{id}')
def get_item(id:int, session: Session = Depends(get_session)):
    try: 
        item = session.query(models.Item).get(id)
        return item
    except:
        return "sorry, item not found"

@app.post('/')
def additem(item:schemas.Item, session: Session = Depends(get_session)):
    item = models.Item(task = item.task)
    session.add(item)
    session.commit()
    session.refresh(item)
    return item


@app.put('/{id}')
def updateItem(id:int, item:schemas.Item, session: Session = Depends(get_session)):
    itemobj = session.query(models.Item).get(id)
    itemobj.task = item.task
    session.commit()
    return itemobj

@app.delete('/{id}')
def deleteitem(id:int,  session: Session = Depends(get_session)):
    itemobject =session.query(models.Item).get(id)
    session.delete(itemobject)
    session.commit()
    session.close()
    return {"Message ": "Item Was deleted", "item":itemobject}