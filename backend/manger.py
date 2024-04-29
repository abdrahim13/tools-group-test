import sys
from app import app, db


# Note:
# This is a simple manager script
# to run the app and create the database

def main(command):
    with app.app_context():
        if command == 'create_db':
            # drop all tables
            db.drop_all()
            db.create_all()
        elif command == 'run':
            app.run(debug=True)
        else:
            print('Invalid command')


if __name__ == '__main__':
    command = sys.argv[1]
    main(command)
