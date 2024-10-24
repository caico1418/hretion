def mover_frame(frame, direction):
    """Mueve el frame en la dirección especificada (izquierda o derecha)."""
    step_size = 10  # Tamaño del paso en píxeles
    if direction == 'derecha':
        target_x = 500  # Mueve a la derecha
    elif direction == 'izquierda':
        target_x = 0  # Mueve a la izquierda

    def move():
        nonlocal target_x
        current_x = frame.winfo_x()
        if current_x < target_x:
            new_x = current_x + step_size
            frame.place(x=new_x, y=frame.winfo_y())
            frame.lift()
            frame.after(10, move)  # Llama recursivamente para mover de forma suave
        elif current_x > target_x:
            new_x = current_x - step_size
            frame.place(x=new_x, y=frame.winfo_y())
            frame.after(10, move)
        else:
            frame.place(x=target_x, y=frame.winfo_y())  # Asegurarse que el frame esté en su destino final
            frame.animacion_final()

    move()

def animacion_final(frame):
    frame.label_question.pack_forget()
