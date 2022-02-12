import serial as s


class ArduinoConexao:

    def __init__(self, porta: str):
        self.porta = porta
        self.conexao = self.setconexao()

    def setconexao(self):
        return s.Serial(self.porta, 9600)

    def setangulo(self, angulo: str):
        self.conexao.write(bytes(angulo, "utf-8"))

    def getlines(self) -> str:
        return str(self.conexao.readline().decode())
