#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/10 上午8:15
# @Author  : Nikky
# @Site    : 
# @File    : manage.py
# python3 manage.py db init
# python3 manage.py db migrate
# python3 manage.py db upgrade

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
# from app.biz.models import db
from app.admin.models import db
from app.admin.run import create_app

app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

