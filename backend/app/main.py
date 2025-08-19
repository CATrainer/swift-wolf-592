from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

app = FastAPI(title="Todo API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = ""

class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

class Todo(BaseModel):
    id: int
    title: str
    description: str
    completed: bool
    created_at: datetime

# In-memory storage
todos = []
next_id = 1

@app.get("/")
def read_root():
    return {"message": "Todo API is running"}

@app.get("/todos", response_model=List[Todo])
def get_todos():
    return todos

@app.post("/todos", response_model=Todo)
def create_todo(todo: TodoCreate):
    global next_id
    new_todo = Todo(
        id=next_id,
        title=todo.title,
        description=todo.description,
        completed=False,
        created_at=datetime.now()
    )
    todos.append(new_todo)
    next_id += 1
    return new_todo

@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, todo_update: TodoUpdate):
    for todo in todos:
        if todo.id == todo_id:
            if todo_update.title is not None:
                todo.title = todo_update.title
            if todo_update.description is not None:
                todo.description = todo_update.description
            if todo_update.completed is not None:
                todo.completed = todo_update.completed
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    global todos
    todos = [todo for todo in todos if todo.id != todo_id]
    return {"message": "Todo deleted"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)