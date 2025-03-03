import socket

def play_game():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)
    client_socket.connect(server_address)

    while True:
        emoji_title = client_socket.recv(1024).decode()

        if not emoji_title:
            break

        print(f"Guess the song title: {emoji_title}")

        guess = input("Your guess: ")
        client_socket.send(guess.encode())

        response = client_socket.recv(1024).decode()
        print(response)

    client_socket.close()

if __name__ == '__main__':
    play_game()
