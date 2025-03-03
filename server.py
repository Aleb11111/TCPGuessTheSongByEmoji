import socket
import threading
import random

SONG_TITLES = {
    "🕒🔙": "Back In Time",
    "🆕📐📏" : "New Rules",
    "🙋🏼➡⛪" : "Take Me To Church",
    "🎉🥳 USA":"Party In The USA",
    "💍💍💍💍💍💍💍":"7 Rings",
    "⚫🤔⚪":"Black or White",
    "☎🤔":"Call Me Maybe",
    "🔮🏪" : "Magic Shop"

}

def handle_client(client_socket):
    try:
        questions = list(SONG_TITLES.keys())
        random.shuffle(questions)

        correct_answers = 0

        for emoji_title in questions:
            actual_title = SONG_TITLES[emoji_title]
            client_socket.send(emoji_title.encode())

            guess = client_socket.recv(1024).decode()

            if guess.lower() == actual_title.lower():
                client_socket.send("Correct! 🎉".encode())
                correct_answers += 1
            else:
                client_socket.send(f"Wrong! The title was {actual_title}".encode())

        # Send summary feedback
        feedback = f"You got {correct_answers} out of {len(questions)} questions correct. Well done!"
        client_socket.send(feedback.encode())

    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)
    server_socket.listen(5)
    print('Server is running...')

    while True:
        client_socket, client_address = server_socket.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == '__main__':
    start_server()
