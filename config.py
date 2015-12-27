__author__ = 'Azad'
import os
basedir = os.path.abspath(os.path.dirname(__file__))

# for postgresql

#SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost:3306/test'
#'sqlite:///sqlalchemy_example.db'



SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'our.db')


SECRET_KEY = 'Sm9obiBTY2hyb20ga2lja3MgYXNz'
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')