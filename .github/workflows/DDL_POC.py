import sqlalchemy as sa
from sqlalchemy import text
from sqlalchemy.schema import CreateTable
from sqlalchemy import  MetaData, Table, Column, Integer, String
import pyodbc

print(pyodbc.drivers())

# engine = sa.create_engine('mssql+pyodbc://DESKTOP-68IH9E2\SQLEXPRESS/API?driver=SQL+Server+Native+Client+11.0')

# sql=text('drop table if exists dbo.test')

# with engine.connect().execution_options(isolation_level="AUTOCOMMIT") as con:

#     con.execute(sql)


# con.close()