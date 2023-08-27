import psycopg2
from bottle import route, run, request

DSN = 'dbname=trabalho1 user=postgres password=postgres host=db'


def resgister_resposta(respostas):

    SQL = f"INSERT INTO perguntas (respostas) VALUES ('{respostas}')"
    conn = psycopg2.connect(DSN)
    cur = conn.cursor()
    cur.execute(SQL)
    conn.commit()
    cur.close()
    conn.close()

    print('Resposta salva no banco!')

@route('/', method='POST')
def send():
    mensagem = request.forms.get('mensagem')
    

    gabarito = 'abb'
    # Converte a string para letras minúsculas para comparar independentemente de maiúsculas e minúsculas
    string = mensagem.lower()

    exibir = []

    x = 1
    if len(string) != len(gabarito):
        return 'Resposta inválida!'
    else:
        for i in range(len(string)):
            if string[i] == gabarito[i]:
                exibir.append(f'Resposta {x} CORRETA!\n')
                x += 1
            else:
                exibir.append(f'Resposta {x} INCORRETA!\n')
                x += 1
        
        resgister_resposta(string)
    
    return exibir

if __name__ == '__main__':
    run(host='0.0.0.0', port=8080, debug=True)