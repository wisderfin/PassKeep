import bcrypt
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String,  func
Base = declarative_base()

class Password(Base):
    __tablename__ = 'passwords'
    title = Column(String, primary_key=True)
    login = Column(String, default=None)
    phone = Column(String, default=None)
    mail = Column(String, default=None)
    password = Column(String, default=None)

    def __init__(self, title, login, phone, mail, password):
        self.title = title
        self.login = bcrypt.hashpw(login.encode(), bcrypt.gensalt())
        self.phone = bcrypt.hashpw(phone.encode(), bcrypt.gensalt())
        self.mail = bcrypt.hashpw(mail.encode(), bcrypt.gensalt())
        self.password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

