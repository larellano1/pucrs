import sqlalchemy as sa
import sqlalchemy.orm as orm
import datetime

engine = sa.create_engine("sqlite:///vendas.db")

base = orm.declarative_base()

#Table clientes
class cliente(base):
    __tablename__ = "clientes"
    cpf = sa.Column(sa.CHAR(14), primary_key=True, index=True)
    nome = sa.Column(sa.VARCHAR(100), nullable=False)
    email = sa.Column(sa.VARCHAR(50))
    genero = sa.Column(sa.VARCHAR(1))
    salario = sa.Column(sa.DECIMAL(10,2))
    dia_mes_aniversario = sa.Column(sa.CHAR(5))

class produto(base):
    __tablename__ = "produtos"
    cod_barras = sa.Column(sa.CHAR(10), primary_key=True, index=True)
    descricao = sa.Column(sa.VARCHAR(100), nullable=False)

class vendas(base):
    __tablename__ = "vendas"
    dia_venda = sa.Column(sa.DATETIME, default=datetime.date.today())
    cliente = sa.Column(sa.CHAR(14), sa.ForeignKey("clientes.cpf"),ondelete="NO ACTION", onupdate="CASCADE")
    produto = sa.Column(sa.CHAR(10), onupdate="CASCADE", ondelete="NO ACTION")