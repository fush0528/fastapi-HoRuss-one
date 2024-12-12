from fastapi import Depends,APIRouter, HTTPException
from sqlalchemy.orm import Session #建議第三方套件放上面


from .schemas import TodoCreate, TodoResponse #自己寫的放下面
from .models import Todo
from .database import SessionLocal

router = APIRouter() #將原本的app改成router


#Database Ingection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



'''
ROUTING
'''

@router.post("/todos",response_model = TodoResponse)
def create_todo(todo: TodoCreate,db: Session = Depends(get_db)):
    db_todo =Todo(**todo.dict())
    db.add(db_todo)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

@router.get("/todos",response_model = list[TodoResponse])
def read_todos(db: Session = Depends(get_db)):
    return db.query(Todo).all()

@router.get("/todo/{todo_id}",response_model = TodoResponse)
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = db.query(Todo).filter(Todo,id == todo_id).fitst()
    if not db_todo:
        raise HTTPException(status_code=404, detaols="Todo not found")
    return db_todo

@router.put("/todo/{todo_id}",response_model = TodoResponse)
def updata_todo(todo_id: int,todo: TodoCreate, db:Session = Depends(get_db)):
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not db_todo:
        raise HTTPException(status_code=404, details = "Todo not found")
    for key,value in todo.dict().items():
        setattr(db_todo,key,value)
    db.commit()
    db.refresh(db_todo)
    return db_todo


@router.delete("/todo/{todo_id}")
def delete_todo(todo_id: int,db: Session = Depends(get_db)):
    db_todo = db.query(Todo).filter(Todo.id == todo_id).fitst()
    if not db_todo:
        raise HTTPException(status_code=404, details="Todo not found")
    db.delete(db_todo)
    db.commit()
    return {"detail": "Todo deleted successfully"}