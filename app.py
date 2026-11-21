def first_file(name:str)->str:
  return f"your name is :{name}"

def second_file(age:int)->str:
  return f"{first_file("Arnab")} your age is:{age}"


print("Hello Git")

name = "Student"

print("Welcome", name)

print(second_file(20))