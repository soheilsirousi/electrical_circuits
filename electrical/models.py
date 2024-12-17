
class Mesh:
    ID = 0

    def __init__(self):
        self.id = Mesh.ID
        self.__VoltageSources = dict()
        self.__Resistances = dict()
        self.__CurrentSources = dict()
        Mesh.ID += 1

    @property
    def VoltageSources(self):
        return self.__VoltageSources

    @property
    def Resistances(self):
        return self.__Resistances

    @property
    def CurrentSources(self):
        return self.__CurrentSources

    @VoltageSources.setter
    def VoltageSources(self, value):
        self.__VoltageSources.update(value)

    @Resistances.setter
    def Resistances(self, value):
        self.__Resistances.update(value)

    @CurrentSources.setter
    def CurrentSources(self, value):
        self.__CurrentSources.update(value)

    def Ammeter(self):
        voltages = 0
        resistances = 0
        for v in self.VoltageSources.values():
            voltages += v
        for r in self.Resistances.values():
            resistances += r

        return str(voltages / resistances) + "A"


class Circuit:

    def __init__(self):
        self.Meshes = list()
