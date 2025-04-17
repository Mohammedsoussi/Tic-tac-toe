a = ""
b = ""
c = ""
d = ""
e = ""
f = ""
g = ""
h = ""
k = ""
content = f"""| {a} | {b} | {c} |\n| {d} | {e} | {f} |\n| {g} | {h} | {k} |"""
def print_elemnts(content):
    print(content)


print_elemnts(content)
while True:
    x = input("user 1 please enter location (0-9)\n>")
    if x == '1': 
        if not a :
            a = "x"
            content = f"""| {a} | {b} | {c} |\n| {d} | {e} | {f} |\n| {g} | {h} | {k} |"""
            print_elemnts(content) 
        else:
            print("the is location is choiced")
            print_elemnts(content)
    if x == '2' :
        if not b :
            b = "x" 
            content = f"""| {a} | {b} | {c} |\n| {d} | {e} | {f} |\n| {g} | {h} | {k} |"""
            print_elemnts(content)
        else:
            print("the is location is choiced")
            print_elemnts(content)
    if x == "3" :
        if not c :
            c = "x"     
            content = f"""| {a} | {b} | {c} |\n| {d} | {e} | {f} |\n| {g} | {h} | {k} |"""
            print_elemnts(content)
        else:
            print("the is location is choiced")
            print_elemnts(content)
    if x == "4" :
        if not d :
            d = "x"
            content = f"""| {a} | {b} | {c} |\n| {d} | {e} | {f} |\n| {g} | {h} | {k} |"""
            print_elemnts(content)
        else:
            print("the is location is choiced")
            print_elemnts(content)
    if x == "5":
        if not e:
            e = "x"
            content = f"""| {a} | {b} | {c} |\n| {d} | {e} | {f} |\n| {g} | {h} | {k} |"""
            print_elemnts(content)
        else:
            print("the is location is choiced")
            print_elemnts(content)
    if x == "6" :
        if not f:
            f = "x"
            content = f"""| {a} | {b} | {c} |\n| {d} | {e} | {f} |\n| {g} | {h} | {k} |"""
            print_elemnts(content)
        else :
            print("the is location is choiced")
    if x == "7" :
        if not g :
            g = "x"
            content = f"""| {a} | {b} | {c} |\n| {d} | {e} | {f} |\n| {g} | {h} | {k} |"""
            print_elemnts(content)
        else:
            print("the is location is oreyde choice it ")
    if x == "8" :
        h = "x"
        content = f"""| {a} | {b} | {c} |\n| {d} | {e} | {f} |\n| {g} | {h} | {k} |"""
        print_elemnts(content)
    if x == "9" :
        k = "x"
        content = f"""| {a} | {b} | {c} |\n| {d} | {e} | {f} |\n| {g} | {h} | {k} |"""
        print_elemnts(content)
    if a ==b==c == "x" or d == e == f == "x" or g ==h == k == "x" or a == e ==k == "x" or g == e ==c == "x" or a == d == g == "x"or e == h == b == "x"or c == f == k == "x":
        print("\n[+]The winer is x")
        print("[+]Game end")
        verifie = input("for play agin y for exiting n\n>")
        if verifie == "y":
            a = ""
            b = ""
            c = ""
            d = ""
            e = ""
            f = ""
            g = ""
            h = ""
            k = ""
            content = f"""| {a} | {b} | {c} |\n| {d} | {e} | {f} |\n| {g} | {h} | {k} |"""
            print_elemnts(content)
        else:
            print("[-]Your are exiting the game!")
            break
    elif a and b and c and d and e and f and g and h and k :
        print("\n[-] Draw")
        verifie = input("for play agin y for exiting n\n>")
        if verifie == "y":
            a = ""
            b = ""
            c = ""
            d = ""
            e = ""
            f = ""
            g = ""
            h = ""
            k = ""
            content = f"""| {a} | {b} | {c} |\n| {d} | {e} | {f} |\n| {g} | {h} | {k} |"""
            print_elemnts(content)
        else:
            break

    o = input("second user please enter location (0-9)\n>")
    if o == '1':
        if not 1 : 
            a = "o"
            content = f"""| {a} | {b} | {c} |\n| {d} | {e} | {f} |\n| {g} | {h} | {k} |"""
            print_elemnts(content) 
        else:
            print("the is location is choiced")
            print_elemnts(content)
    if o == '2' :
        if not b :
            b = "o" 
            content = f"""| {a} | {b} | {c} |\n| {d} | {e} | {f} |\n| {g} | {h} | {k} |"""
            print_elemnts(content)
        else:
            print("the is location is choiced")
            print_elemnts(content)
    if o == "3" :
        if not c :
            c = "o"    
            content = f"""| {a} | {b} | {c} |\n| {d} | {e} | {f} |\n| {g} | {h} | {k} |"""
            print_elemnts(content)
        else:
            print("the is location is choiced")
            print_elemnts(content)
    if o == "4" :
        if not d :
            d = "o"
            content = f"""| {a} | {b} | {c} |\n| {d} | {e} | {f} |\n| {g} | {h} | {k} |"""
            print_elemnts(content)
        else:
            print("the is location is choiced")
            print_elemnts(content)
    if o == "5":
        if not e :
            e = "o"
            content = f"""| {a} | {b} | {c} |\n| {d} | {e} | {f} |\n| {g} | {h} | {k} |"""
            print_elemnts(content)
        else:
            print("the is location is choiced")
            print_elemnts(content)
    if o == "6" :
        if not f:
            f = "o"
            content = f"""| {a} | {b} | {c} |\n| {d} | {e} | {f} |\n| {g} | {h} | {k} |"""
            print_elemnts(content)
        else:
            print("the is location is choiced")
            print_elemnts(content)
    if o == "7" :
        if not g :
            g = "o"
            content = f"""| {a} | {b} | {c} |\n| {d} | {e} | {f} |\n| {g} | {h} | {k} |"""
            print_elemnts(content)
        else:
            print("the is located is oeryde choice it ")
    if o == "8" :
        if not h:
            h = "o"
            content = f"""| {a} | {b} | {c} |\n| {d} | {e} | {f} |\n| {g} | {h} | {k} |"""
            print_elemnts(content)
        else:
            print("the is location is choiced")
            print_elemnts(content)
    if o == "9" :
        if not k :
            k = "o"
            content = f"""| {a} | {b} | {c} |\n| {d} | {e} | {f} |\n| {g} | {h} | {k} |"""
            print_elemnts(content)
        else:
            print("the is location is choiced")
            print_elemnts(content)
    if a == b == c == "o"or d == e == f == "o"or g == h == k == "o" or a == e == k == "o" or g == e == c == "o" or a == d == g == "o"or e == h == b == "o"or c == f == k == "o":
        print("\n[+]The winer is o")
        print("[+]Game end")
        verifie = input("for play agin y for exiting n\n>")
        if verifie == "y":
            a = ""
            b = ""
            c = ""
            d = ""
            e = ""
            f = ""
            g = ""
            h = ""
            k = ""
            content = f"""| {a} | {b} | {c} |\n| {d} | {e} | {f} |\n| {g} | {h} | {k} |"""
            print_elemnts(content)
        else:
            print("[-]Your are exting the game!")
            break
    elif a and b and c and d and e and f and g and h and k :
        print("\n[-]Draw")
        verifie = input("for play agin y for exiting n\n>")
        if verifie == "y":
            a = ""
            b = ""
            c = ""
            d = ""
            e = ""
            f = ""
            g = ""
            h = ""
            k = ""
            content = f"""| {a} | {b} | {c} |\n| {d} | {e} | {f} |\n| {g} | {h} | {k} |"""
            print_elemnts(content)
        else:
            break
        
