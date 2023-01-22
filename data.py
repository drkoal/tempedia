import json

class Data:

    def loadData(self):
        self.__loadTemtems()
        self.__loadConditions()
        self.__loadTechniques()
        self.__loadTraits()
        self.__loadWeaknesses()

    def __loadTemtems(self):
        f = open(r'resources/data/temtem.json')
        self.temtems = json.load(f)

    def __loadConditions(self):
        f = open(r'resources/data/conditions.json')
        self.conditions = json.load(f)

    def __loadTechniques(self):
        f = open(r'resources/data/techniques.json')
        self.techniques = json.load(f)

    def __loadTraits(self):
        f = open(r'resources/data/traits.json')
        self.traits = json.load(f)

    def __loadWeaknesses(self):
        f = open(r'resources/data/weaknesses.json')
        self.weaknesses = json.load(f)

    def getTemtemByName(self, name):
        for temtem in self.temtems:
            if temtem['name']==name.capitalize(): return temtem
        return None

    def getWeaknessesByType(self, type):
        return self.weaknesses[type.capitalize()]

    def getWeaknessByTemtem(self, name):
        temtem = self.getTemtemByName(name)
        types = temtem['types']

        result = self.getWeaknessesByType(types[0])
        result['Neutral'] = 1
        result['Wind'] = 1
        result['Earth'] = 1
        result['Water'] = 1
        result['Fire'] = 1
        result['Nature'] = 1
        result['Electric'] = 1
        result['Mental'] = 1
        result['Digital'] = 1
        result['Melee'] = 1
        result['Crystal'] = 1
        result['Toxic'] = 1

        for x in types:
            for type in self.weaknesses:
                result[type] *= self.getWeaknessesByType(type)[x]

        return result





