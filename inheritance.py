class animal:
    def __init__(self,name,color):
        self.name=name
        self.color=color
class birds(animal):
    def __init__(self,shape,name,color):
        animal. __init__(self,name,color)
        self.shape=shape

Birds=birds("circle","cow","black")
print(Birds.shape)
print(Birds.name)
print(Birds.color)
        
