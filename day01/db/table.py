from .database import Base
from sqlalchemy import Integer,String,Column
from sqlalchemy.orm import class_mapper

class Classroom(Base):
    __tablename__ = "classroom"
    id = Column(Integer,primary_key=True) # 主键
    name = Column(String)
    num = Column(Integer)
    teacher = Column(String)
    img = Column(String)

def serial(obj): #obj 传入单个数据对象
    columns = [c.key for c in class_mapper(obj.__class__).columns]
    data ={c:getattr(obj,c) for c in columns}
    #获取对象属性的函数 getattr()
    return data