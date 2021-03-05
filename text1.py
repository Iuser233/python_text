message="hello world"
print(message)

name="ada lovelace"
print(name.title())
print(name.lower())
print(name.upper())

class Dog():
    def __init__(self, name,age):
       """初始化属性name和age"""
       self.name=name
       self.age=age

    def sit(self):
        print(self.name.title()+' is now sitting.')

    def roll_over(self):
        '模拟小狗打滚'
        print(self.name.title()+"rolled over")


my_dog=Dog('xiaoHuang',6)
print("my dog's name is "+my_dog.name.title()+".")
my_dog.sit()