import pyautogui
import time

# Define o tamanho do lado do quadrado
lado_quadrado = 100

# Obtém as dimensões da tela
largura_tela, altura_tela = pyautogui.size()

# Calcula as coordenadas dos quatro cantos do quadrado
canto_superior_esquerdo = (largura_tela // 2 - lado_quadrado // 2, altura_tela // 2 - lado_quadrado // 2)
canto_superior_direito = (largura_tela // 2 + lado_quadrado // 2, altura_tela // 2 - lado_quadrado // 2)
canto_inferior_direito = (largura_tela // 2 + lado_quadrado // 2, altura_tela // 2 + lado_quadrado // 2)
canto_inferior_esquerdo = (largura_tela // 2 - lado_quadrado // 2, altura_tela // 2 + lado_quadrado // 2)

# Define a velocidade de movimento do cursor (em segundos)
velocidade_movimento = 0.5

# Loop infinito para mover o cursor em formato de quadrado
while True:
    for destino in [canto_superior_direito, canto_inferior_direito, canto_inferior_esquerdo, canto_superior_esquerdo]:
        pyautogui.moveTo(destino[0], destino[1], duration=velocidade_movimento)
        time.sleep(0.5)
