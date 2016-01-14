from app import db
from app.models import BlogPost
from slugify import slugify

first = db.session.query(BlogPost).filter_by(id=6).one()
print first.title

first_slug = slugify(first.title)
print first_slug