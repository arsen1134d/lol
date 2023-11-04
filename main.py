class t:
   total_t = 0



   def __init__(self, name, swim = False, fly=False, walk = True, run = True):
       self.name = name
       self.can_swim = swim
       self.can_fly = fly
       self.can_walk = walk
       self.can_run = run


def swim(self):
        if self.can_swim:
            return f"{self.name}"
        else:
            return f"{self.name}"

def fly(self):
       if self.can_fly:
           return f"{self.name}"
       else:
           return f"{self.name}"

 def walk(self):
       if self.can_walk:
           return f"{self.name}"
       else:
           return f"{self.name}"



def run(self):
    if self.can_run:
        return f"{self.name}"
    else:
        return f"{self.name}"

tiger = t(swim = False, fly =False, walk = True, run = True)
duck = t(swim= True, fly =True, walk = True, run = False)
fish = t(swim = True, fly =False, walk = False, run = False)
monkey = t(swim = True, fly =False, walk = True, run =True)

print(tiger.swim())
print(duck.swim())
print(fish.swim())
print(monkey.swim())

print(f"зоопарк: {t.total_t}")