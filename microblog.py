import sqlalchemy as sa
import sqlalchemy.orm as so

from app import app, db
from app.models import Post, User


@app.shell_context_processor
def make_shell_context():
    """
    Registered shell context function. When `flask shell` is run, this function
    is invoked and registers the items with the dictionary returned.

    This saves you time and headache with having to import everything when working
    in the shell for testing purposes.
    """
    return {"sa": sa, "so": so, "db": db, "User": User, "Post": Post}
