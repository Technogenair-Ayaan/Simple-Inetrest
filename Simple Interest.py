print("WELCOME TO SIMPLE INTEREST CALCULATOR")
print("Designed,Coded by Ayaan Ansari")
print("\t SIMPLE \t INTEREST \t CALCULATOR")
print("Please enter your principal:")
var1 = input()
print("Please enter you rate of interest:")
var2 = input()
print("Please enter the time:")
var3 = input()
one = int(var1)*int(var2)
two = int(one)*int(var3)
si = int(two)/100
A = int(si)+int(var1)
print("Your Simple Interest:",si)
print("Your Amount Is:",A)

