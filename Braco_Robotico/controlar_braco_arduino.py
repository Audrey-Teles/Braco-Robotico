from conexao_arduino import ArduinoConexao
import pyautogui as p

arduino = ArduinoConexao("COM4")

while True:

    porcentagem_posicao = 100 - ((100 * p.position().y) / 1080)
    angulo_servo = str((int((porcentagem_posicao / 100) * 90)))

    arduino.setangulo(angulo_servo)
    print(arduino.getlines())


