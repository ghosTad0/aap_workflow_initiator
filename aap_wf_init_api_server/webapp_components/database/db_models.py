from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from aap_wf_init_api_server.webapp_components.database.db_config import db

class User(db.Model): # type: ignore
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(20), unique=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)