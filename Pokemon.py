class Pokemon:
    def __init__(self,img, id, name,gen, types : list, total, hp, attack, defense, spAtk, spDef, speed):
        self.img = img
        self.id = id
        self.name = name
        self.gen = gen
        self.types = types
        self.total = total
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.spAtk = spAtk
        self.spDef = spDef
        self.speed = speed

    # @classmethod
    # def from_array(cls, arr):
    #     if len(arr) == 9:
    #         id, name, types, total, hp, attack, defense, spAtk, spDef, speed = arr
    #         return cls(id, name, types, int(total), int(hp), int(attack), int(defense), int(spAtk), int(spDef),int(speed))
    #     else:
    #         raise ValueError("El array debe contener 9 elementos para crear un Pokémon.")

    @classmethod
    def from_array(cls, arr):
        if len(arr) == 11:
            img, id, name,gen, types, total, hp, attack, defense, spAtk, spDef, speed = arr
            print(types)
            return cls(img, id, name,gen, types, int(total), int(hp), int(attack), int(defense), int(spAtk), int(spDef),int(speed))
        else:
            raise ValueError("El array debe contener 9 elementos para crear un Pokémon.")
        
    def compare(self, other):
        results = []
        if self.types == other.types:
            results.append("=")
        else:
            for t in self.types:
                if(t in other.types):
                    results.append("~")
                    break
            else:      
                results.append("!=")

        if self.total == other.total:
            results.append("=")
        elif self.total > other.total:
            results.append(">")
        else:
            results.append("<")

        if self.hp == other.hp:
            results.append("=")
        elif self.hp > other.hp:
            results.append(">")
        else:
            results.append("<")

        if self.attack == other.attack:
            results.append("=")
        elif self.attack > other.attack:
            results.append(">")
        else:
            results.append("<")

        if self.defense == other.defense:
            results.append("=")
        elif self.defense > other.defense:
            results.append(">")
        else:
            results.append("<")

        if self.spAtk == other.spAtk:
            results.append("=")
        elif self.spAtk > other.spAtk:
            results.append(">")
        else:
            results.append("<")

        if self.spDef == other.spDef:
            results.append("=")
        elif self.spDef > other.spDef:
            results.append(">")
        else:
            results.append("<")
        
        if self.speed == other.speed:
            results.append("=")
        elif self.speed > other.speed:
            results.append(">")
        else:
            results.append("<")
        return results
    
    def __str__(self):
        return f'''{self.name}
        ID              : {self.id}
        Type(s)         : {self.types}
        Gen             : {self.gen}
        Total           : {self.total}
        HP              : {self.hp}
        Attack          : {self.attack}
        Defense         : {self.defense}
        Special Attack  : {self.spAtk}
        Special Defense : {self.spDef}
        Speed           : {self.speed}
        \n'''
    def mostrar(self):
        return f"{self.name} {self.id} {self.types} {self.total} {self.hp} {self.attack} {self.defense} {self.spAtk} {self.spDef} {self.speed}"
        

