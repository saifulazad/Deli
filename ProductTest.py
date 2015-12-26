import random

__author__ = 'Azad'

from app import db
from app import db, models
from faker import Faker
fake = Faker()
import datetime

#product = models.Product(name= 'Sadi product' , description="Sadi product is very cool", price=120)
#
# address1 = models.Address()
#
# address1.body = 'Tamanna Housing Dhaka'
# address1.timestamp = datetime.datetime.utcnow()
# #
# u.addresses.append(address1)

# for x in range(100):
#     product = models.Product(name= fake.name() , description=fake.text(), price=random.randrange(55, 101))
#     db.session.add(product)
#     db.session.commit()
#
# u = models.User.query.get(4)

# p = models.Address(body='51/2', timestamp=datetime.datetime.utcnow(), user=u)
#
#
# db.session.add(p)
# db.session.commit()
# add =models.Address.query.get(1)
#
# print add.user
#
# res = models.User.query.order_by(models.User.id)[0:6]
# #res =models.Address.query.filter(models.Address.body=='51/2').first()
# print res