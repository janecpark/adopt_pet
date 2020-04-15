from models import Pet, db
from app import app

db.drop_all()
db.create_all()

Pet.query.delete()

charlie = Pet(name="Charlie Brown", species="Cat", photo_url="https://www.rd.com/wp-content/uploads/2019/05/American-shorthair-cat.jpg", age="2")
shia = Pet(name="Shia", species='Dog', photo_url="https://thehappypuppysite.com/wp-content/uploads/2017/11/maltipoo3-1.jpg", age="3")

db.session.add_all([charlie,shia])
db.session.commit()

