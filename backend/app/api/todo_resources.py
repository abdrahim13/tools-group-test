from flask_restful import Resource, request
from app.models.todo import Todo as TodoModel


from app.service.todo import (
    create_todo,
    delete_todo,
    get_todo_by_id,
    get_todos,
    search_by_text,
    update_todo)


# /api/todo
class Todo(Resource):

    def get(self, todo_id):

        return get_todo_by_id(todo_id)

    def put(self, todo_id):
        try:
            json_data = request.get_json(force=True)
            return update_todo(todo_id, json_data)

        except Exception as e:
            return {'error': 'Invalid JSON payload', "stack": str(e)}, 400

    def delete(self, todo_id):
        return delete_todo(todo_id)


# /api/todos
class TodoList(Resource):

    def get(self):
        return get_todos()

    def post(self):
        try:
            json_data = request.get_json(force=True)
        except Exception as e:
            return {'error': 'Invalid JSON payload', "stack": str(e)}, 400
        return create_todo(json_data)


# /api/search
class SearchTodoList(Resource):

    def get(self):
        text = request.args.get('text', "")
        return search_by_text(text)
