class TV:
    _numTV = 0

    def __init__(self, marca, estado):
        self._marca = marca
        self._canal = 1
        self._precio = 500
        self._estado = estado
        self._volumen = 1
        self._control = None
        TV._numTV += 1

    # Setters
    def setMarca(self, marca):
        self._marca = marca

    def setControl(self, control):
        self._control = control

    def setPrecio(self, precio):
        self._precio = precio

    def setVolumen(self, volumen):
        if self.getEstado():
            if volumen >= 0 and volumen <= 7:
                if self._volumen >= 0 and self._volumen <= 7:
                    self._volumen = volumen

    def setCanal(self, canal):
        if self.getEstado():
            if canal >= 0 and canal <= 120:
                if self._canal >= 0 and self._canal <= 120:
                    self._canal = canal

    @classmethod
    def setNumTV(cls, numTV):
        cls._numTV = numTV

    # Getters
    def getMarca(self):
        return self._marca

    def getControl(self):
        return self._control

    def getPrecio(self):
        return self._precio

    def getEstado(self):
        return self._estado

    def getVolumen(self):
        return self._volumen

    def getCanal(self):
        return self._canal

    @classmethod
    def getNumTV(cls):
        return cls._numTV

    # Metodos
    def turnOn(self):
        self._estado = True

    def turnOff(self):
        self._estado = False

    def canalUp(self):
        if self.getEstado():
            if self._canal < 120:
                self._canal += 1

    def canalDown(self):
        if self.getEstado():
            if self._canal > 0:
                self._canal -= 1

    def volumenUp(self):
        if self.getEstado():
            if self._volumen < 7:
                self._volumen += 1

    def VolumenDown(self):
        if self.getEstado():
            if self._volumen > 0:
                self._volumen -= 1
