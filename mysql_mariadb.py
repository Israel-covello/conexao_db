import pymysql.cursors
from contextlib import contextmanager


@contextmanager
def conect():
    """Função para conectar com a base de dados"""
    #Confg. da conexão com a BD e com servidor no caso utilizei o XAMPP
    conexao = pymysql.connect(
        #Localhost
        host='127.0.0.1',
        #Usuário config. do servidor
        user='root',
        #Password config. do servidor
        password='',
        #Base de dados
        db='clientes',
        #Config. de caracteres
        charset='utf8mb4',
        #Modo de exibição do cursor, no caso exibirá como dicionário
        cursorclass=pymysql.cursors.DictCursor
    )

    """Conexão automatica"""
    try:
        yield conexao
    finally:
        conexao.close()


#Gerenciador de contexto "with" para fechar conexão e a conexão com cursor automaticamente.
#Todos os comandos SQL usará os dois primeiros comandos com o with.
with conect() as conexao:
    with conexao.cursor() as cursor:
        cursor.execute('SELECT * FROM clientes ORDER BY id DESC LIMIT 50')
        resultado = cursor.fetchall()

        for linha in resultado:
            print(linha)
