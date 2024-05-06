"""
3 Colors
Red:"Stop"
Green:"Go"
Yellow:"Look"
Blue,White:"Light is Broken"
Else:Not Valid Keyword
"""

light=input("Enter any Traffic Light:")
if (light=="Red"):
    print("Stop!")
elif (light=="Green"):
    print("Go!")
elif (light=="Yellow"):
    print("Look!")
elif (light=="Blue" or light=="White"):
    print("Light is Broken")
else:
    print("Invalid Keyword, Please try Again Later")