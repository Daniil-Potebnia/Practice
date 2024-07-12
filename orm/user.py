from sqlalchemy.orm import Mapped, MappedColumn
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from orm.db_session import SqlBase


class User(SqlBase, UserMixin):
    __tablename__ = 'user'

    id: Mapped[int] = MappedColumn(primary_key=True)
    login: Mapped[str] = MappedColumn(unique=True)
    email: Mapped[str] = MappedColumn(unique=True)
    hashed_password: Mapped[str] = MappedColumn()

    def __repr__(self) -> str:
        return f'{self.id}: {self.login}'

    def set_email(self, email: str):
        self.email = email

    def set_login(self, login: str):
        self.login = login

    def set_hashed_password(self, password: str):
        self.hashed_password = generate_password_hash(password)

    def check_hashed_password(self, password: str):
        return check_password_hash(self.hashed_password, password)
