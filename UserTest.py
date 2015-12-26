from app import db
from app import db, models

import datetime

# u = models.User(nickname='azada', email='10@email.com')
#
# address1 = models.Address()
#
# address1.body = 'Tamanna Housing Dhaka'
# address1.timestamp = datetime.datetime.utcnow()
# #
# u.addresses.append(address1)
# db.session.add(u)
# db.session.commit()
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

res = models.User.query.order_by(models.User.id)[0:6]
#res =models.Address.query.filter(models.Address.body=='51/2').first()
print res
