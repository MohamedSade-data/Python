# #1- Create a class Rectangle with attributes width and height, 
# # and methods area and perimeter. Then create a class Square that inherits from Rectangle.

class rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    
    def area(self):
        return (self.width * self.height)
    
   
    def perimeter(self):
        return 2*(self.width + self.height)


class Square(rectangle):
    def __init__(self, width):
        # self.width = width
        super().__init__(width,width)
        
   
    def area(self):
        return 4 * (self.width)
    
    
    def perimeter(self):
        return  (self.width * self.width)

rectangle1 = rectangle(2,5)
print(rectangle1.perimeter())

Square1 = Square(8)
print(Square1.area())

# #--------------------------------------------------------------------------------------------------------------

# # 2- Define a class Account with a private attribute balance. 
# # Provide methods to deposit, withdraw, and make balance private and provide setter and getter property for it.

class account:
    
    def __init__(self, accountant):
        self.Accountant(accountant) 

    @balance.setter
    def Accountant(self, accountant):
         if (accountant > 0):
              self.__accountant = accountant 
         else:
              print ("Can not set negative value")   
    
    @property
    def Accountant(self):
        return self.accountant         
   
    def deposite(self, preacher):
        if (preacher > 0 and preacher < self.accountant):
            result = self.__accountant - preacher
            self.Accountant(result)
            return result 
    
    def add(self, preacher):
        self.Accountant(self.__accountant + preacher)
        return (self.__accountant + preacher)
    
    
    

wor1 = account(-600000)


# # ---------------------------------------------------------------------------------------------------
# #3- Define a function play_sound that accepts an object of a base class Instrument and calls its play method. 
# # Create subclasses Guitar and Drum that override the play method. 
# # Demonstrate polymorphism by passing objects of Guitar and Drum to play_sound.
    
class instrument:
    def play(self):
        pass

class Guitar(instrument):
    def play(self):
        print("its Guitar")

class Drum(instrument):
    def play(self):
        print("ist Drum")

def play_sound(object : instrument):
    return object.play()

Drum1 = Drum()

Guitar1 = Guitar()
play_sound(Drum1)
    
# ---------------------------------------------------------------------------------------------------
#4- Create classes CPU, RAM, and Storage each with a method specs. Create a class Computer that includes objects of CPU, 
#RAM, and Storage. The Computer class should have a method system_specs that calls the specs method of each component.

class cpu:
    def specs(self):
        print("Cpu Core 8")

class ram:
    def specs(self):
        print("Ram 14")

class storage:
    def specs(self):
        print("Storage is 256")

class computer:    
    def __init__(self, cpu_object : cpu, ram_object : ram, storage_opject: storage):
        self.cpu_object = cpu_object
        self.ram_object = ram_object
        self.storage_opject = storage_opject

    def calling(self):
        self.cpu_object.specs()
        self.ram_object.specs()
        self.storage_opject.specs()

cpu1 = cpu()
ram1 = ram()
storage1 = storage()

computer1 = computer(cpu1, ram1, storage1)
computer1.calling()

