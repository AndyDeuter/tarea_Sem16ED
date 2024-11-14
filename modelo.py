from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Autores(Base):
    __tablename__ = 'tbl_autor'

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    nacionalidad = Column(String)

    libros = relationship("Libros", back_populates="autor")

class Categorias(Base):
    __tablename__ = 'tbl_categoria'

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)

    libros = relationship("Libros", back_populates="categoria")

class Libros(Base):
    __tablename__ = 'tbl_libro'

    id = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False)
    anio_publicacion = Column(Integer)

    autor_id = Column(Integer, ForeignKey('tbl_autor.id'))
    categoria_id = Column(Integer, ForeignKey('tbl_categoria.id'))

    autor = relationship("Autores", back_populates="libros")
    categoria = relationship("Categorias", back_populates="libros")

engine = create_engine('sqlite:///biblioteca.db', echo=True)

Base.metadata.create_all(engine)