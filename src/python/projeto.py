import oracledb

ORACLE_DSN = "[USUARIO]/[SENHA]@oracle.fiap.com.br:1521/ORCL"

try:
    connection = oracledb.connect(ORACLE_DSN)
    cursor = connection.cursor()
except oracledb.DatabaseError as e:
    print(f"Erro ao conectar ao banco de dados: {e}")
    exit(1)

def validar_entrada(dados):
    try:
        umidade = float(dados[0])
        temperatura = float(dados[1])
        nivel_p = int(dados[2])
        nivel_k = int(dados[3])
        ph = float(dados[4])
        bomba_estado = int(dados[5])
        return umidade, temperatura, nivel_p, nivel_k, ph, bomba_estado
    except (ValueError, IndexError):
        print("Entrada inválida. Certifique-se de inserir os dados corretamente.")
        return None

# Função para inserir dados no banco de dados
def create_data(umidade, temperatura, nivel_p, nivel_k, ph, bomba_estado):
    cursor.execute('''
        INSERT INTO sensor_data (umidade, temperatura, nivel_p, nivel_k, ph, bomba_estado)
        VALUES (:umidade, :temperatura, :nivel_p, :nivel_k, :ph, :bomba_estado)
    ''', umidade=umidade, temperatura=temperatura, nivel_p=nivel_p, nivel_k=nivel_k, ph=ph, bomba_estado=bomba_estado)
    connection.commit()

# Função para listar todos os dados do banco de dados
def read_data():
    cursor.execute('SELECT * FROM sensor_data')
    rows = cursor.fetchall()
    if not rows:
        print("Nenhum dado encontrado.")
    else:
        headers = ["ID", "Umidade", "Temperatura", "Nível P", "Nível K", "pH", "Bomba Estado", "Timestamp"]
        print(f"{headers[0]:<5} {headers[1]:<10} {headers[2]:<12} {headers[3]:<10} {headers[4]:<10} {headers[5]:<5} {headers[6]:<12} {headers[7]:<20}")
        print("-" * 100)
        for row in rows:
            timestamp = row[7].strftime("%Y-%m-%d %H:%M:%S")
            bomba_estado = "Ligada" if row[6] == 1 else "Desligada"
            print(f"{row[0]:<5} {row[1]:<10} {row[2]:<12} {row[3]:<10} {row[4]:<10} {row[5]:<5} {bomba_estado:<12} {timestamp:<20}")

# Função para atualizar dados no banco de dados
def update_data(id, umidade, temperatura, nivel_p, nivel_k, ph, bomba_estado):
    cursor.execute('''
        UPDATE sensor_data
        SET umidade = :umidade, temperatura = :temperatura, nivel_p = :nivel_p, nivel_k = :nivel_k, ph = :ph, bomba_estado = :bomba_estado
        WHERE id = :id
    ''', id=id, umidade=umidade, temperatura=temperatura, nivel_p=nivel_p, nivel_k=nivel_k, ph=ph, bomba_estado=bomba_estado)
    connection.commit()

# Função para deletar dados no banco de dados
def delete_data(id):
    cursor.execute('DELETE FROM sensor_data WHERE id = :id', id=id)
    connection.commit()

# Menu interativo
while True:
    print("\n")
    print("Menu:")
    print("1. Inserir dados")
    print("2. Listar dados")
    print("3. Atualizar dados")
    print("4. Deletar dados")
    print("5. Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        entrada = input("Digite os dados (umidade, temperatura, nivel_p, nivel_k, ph, bomba_estado) separados por vírgula: ")
        dados = entrada.split(',')
        valores = validar_entrada(dados)
        if valores:
            umidade, temperatura, nivel_p, nivel_k, ph, bomba_estado = valores
            create_data(umidade, temperatura, nivel_p, nivel_k, ph, bomba_estado)
    elif escolha == '2':
        read_data()
    elif escolha == '3':
        id = input("Digite o ID do registro a ser atualizado: ")
        if id.isdigit():
            id = int(id)
            entrada = input("Digite os novos dados (umidade, temperatura, nivel_p, nivel_k, ph, bomba_estado) separados por vírgula: ")
            dados = entrada.split(',')
            valores = validar_entrada(dados)
            if valores:
                umidade, temperatura, nivel_p, nivel_k, ph, bomba_estado = valores
                update_data(id, umidade, temperatura, nivel_p, nivel_k, ph, bomba_estado)
        else:
            print("ID inválido. Certifique-se de inserir um número inteiro.")
    elif escolha == '4':
        id = input("Digite o ID do registro a ser deletado: ")
        if id.isdigit():
            id = int(id)
            delete_data(id)
        else:
            print("ID inválido. Certifique-se de inserir um número inteiro.")
    elif escolha == '5':
        break
    else:
        print("Opção inválida. Tente novamente.")

# Fechamento da conexão com o banco de dados
cursor.close()
connection.close()