# Quinn Plumb

from dog import Dog

dogs = []

with open("dogs.txt") as file:
    for line in file:
        # strip line
        stripped_line = line.strip()
        # split line
        c = stripped_line.split()
        dog1 = Dog(c[0], c[1], c[2], eval(c[3]))
        print(dog1)
        dogs.append(dog1)

print(dogs[0].get_name())
print(dogs[0].get_breed())
print(dogs[0].get_trick())
print(dogs[0].isHungry())

dogs[0].speak()
dogs[0].feed()
dogs[0].change_trick("fetch")

print(dogs[0].get_name())
print(dogs[0].get_breed())
print(dogs[0].get_trick())
print(dogs[0].isHungry())
