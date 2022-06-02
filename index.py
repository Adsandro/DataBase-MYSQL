import mysql.connector

# criação da conexão
conexao = mysql.connector.connect (
    host = 'localhost', #Local onde esta guardado o banco de dados, nesse caso esta no local host, porem pode ser um link ou até mesmo um ip
    user = 'root',
    password = 'Dede01122002!',
    database = 'hashtag',
)
cursor = conexao.cursor()

# CRUD
idVendas = 3
comando = f'DELETE FROM vendas WHERE idVendas = 3' #Manda o comando em SQL 
cursor.execute(comando)
conexao.commit() #Edita o banco de dados



#Encerrar todo o processo
cursor.close()
conexao.close()


#CREATE 
# nome_produto = "chocolate"
# valor = 16
# comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})' #Manda o comando em SQL 
# cursor.execute(comando)
# conexao.commit( )#Edita o banco de dados


#READ 
# comando = f'SELECT * FROM vendas;' #Manda o comando em SQL 
# cursor.execute(comando)
# resultado = cursor.fetchall() #Lendo o banco de dados
# print(resultado)


#UPDATE
# valor = 6
# nome_produto = "Todynho"
# comando = f'UPDATE vendas set valor = {valor} WHERE nome_produto  = "{nome_produto}"' #Manda o comando em SQL 
# cursor.execute(comando)
# conexao.commit() #Edita o banco de dados


#DELETE 
# idVendas = 3
# comando = f'DELETE FROM vendas WHERE idVendas = 3' #Manda o comando em SQL 
# cursor.execute(comando)
# conexao.commit() #Edita o banco de dados
