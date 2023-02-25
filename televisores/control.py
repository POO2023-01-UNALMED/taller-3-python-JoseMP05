class Control:
    def __init__(self):
        pass

    # Setters
    def setTv(self, tv):
        self._tv = tv

    # Getters
    def getTv(self):
        return self._tv

    # Metodos
    def enlazar(self, tv):
        self._tv = tv
        tv.setControl(self)

    def turnOn(self):
        self._tv.turnOn()

    def turnOff(self):
        self._tv.turnOff()

    def canalUp(self):
        self._tv.canalUp()

    def canalDown(self):
        self._tv.canalDown()

    def setCanal(self, canal):
        self._tv.setCanal(canal)

    def volumenUp(self):
        self._tv.volumenUp()

    def volumenDown(self):
        self._tv.voluemenDown()
