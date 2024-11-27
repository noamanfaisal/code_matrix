from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from ..database.info import Base
Base = declarative_base()

class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    language = Column(String, nullable=False)
    meta_data = Column(Text)

class Module(Base):
    __tablename__ = "modules"
    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    name = Column(String, nullable=False)
    path = Column(String, nullable=False)
    meta_data = Column(Text)
    project = relationship("Project", back_populates="modules")

class File(Base):
    __tablename__ = "files"
    id = Column(Integer, primary_key=True, index=True)
    module_id = Column(Integer, ForeignKey("modules.id"))
    text = Column(Text, nullable=False)
    path = Column(String, nullable=False)
    chroma_path = Column(String, nullable=True)
    module = relationship("Module", back_populates="files")

class Relation(Base):
    __tablename__ = "relations"
    id = Column(Integer, primary_key=True, index=True)
    file_id = Column(Integer, ForeignKey("files.id"))
    related_file_id = Column(Integer, ForeignKey("files.id"))
    relation_type = Column(String, nullable=False)
    meta_data = Column(Text)
