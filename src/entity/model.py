from datetime import date

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Date, Integer, Boolean, ForeignKey, DateTime, func
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Contact(Base):
    __tablename__ = 'contacts'
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    phone: Mapped[str] = mapped_column(String(13))
    born_date: Mapped[str] = mapped_column(Date())
    delete: Mapped[bool] = mapped_column(default=False)

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'), nullable=True)
    user: Mapped["User"] = relationship('User', backref='contacts', lazy='joined')

    created_at: Mapped[date] = mapped_column('created_at', DateTime(timezone=True), default=func.now(), nullable=True)
    updated_at: Mapped[date] = mapped_column('updated_at', DateTime(timezone=True), onupdate=func.now(), default=func.now(),
                                             nullable=True)


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(150), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255))
    avatar: Mapped[str] = mapped_column(String(250), nullable=True)
    refresh_token: Mapped[str] = mapped_column(String(255), nullable=True)

    created_at: Mapped[date] = mapped_column('created_at', DateTime(timezone=True), default=func.now())
    updated_at: Mapped[date] = mapped_column('updated_at', DateTime(timezone=True), onupdate=func.now(), default=func.now())
