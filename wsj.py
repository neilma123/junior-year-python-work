import webbrowser
s = int(input("wanna start?"))
while s == 1:
    z = input("what is the year?")
    z2 = input("what is the month?")
    if int(z2) < 10:
        z2 ="0" + z2
    z3 = input("what is the day?")
    if int(z3) < 10:
        z3 = "0" + z3
    z4 = z+z2+z3
    x = "https://www.wsj.com/news/archive/" + z4
    webbrowser.open("https://www.wsj.com/news/archive/"+z4)
    print(x)
    s2 = int(input("again?"))
    if s2 == 0:
        break
