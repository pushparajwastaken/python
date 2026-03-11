name="Alice"
age=25
#naming convention- snake_case
"""
    This is a multiline quote
    use proper indentation
"""
print(age)
first_name="Pushparaj"
age=22
cgpa=8.19
power=10**2
print(age)
print(power)


#three ways to use strings
long_dash="-"*20
print(long_dash)
string_normal="My name is Pushparaj\n"
string_small='in 3rd sem\n'
string_long="""and i am doing python
"""
print(string_normal+string_small+string_long)

#booleans
is_true=True #not true or TRUE

can_vote=age>=18
print(can_vote)

# //-used for floor division rounds down the value 
# **-used fo exponent
"""
AND-both must be true
OR-at least one must be true
NOT-reverses the value
"""


#fStrings
sen=f"Hi my name is {name}".title()
print(sen)
print(sen.lower())
print(sen.upper())
print("Python" in sen)#false
print(sen.startswith("P"))#false
print(sen.endswith("j"))#false
print(sen.find("hi"))#-1
print(sen.count("is"))#0
print(sen.replace("Alice","Lavanya"))