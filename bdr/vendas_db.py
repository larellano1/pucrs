import sqlalchemy as sa
import sqlalchemy.orm as orm
import datetime
import pandas as pd

#Create the database
engine = sa.create_engine("sqlite:///vendas.db")

#Create the tables
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

#Table produtos
class produtos(base):
    __tablename__ = "produtos"
    cod_barras = sa.Column(sa.CHAR(10), primary_key=True, index=True)
    descricao = sa.Column(sa.VARCHAR(100), nullable=False)

#Table vendas
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

#Functions to insert data in the database

#Create a code that inserts a new client in the database
def insert_client(cpf, nome, email, genero, salario, dia_mes_aniversario):
    session = orm.sessionmaker(bind=engine)()
    cliente = clientes(cpf=cpf, nome=nome, email=email, genero=genero, salario=salario, dia_mes_aniversario=dia_mes_aniversario)
    session.add(cliente)
    session.commit()
    session.close()

#Create a function that inserts several clients in the database from a cvs file
def insert_clients_from_file(file):
    session = orm.sessionmaker(bind=engine)()
    with open(file, "r") as f:
        for line in f:
            cpf, nome, email, genero, salario, dia_mes_aniversario = line.split(";")
            cliente = clientes(cpf=cpf, nome=nome, email=email, genero=genero, salario=salario, dia_mes_aniversario=dia_mes_aniversario)
            session.add(cliente)
    session.commit()
    session.close()

#Create a function that inserts products in the database from a Pandas Dataframe, using sa.Table
def insert_products_from_dataframe(df):
    session = orm.sessionmaker(bind=engine)()
    df.to_sql("produtos", con=engine, if_exists="append", index=False)
    session.commit()
    session.close()

#Create a function that inserts vendas in the database
def insert_venda(dia_venda, cliente, produto):
    session = orm.sessionmaker(bind=engine)()
    venda = vendas(dia_venda=dia_venda, cliente=cliente, produto=produto)
    session.add(venda)
    session.commit()
    session.close()

#Functions to update data from the database

#Create function to update the product description by the product code
def update_product_description(cod_barras, descricao):
    session = orm.sessionmaker(bind=engine)()
    produtos = sa.Table("produtos", base.metadata, autoload=True, autoload_with=engine)
    query = sa.update(produtos).where(produtos.columns.cod_barras == cod_barras).values(descricao=descricao)
    session.execute(query)
    session.commit()
    session.close()

########## USE CASES FOR THE ABOVE FUNCTIONS ##########

#Insert 3 diferent products in the database
try:
    insert_products_from_dataframe(pd.DataFrame({"cod_barras": ["1234567890", "0987654321", "1234567891"], "descricao": ["Produto 1", "Produto 2", "Produto 3"]}))
except ValueError:
    ValueError() 
    
#Use the function to insert a new client
try:
    insert_client("123.456.789-99", "João da Silva", "joao@gmail.com", "M", 1000.00, "01/01")
except ValueError:
    ValueError()

#Use the function to insert clients from csv file
try:
    insert_clients_from_file("clientes.csv")
except ValueError:
    ValueError()
  
#Insert a new venda
try:
    insert_venda(datetime.datetime.now(), "123.456.789-99", "1234567890")
except ValueError:
    ValueError()

