a=2
b=type(a)
x=2.9
d=type(x)
name="deepu"
c=type(name)
num=3.5
x=type(num)
m=3+5j
n=type(m)
print(b,d,c,x,n)
v=3
c=type(v)
print(c)
first_name= "deepu"
last_name= "turupu"
age= "27"
email= "tdeepu308@gmail.com"
print("First name", first_name)
print("Last name", last_name)
print("Age", age)
print("Email", email)

list = ["deepika", "mani", "gayathri","maha"]
list.append("chinni")
print(list)
list.remove("chinni")
print(list)
tuple = ("apple","grapes","oranges","mangoes")
print(tuple)
set = {"oye","hinana","bahubali","nagavali"}
set.add("ready")
set.add("boss")
set.remove("ready")
print(set)
dict = {"don": "nagarjuna" ,
       "chandramukhi": "Raginikanth"}
dict.update({"manam": "shreya","orange": "ramcharan"})
dict.pop("manam")       
print(dict)




def check_number(num):
    if num >=70:
        return f"{num} is greater."
    elif num <=60:
        return f"{num} is lesser."
print(check_number(60))

def check_number(num):
    if num % 2 == 0:
        return f"{num} is even."
    else:
        return f"{num} is odd."
    
print(check_number(3))

def check_number(num):
    if num >= 60:
        return f"{num} is greater."
    else:
        return f"{num} is lesser."
print(check_number(100))






