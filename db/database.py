from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy import String

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str]
    mail: Mapped[str]
    payment_methods: Mapped[str]

    # payment_methods: Mapped[list[str]] = mapped_column(ARRAY(String), default=[]) - в sqlite не работает - надо разобраться

class Payment_method(Base):
    __tablename__ = "payment_methods"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(nullable=True)

    # default= self.Payment_method - надо разобраться

    logo: Mapped[str] = mapped_column(nullable=True)
    short_name: Mapped[str]
    description: Mapped[str]

SessionLocal = sessionmaker(autoflush=False, bind=engine)