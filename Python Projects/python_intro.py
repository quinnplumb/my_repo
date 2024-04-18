# this is a comment

# if statements

x = -1
y = 1

if x < 1:
    x = 1
    x+= 10
    print("x was negative")


# loops
nums = [10, 20, 30, 40, 50]
for i in range(len(nums)):
    print(nums[i])

for num in nums:
    num += 5
    print(num)
print(nums)

for i, num in enumerate(nums):
    print("i is", i, "num is", num)

dogs=["brody","phoebe","bailey"]

for d in range(len(dogs)):
    print(dogs[d])

for d in dogs:
    print(d)

total = 0
nums = [1, 5, 9, 13]
for n in nums:
    total += n

print(total, "is the total in nums")
print(f"the sum of nums is {total}")

# functions
def hello():
    print("hello!")
hello()

def hello(name):
    print("hello,", name)
hello("thomas")

# Strings
print("She's a great dancer")
print('Im "him"')

#string concatenation
cost = 14.75

print("this costs $",str(cost))

title = "Rephactor Python"
print("Last character:", title[-1])
print("Fifth character from the end", title[-5])

full_name = "Quinn Plumb"

fname = full_name[0:5]

platform_computing = "platform computing"

platform = platform_computing[0:8]
computing = platform_computing[9:18]

# Swapping values in a list
nums = [0, 3, 8, 5, 4]
temp = nums[2]
nums[2] = nums[4]
nums[4] = temp
print(nums)