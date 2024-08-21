import pyautogui
import time 

# Move para a posição do documento e clica duas vezes
pyautogui.move()
pyautogui.doubleClick(0,0)
for _ in range(10):

    # Marcar como lido
    pyautogui.move()
    pyautogui.click()
    pyautogui.press('esc')  # Sai da tela do documento

    # Aguarda
    time.sleep(1.0)

    # Mover dnv para a posição do documento e clica duas vezes
    pyautogui.move()
    pyautogui.doubleClick()

    # Aguarda
    time.sleep(1.0)

# Atualiza pagina fora do loop
pyautogui.press('f5')

time.sleep(1.2)

# Muda aba no chrome
pyautogui.keyDown('ctrl')
pyautogui.press(['tab'])
pyautogui.keyUp('ctrl')