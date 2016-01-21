from app import db
from app.models import BlogPost
from slugify import slugify

# first = db.session.query(BlogPost).filter_by(id=6).one()
# print first.title

# first_slug = slugify(first.title)
# print first_slug

import datetime 
current_time = datetime.datetime.now()
print current_time

# from time import esttime, strftime
# print strftime("%Y-%m-%d %H:%M:%S", gmtime())
print datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print '{dt:%A} {dt:%B} {dt.day}, {dt.year}'.format(dt=datetime.datetime.now())
print '{dt:%H:%M}'.format(dt=datetime.datetime.now())