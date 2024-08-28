from sqlalchemy import Integer, String, UUID, ForeignKey, Table, Column
from sqlalchemy.orm import relationship
import uuid
from typing import List
from sqlalchemy.orm import Mapped, mapped_column
from aap_wf_init_api_server.webapp_components.database.db_config import db

class User(db.Model): # type: ignore
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(20), unique=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)


class repo_sync(db.Model):
    __tablename__ = "repo_sync_table"
    id: Mapped[int] = mapped_column(primary_key=True)
    repo_url: Mapped[str] = mapped_column(String(200))
    workflows: Mapped[List["workflow"]] = relationship(back_populates="repo_sync")


association_table_wf_and_wftriggers = Table(
    "association_table_wf_and_wftriggers",
    db.Model.metadata,
    Column("workflow_id", ForeignKey("workflow_table.id"), primary_key=True),
    Column("workflow_trigger_id", ForeignKey("workflow_trigger_table.id"), primary_key=True),
)


class workflow(db.Model):   #associated workflow
    __tablename__ = "workflow_table"
    id: Mapped[int] = mapped_column(primary_key=True)
    workflow_url: Mapped[str] = mapped_column(String(200))
    repo_sync_id: Mapped[int] = mapped_column(ForeignKey("repo_sync_table.id"))
    workflow_triggers: Mapped[List["workflow_trigger"]] = relationship(secondary=association_table_wf_and_wftriggers, back_populates="workflow")


class workflow_trigger(db.Model):
    __tablename__ = "workflow_trigger_table"
    id: Mapped[int] = mapped_column(primary_key=True)
    trigger_name: Mapped[str] = mapped_column(String(100))
    type: Mapped[str] = mapped_column(String(20))
    filenames: Mapped[str] = mapped_column(String(200))
    workflows: Mapped[List["workflow"]] = relationship(secondary=association_table_wf_and_wftriggers, back_populates="workflow_trigger")


# Associated workflow : workflow triggers = one : many
# repo_sync: associated_workflow = one : many