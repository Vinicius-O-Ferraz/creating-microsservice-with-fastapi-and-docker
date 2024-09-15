"""Responsável por lidar com a lógica de negócios do aplicativo e acessar os dados. Ela pode ser implementada usando uma biblioteca de ORM,
como SQLAlchemy ou Tortoise ORM. Com o ORM, você pode definir os seus modelos de banco de dados como classes Python e, em seguida, interagir
com o banco de dados usando essas classes."""


# Import necessary components from Pydantic and typing modules
from pydantic import BaseModel
from typing import List

# Define a Pydantic model for a single TodoItem
class TodoItem(BaseModel):
    id: int  # Integer ID for the TodoItem
    title: str  # Title of the TodoItem, expected to be a string
    description: str  # Description of the TodoItem, expected to be a string
    completed: bool = False  # Boolean flag indicating whether the TodoItem is completed, default is False

# Define another Pydantic model representing a TodoList
class TodoList(BaseModel):
    todos: List[TodoItem] = []  # List of TodoItem objects, initialized as empty by default