import socket

# Definindo as questões e respostas corretas
questions = [
    {"question": "Qual é a capital da França?", "options": ["a) Paris", "b) Londres", "c) Roma"], "correct_answer": "a"},
    {"question": "Quem pintou a Mona Lisa?", "options": ["a) Van Gogh", "b) Leonardo da Vinci", "c) Pablo Picasso"], "correct_answer": "b"},
    {"question": "Qual é o maior planeta do Sistema Solar?", "options": ["a) Terra", "b) Júpiter", "c) Marte"], "correct_answer": "b"}
]

def handle_client(client_socket):
    correct_answers = 0
    answers_feedback = []

    for question in questions:
        # Enviar a pergunta para o cliente
        question_text = question["question"] + "\n" + "\n".join(question["options"]) + "\nResposta: "
        client_socket.sendall(question_text.encode())

        # Receber a resposta do cliente
        client_response = client_socket.recv(1024).decode().strip().lower()

        # Verificar se a resposta está correta
        if client_response == question["correct_answer"]:
            correct_answers += 1
            answers_feedback.append("Correta")
        else:
            answers_feedback.append("Incorreta")

    # Enviar a contagem de respostas corretas e o feedback das respostas
    result = f"Você acertou {correct_answers} questões de um total de {len(questions)}.\n"
    result += "\n".join([f"Questão {i+1}: {feedback}" for i, feedback in enumerate(answers_feedback)])
    client_socket.sendall(result.encode())

    client_socket.close()

def main():
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()

    print(f"Servidor ouvindo em {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Conexão estabelecida com {client_address}")
        handle_client(client_socket)

if __name__ == "__main__":
    main()