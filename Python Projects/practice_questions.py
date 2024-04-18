'''
Given two int values, return their sum. Unless the two values are the same, then return double their sum.

sum_double(1, 2) → 3
sum_double(3, 2) → 5
sum_double(2, 2) → 8
'''
def sum_double(a, b):
  # Store the sum in a local variable
  sum = a + b
  
  # Double it if a and b are the same
  if a == b:
    sum = sum * 2
  return sum

'''
Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.

diff21(19) → 2
diff21(10) → 11
diff21(21) → 0
'''
def diff21(n):
  if n <= 21:
    return 21 - n
  else:
    return (n - 21) * 2
  
'''
Make a string out of text by enclosing it in single or double quotes "like this", and use + to
combine strings to make bigger strings. The with_no() example function takes in a string and
returns a new string with "No:" added at the front.
'''
def with_no(str):
  return "No:" + str

'''
The function len(str) returns the length of a string, and str[i] returns the char at index i.

This two_e() example method returns True if the string contains exactly two 'e' chars. The loop
for ch in str: is a standard loop which iterates over the chars in a string:
'''
def two_e(str):
  count = 0
  for ch in str:  ## this loops over each char in the string
    if ch == 'e':
      count = count + 1

  if count == 2:
    return True
  else:
    return False
  ## this last if/else can be written simply as "return (count == 2)"

'''
The same as with strings, the len() function returns the length of a list, and [i] accesses the ith element.
The same loop as above, for num in nums:, will loop over all the values in a list. However, here is another way to do it: 
The function range(n) returns 0, 1, 2, ... n-1. This can be used to write a loop for i in range(len(list)): 
over the index numbers of a list (or string). This makes it easier to refer to relative (i-1) or (i+1) elements 
inside the loop. This pair_13() example function returns True if the list contains a pair of 13's next to each other.
'''
def pair_13(nums):
  for i in range(len(nums) - 1):
    if nums[i]==13 and nums[i+1]==13:
      return True

  return False ## if we get here, there was not a pair of 13's

  ## Note: the -1 inside the range() stops the loop one short of the full length,
  ## so the code in the loop can refer to nums[i+1]

'''
Given a string, return the count of the number of times that a substring length 2 appears in the string 
and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).

last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2
'''
def last2(str):
  # Screen out too-short string case.
  if len(str) < 2:
    return 0
  
  # last 2 chars, can be written as str[-2:]
  last2 = str[len(str)-2:]
  count = 0
  
  # Check each substring length 2 starting at i
  for i in range(len(str)-2):
    sub = str[i:i+2]
    if sub == last2:
      count = count + 1

  return count