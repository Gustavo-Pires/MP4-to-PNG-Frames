import cv2
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def processar_video():
    # Obtenha o arquivo de vídeo selecionado 
    video_filename = filedialog.askopenfilename(filetypes=[("Arquivos de vídeo", "*.mp4")])

    if not video_filename:
        return

    # Nome do diretório para salvar os frames
    output_directory = os.path.join(os.path.dirname(video_filename), 'frames_output')

    # Crie o diretório se ele não existir
    os.makedirs(output_directory, exist_ok=True)

    # Abra o arquivo de vídeo
    cap = cv2.VideoCapture(video_filename)

    # Verifique se o vídeo foi aberto corretamente
    if not cap.isOpened():
        messagebox.showerror("Erro", "Erro ao abrir o arquivo de vídeo.")
        return

    # Taxa de quadros por segundo (FPS) do vídeo
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    # Duração do vídeo em segundos
    duration = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) // fps

    # Nome base para os frames
    base_name = os.path.splitext(os.path.basename(video_filename))[0]

    # Loop para ler e salvar cada frame
    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Nome do arquivo de saída para o frame atual
        frame_filename = f'{base_name}_{frame_count+1:02d}.png'

        # Caminho completo para o arquivo de saída
        output_path = os.path.join(output_directory, frame_filename)

        # Salvar o frame como uma imagem
        cv2.imwrite(output_path, frame)

        frame_count += 1

    # Libere o objeto de captura de vídeo
    cap.release()

    messagebox.showinfo("Concluído", f'Processamento concluído. {frame_count} frames salvos em {duration} segundos.')

# Crie a janela principal
root = tk.Tk()
root.title("Processador de Vídeo")

# Botão para selecionar o arquivo de vídeo e processá-lo
process_button = tk.Button(root, text="Selecionar Arquivo de Vídeo", command=processar_video)
process_button.pack(pady=20)

# Inicie a interface gráfica
root.mainloop()
