from app.models.todo import Todo


def create_todo(todo_data):
    """
    create a new todo
    """
    # validate data
    if not todo_data:
        return {'error': 'Invalid JSON payload'}, 400
    text = todo_data.get('text')
    done = todo_data.get('done', False)
    important = todo_data.get('important', False)
    if not text:
        return {'error': 'text is required'}, 400

    todo = Todo(text, done, important)
    todo.save()
    return todo.to_dict(), 201


def get_todo_by_id(todo_id):
    """
    get todo by id
    """
    return Todo.query.filter_by(id=todo_id).first()


def get_todos():
    """
    get all todos
    """
    todos = Todo.query.all()
    return Todo.list_to_json(todos)


def update_todo(todo_id, data):
    """
    update todo
    """
    todo = Todo.query.filter_by(id=todo_id).first()

    if not todo:
        return {'error': 'Todo not found'}, 404
    if not data:
        return {'error': 'Invalid JSON payload'}, 400

    todo.update(data)

    return todo.to_dict()


def delete_todo(todo_id):
    """
    delete todo
    """
    todo = Todo.query.filter_by(id=todo_id).first()
    if not todo:
        return False
    todo.delete()
    return True


def toggle_done(todo_id, done):
    """
    toggle todo done
    """
    todo = Todo.query.filter_by(id=todo_id).first()
    if not todo:
        return False
    todo.update({'done': done})
    return todo


def toggle_important(todo_id, important):
    """
    toggle todo important
    """
    todo = Todo.query.filter_by(id=todo_id).first()
    if not todo:
        return False
    todo.update({'important': important})
    return todo


def search_by_text(text, skip=0, limit=10):
    """
    search todo by text
    """
    todos = Todo.query.filter(Todo.text.like(
        f'%{text}%')).offset(skip).limit(limit).all()
    
    return Todo.list_to_json(todos)
