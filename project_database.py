from sqlalchemy import Column,Integer,String
from sqlalchemy .ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship #used to connect t other files

Base=declarative_base()

class Register(Base):
	__tablename__='register'

	id=Column(Integer,primary_key=True)#by default ID will be generated in sqlalchemy
	name=Column(String(100))
	surname=Column(String(100))
	mobile=Column(String(20))
	email=Column(String(50))
	branch=Column(String(100))
	role=Column(String(10))


engine=create_engine('sqlite:///iii.db')	#table is stored in engine
Base.metadata.create_all(engine)	#to know which type of data is present in table
print("database is created............")


