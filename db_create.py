from app import db
from app.models import User, BlogPost

# create the database and the db table
db.create_all()
db.session.add(User("admin", "ad@min.com", "admin"))
# insert data
db.session.add(BlogPost(1,"Good mulit word title", "I\'m good."))
db.session.add(BlogPost(2,"Well", "I\'m well."))
db.session.add(BlogPost(3,"Excellent", "I\'m excellent."))
db.session.add(BlogPost(4,"Okay", "This is a postgres product code post."))

# commit the changes
db.session.commit()