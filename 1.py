''' print("---------with parameter-------")
def demo(name):
    print("welcome to basic python",name)
    print("welcome to basic python"+name)
demo("anjuma nasreen")


print("---------------keyword argument----------------")
def demo(name,designation,age):
    print(name)
    print(age)
    print(designation)
demo("anjuma nasreen",19,"designer"
    #default in function that is parameter and while calling functions we use parameters
   #DIFFERENCE B/W THESE 2 IS ARGU PLACING


print("---------------parameter argument----------------")
def demo(name,age,designation):
    print(name)
    print(age)
    print(designation)
demo("anjuma nasreen",19,"designer")
print("---------------------LIST---------------------")
def demo(list):
    list=["anju","ashu","ammi","abba"]
    for i in list:
        print(i)        
demo(list)
print("------PRINTING_PARTICULAR_INDEX_VALUE----------")
def demo(list):
    list=["anju","ashu","ammi","abba"]
    print("welcome",list[1])
demo(list)
print("------PRINTING_PARTICULAR_INDEX_VALUE2----------")
def demo(list):
    for i in list:
        print(i)
list=["anju","ashu","ammi","abba"]
demo(list)
print("")
print("welcome",list[1])   


print("-----------------------CLASSES WITH OBJECTS----------------------")
class register:
    print("welcome to classes")
    x=123
    a="anjuma nasreen"
obj=register()
print(obj)
print(obj.x)
print(obj.a)'''
print("---------------using INIT function-------------")
class register:
    def __init__(self,name,desg):
        self.name=name
        self.desg=desg
    def login(self):
        '''print("ur name"+name)
        print("ur desg"+desg)'''
        print("logged in",self.name)
obj=register("anju","developer")
#print(obj.name)
#print(obj.desg)
obj.login()




