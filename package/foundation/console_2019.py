from data_builder_2019 import *
import errno
import shutil
from os import remove
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///EPL_fantasy_2019.db')

#### Change your file path roots accordingly #### 
foundation_db_file = '/Users/asproul/Desktop/projects/fantasy_EPL_update2019/package/foundation/EPL_fantasy_2019.db'
package_db_file = '/Users/asproul/Desktop/projects/fantasy_EPL_update2019/package/EPL_fantasy_2019.db'


def db_creator(file_path_name):
    try:
        remove(file_path_name)
        Base.metadata.create_all(engine)
    except OSError as e:
        if e.errno != errno.ENOENT: # errno.ENOENT = no such file or directory
            raise
        else:
            Base.metadata.create_all(engine)


def db_mover(curent_file_path, destination_file_path):
    try:
        remove(destination_file_path)
        shutil.move(curent_file_path, destination_file_path)
    except OSError as e:
        if e.errno != errno.ENOENT: # errno.ENOENT = no such file or directory
            raise
        else:
            shutil.move(curent_file_path, destination_file_path)


db_creator(foundation_db_file)

Session = sessionmaker(bind=engine)
session = Session()

session.add_all(team_results)
session.commit()

db_mover(foundation_db_file, package_db_file)
