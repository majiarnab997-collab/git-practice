def first_file(name:str)->str:
  return f"your name is :{name}"

def second_file(age:int)->str:
  return f"{first_file("Arnab")} your age is:{age}"


def third_file(places:str)->str:
  return f"{second_file(20)} and you are living in {places}"

print("Hello Git")

name = "Student"

print("Welcome", name)

print(third_file("bhongir"))