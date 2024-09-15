from fastapi import FastAPI, HTTPException
from typing import Optional

from Models import TodoList, TodoItem

app = FastAPI()

todos = []

@app.get("/todos/", response_model=TodoList)
async def read_todos():
    return {"todos": todos}

@app.post("/todos/")
async def create_todo(title: str, description: str):
    todo = {"id": len(todos) + 1, "title": title, "description": description, "completed": False}
    todos.append(todo)
    return todo

@app.put("/todos/{todo_id}/", response_model=TodoItem)
async def update_todo(todo_id: int, title: Optional[str] = None, description: Optional[str] = None):
    for todo in todos:
        if todo["id"] == todo_id:
            todo["title"] = title if title else todo["title"]
            todo["description"] = description if description else todo["description"]
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

@app.delete("/todos/{todo_id}/")
async def delete_todo(todo_id: int):
    for idx, todo in enumerate(todos):
        if todo["id"] == todo_id:
            del todos[idx]
            return {"message": "Todo deleted"}
    raise HTTPException(status_code=404, detail="Todo not found")