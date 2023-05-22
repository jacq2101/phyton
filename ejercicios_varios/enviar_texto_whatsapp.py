import tkinter as tk
import webbrowser

def open_whatsapp():
    phone_number = phone_entry.get()
    message = message_entry.get()
    whatsapp_url = f"https://api.whatsapp.com/send?phone={phone_number}&text={message}"
    webbrowser.open(whatsapp_url)

# Crear la ventana de la aplicación
window = tk.Tk()
window.title("Enviar Mensaje de WhatsApp")
window.geometry("300x200")

# Etiqueta y campo de entrada para el número de teléfono
phone_label = tk.Label(window, text="Número de Teléfono (10 dígitos):")
phone_label.pack()
phone_entry = tk.Entry(window)
phone_entry.pack()

# Etiqueta y campo de entrada para el mensaje
message_label = tk.Label(window, text="Mensaje:")
message_label.pack()
message_entry = tk.Entry(window)
message_entry.pack()

# Botón para abrir WhatsApp y enviar el mensaje
send_button = tk.Button(window, text="Enviar", command=open_whatsapp)
send_button.pack()

# Ejecutar la aplicación
window.mainloop()
