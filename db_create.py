<<<<<<< HEAD
from app import db
from app.models import User, BlogPost
||||||| merged common ancestors
from project import db
from models import BlogPost
=======
from app import db
from app.models import BlogPost
>>>>>>> fresh

# create the database and the db table
db.create_all()
db.session.add(User("admin", "ad@min.com", "admin"))
# insert data
<<<<<<< HEAD
db.session.add(BlogPost(1,"Good mulit word title", "I\'m good."))
db.session.add(BlogPost(2,"Well", "I\'m well."))
db.session.add(BlogPost(3,"Excellent", "I\'m excellent."))
db.session.add(BlogPost(4,"Okay", "This is a postgres product code post."))
||||||| merged common ancestors
db.session.add(BlogPost("Good", "I\'m good."))
db.session.add(BlogPost("Well", "I\'m well."))
db.session.add(BlogPost("Excellent", "I\'m excellent."))
db.session.add(BlogPost("Okay", "This is a postgres product code post."))
=======
db.session.add(BlogPost("Good", "I\'m good.",1))
db.session.add(BlogPost("Well", "I\'m well.",1))
db.session.add(BlogPost("Excellent", "I\'m excellent.",1))
db.session.add(BlogPost("Okay", "This is a postgres product code post.",1))
>>>>>>> fresh

# commit the changes
db.session.commit()