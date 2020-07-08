from app import db
from app import Posts, Users

db.drop_all()
db.create_all()