from app import app, db
from models import Homelibrary, Author

@app.shell_context_processor
def make_shell_context():
   return {
       "db": db,
       "User": Homelibrary,
       "Post": Author
   }