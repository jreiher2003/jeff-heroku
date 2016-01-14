from app import db
from app.models import User

db.create_all()
# insert data
db.session.add(User("Jeffrey", "me@jeffreiher.com", "1234"))
db.session.add(User("admin", "ad@min.com", "admin"))

# commit the changes
db.session.commit()