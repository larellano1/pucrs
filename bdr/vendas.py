import sqlalchemy as sa
import sqlalchemy.orm as orm
import datetime

engine = sa.create_engine("sqlite:///vendas.db")

base = orm.declarative_base()

#Table clientes
class clientes(base):
    __tablename__ = "clientes"
    cpf = sa.Column(sa.CHAR(14), primary_key=True, index=True)
    nome = sa.Column(sa.VARCHAR(100), nullable=False)
    email = sa.Column(sa.VARCHAR(50))
    genero = sa.Column(sa.VARCHAR(1))
    salario = sa.Column(sa.DECIMAL(10,2))
    dia_mes_aniversario = sa.Column(sa.CHAR(5))

class produtos(base):
    __tablename__ = "produtos"
    cod_barras = sa.Column(sa.CHAR(10), primary_key=True, index=True)
    descricao = sa.Column(sa.VARCHAR(100), nullable=False)

class vendas(base):
    __tablename__ = "vendas"
    id_venda = sa.Column(sa.INTEGER, primary_key=True, index=True)
    dia_venda = sa.Column(sa.DATETIME, default=datetime.date.today())
    cliente = sa.Column(sa.CHAR(14), sa.ForeignKey("clientes.cpf"), onupdate="CASCADE")
    produto = sa.Column(sa.CHAR(10), sa.ForeignKey("produtos.cod_barras"), onupdate="CASCADE")
try:
    base.metadata.create_all(engine)
    print("Tabelas criadas")
except ValueError:
    ValueError()

#Create a code that inserts a new client in the database
def insert_client(cpf, nome, email, genero, salario, dia_mes_aniversario):
    session = orm.sessionmaker(bind=engine)()
    cliente = clientes(cpf=cpf, nome=nome, email=email, genero=genero, salario=salario, dia_mes_aniversario=dia_mes_aniversario)
    session.add(cliente)
    session.commit()
    session.close()

#Use the function to insert a new client
insert_client("123.456.789-00", "João da Silva", "joao@gmail.com", "M", 1000.00, "01/01")