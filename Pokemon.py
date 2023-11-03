class Pokemon:
    def __init__(self,img, id, name,gen, types : list, total, hp, attack, defense, spAtk, spDef, speed):
        self.img        = img
        self.id         = id
        self.name       = name
        self.gen        = gen
        self.types      = types
        self.total      = int(total)
        self.hp         = int(hp)
        self.attack     = int(attack)
        self.defense    = int(defense)
        self.spAtk      = int(spAtk)
        self.spDef      = int(spDef)
        self.speed      = int(speed)

    # @classmethod
    # def from_array(cls, arr):
    #     if len(arr) == 11:
    #         img, id, name,gen, types, total, hp, attack, defense, spAtk, spDef, speed = arr
    #         #print(types)
    #         if len(types) == 1:
    #             list(types).append('None')
                
    #         return cls(img, id, name,gen, types, int(total), int(hp), int(attack), int(defense), int(spAtk), int(spDef),int(speed))
    #     else:
    #         raise ValueError("El array debe contener 11 elementos para crear un Pokémon.")
        
    def compare(self, other):
        results = []
        if self.types[0] == other.types[0]:
            results.append("=")
        else:
            results.append("!=")
        if self.types[1] == other.types[1]:
            results.append("=")
        else:
            results.append("!=")
        

        if self.total == other.total:
            results.append("=")
        elif self.total > other.total:
            #print("1Secreto mayor", self.total , other.total)
            results.append("↑")
        else:
            results.append("↓")

        if self.hp == other.hp:
            results.append("=")
        elif self.hp > other.hp:
            #print("2Secreto mayor", self.hp ,other.hp)
            
            results.append("↑")
        else:
            results.append("↓")

        if self.attack == other.attack:
            results.append("=")
        elif self.attack > other.attack:
            #print("3Secreto mayor", self.attack ,other.attack)
            
            results.append("↑")
        else:
            results.append("↓")

        if self.defense == other.defense:
            results.append("=")
        elif self.defense > other.defense:
            #print("4Secreto mayor", self.defense , other.defense)
            
            results.append("↑")
        else:
            results.append("↓")

        if self.spAtk == other.spAtk:
            results.append("=")
        elif self.spAtk > other.spAtk:
            #print("5Secreto mayor",self.spAtk , other.spAtk)
            
            results.append("↑")
        else:
            results.append("↓")

        if self.spDef == other.spDef:
            results.append("=")
        elif self.spDef > other.spDef:
            #print("6Secreto mayor",self.spDef , other.spDef)
            
            results.append("↑")
        else:
            results.append("↓")
        
        if self.speed == other.speed:
            results.append("=")
        elif self.speed > other.speed:
            
            #print("7Secreto mayor", self.speed , other.speed)
            
            results.append("↑")
        else:
            results.append("↓")
        
        if int(self.gen[-1]) == int(other.gen[-1]):
                results.append("=")
        elif self.gen > other.gen:
            #print("8Secreto mayor",self.gen ,other.gen)
            
            results.append("↑")
        else:
            results.append("↓")
        
        #print(self)
        #print(other)
        #print(results)
        
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
        

