import socket
import random

# Δημιουργία socket για τον server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Σύνδεση στη θύρα 12345
server_socket.bind(('localhost', 12345))
server_socket.listen(1)

print("Ο server ακούει στη θύρα 12345...")

# Περιμένουμε τον client να συνδεθεί
client_socket, addr = server_socket.accept()
print(f"Σύνδεση από {addr}")

# Ο server επιλέγει έναν τυχαίο αριθμό
target_number = random.randint(1, 100)
print(f"Ο σωστός αριθμός είναι: {target_number}")

# Ξεκινάμε το παιχνίδι
while True:
    # Λήψη της εικασίας από τον client
    data = client_socket.recv(1024).decode('utf-8')
    print(f"Ο client έστειλε: {data}")

    if data == "*#0#*":
        print("Λήφθηκε η εντολή εξόδου. Κλείσιμο σύνδεσης.")
        break

    # Μετατροπή της εισόδου του client σε ακέραιο αριθμό
    guess = int(data)

    # Έλεγχος της εικασίας
    if guess < target_number:
        client_socket.send("Ο αριθμός σου είναι μικρότερος.".encode('utf-8'))
    elif guess > target_number:
        client_socket.send("Ο αριθμός σου είναι μεγαλύτερος.".encode('utf-8'))
    else:
        client_socket.send("Σωστά! Βρήκες τον αριθμό.".encode('utf-8'))
        break

client_socket.close()  # Κλείνουμε τη σύνδεση με τον client
server_socket.close()  # Κλείνουμε το socket του server