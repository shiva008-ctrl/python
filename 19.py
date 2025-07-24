# class myclass():
#  x=5
# p1=myclass

# print(p1.x)

# class person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
# p1=person("sahil",18)
# print(p1.name)
# print(p1.age)


# class myname:
# 	def __init__(self, name, age,city):
# 		self.name = name
# 		self.age = age
# 		self.city=city
# p1= myname("sahil",18,"shimla")
# print(p1.name,p1.age,p1.city)
   
# # 
# # repr
# def __repr__(self):
#     return f" student({self.name}{self.age}{self.city})"
# p1= myname("sahil",18,"hamirpur")
# print(p1)

#coustom ,object string output 
class book :
  def __init__(self,title,authour,year):
    self . title = title
    self . authour = authour
    self . year = year
    def __str__(self):
        return f"({self.title}, {self.author}, {self.year})"
    p1 = book("python", "sahil", 2023)
    print(p1)