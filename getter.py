class patients:
    
     def setName(self,name):
        self.name=name
        
     def getName(self):
        return self.name
    
     def setId(self,Id):
        self.Id=Id
        
     def getId(self):
        return self.Id
    
p = patients()
p.setName('gayathri')
p.setId (10)
print(p.getName())
print(p.getId())
