from flask import Flask, render_template, request, redirect # Importa o Flask e outras funções necessárias

app = Flask(__name__) # Inicializa a aplicação Flask

# Rota para a página inicial
@app.route("/")
def index():
    return render_template("index.html") # Renderiza o template HTML da página de lançamento de notas

# Rota para validar e salvar as notas no arquivo
@app.route("/validar_notas", methods=['POST'])
def validar_notas():
    nome_do_aluno = request.form["nome_do_aluno"] # Obtém o nome do aluno do formulário
    nota_1 = request.form["nota_1"] # Obtém a primeira nota do formulário
    nota_2 = request.form["nota_2"] # Obtém a segunda nota do formulário
    nota_3 = request.form["nota_3"] # Obtém a terceira nota do formulário

    # Caminho para o arquivo de texto onde as notas serão salvas
    caminho_arquivo = 'models/notas.txt'
    with open(caminho_arquivo, 'a') as arquivo: # Abre o arquivo no modo de adição
        arquivo.write(f"{nome_do_aluno};{nota_1};{nota_2};{nota_3}\n") # Escreve os dados no arquivo

    return redirect("/") # Redireciona de volta para a página inicial

# Rota para consultar as notas
@app.route("/consulta")
def consulta_notas():
    notas = [] # Lista para armazenar as notas dos alunos
    caminho_arquivo = 'models/notas.txt' # Define o caminho do arquivo de notas
    
    # Abre o arquivo de notas para leitura
    with open(caminho_arquivo, 'r') as arquivo:
        for linha in arquivo: # Itera sobre cada linha do arquivo
            item = linha.strip().split(';') # Separa os dados da linha por ponto e vírgula
            # Calcula a média das três notas e arredonda para 2 casas decimais
            media = round((float(item[1]) + float(item[2]) + float(item[3])) / 3, 2)
            # Define o status como "Aprovado" se a média for maior ou igual a 7, caso contrário "Reprovado"
            status = 'Aprovado' if media >= 7 else 'Reprovado'
            
            # Adiciona os dados à lista de notas
            notas.append({
                'nome': item[0], # Nome do aluno
                'nota_1': item[1], # Primeira nota
                'nota_2': item[2], # Segunda nota
                'nota_3': item[3], # Terceira nota
                'media': media, # Média calculada
                'status': status # Status do aluno (Aprovado/Reprovado)
            })
    
    return render_template("consulta.html", notas=notas) # Renderiza o template de consulta com os dados das notas

# Inicia a aplicação Flask
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=80, debug=True) # Executa o servidor na porta 80, modo debug ativado
