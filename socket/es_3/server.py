import socket
import tkinter
import threading

def avviaServer(textbox):
    HOST = "127.0.0.1"
    PORT = 5000
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen()
        textbox.insert(tkinter.END, "Server in ascolto...")
        textbox.see(tkinter.END)

        conn, addr = server.accept()
        with conn:
            textbox.insert(tkinter.END,f"Connessione da {addr}")
            textbox.see(tkinter.END)
            data = conn.recv(1024).decode()

            textbox.insert(tkinter.END, f"Messaggio ricevuto dal cliente: {data}")
            textbox.see(tkinter.END)

            risposta = "Messaggio ricevuto correttamente!"
            conn.sendall(risposta.encode())


# define tkinter window
root = tkinter.Tk()
root.title("Server Python")
frame = tkinter.Frame(root, padx=20, pady=20)
frame.pack()

# create textbox for text and make it read-only
textbox = tkinter.Text(root, width=50, height=10)
textbox.pack()
textbox.config(state=tkinter.NORMAL)

# create label for the header
label = tkinter.Label(frame, text="Risultati ricevuti")
label.pack()
threading.Thread(target=avviaServer, args=(textbox,), daemon=True).start()

root.mainloop()