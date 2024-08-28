from sqlalchemy import Integer, String, UUID
import uuid
from sqlalchemy.orm import Mapped, mapped_column
from aap_wf_init_api_server.webapp_components.database.db_config import db

class User(db.Model): # type: ignore
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(20), unique=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)

class repo_sync(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    repo_url: Mapped[str] = mapped_column(String(200))

class workflow(db.Model):   #associated workflow
    id: Mapped[int] = mapped_column(primary_key=True)
    workflow_url = Mapped[str] = mapped_column(String(200))

class workflow_trigger(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column(String(20))
    filenames: Mapped[str] = mapped_column(String(200))

# Associated workflow : workflow triggers = one : many
# repo_sync: associated_workflow = one : many