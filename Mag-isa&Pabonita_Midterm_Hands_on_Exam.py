import random
# Grade School Solving Basic Operations
print("Grade School Basic Mathematical Solving of Operations")
print("***************************************")
a = (random.randrange(1, 99))
b = (random.randrange(1, 99))
print(f"What is {a} + {b}?")
add = int(input(f"{a} + {b} = "))

if add == a + b:
    print("Your answer is correct!")
else:
    print("Your answer is incorrect!")

    c = (random.randrange(1, 99))
    d = (random.randrange(1, 99))
    print(f"What is {c} - {d}?")
    add = int(input(f"{c} - {d} = "))

    if add == a + b:
        print("Your answer is correct!")
    else:
        print("Your answer is incorrect!")

        e = (random.randrange(1, 99))
        f = (random.randrange(1, 99))
        print(f"What is {e} x {f}?")
        add = int(input(f"{e} x {f} = "))

        if add == a + b:
            print("Your answer is correct!")
        else:
            print("Your answer is incorrect!")

    g = (random.randrange(1, 99))
    h = (random.randrange(1, 99))
    print(f"What is {g} / {h}?")
    add = int(input(f"{g} / {h} = "))

    if add == a + b:
        print("Your answer is correct!")
    else:
        print("Your answer is incorrect!")