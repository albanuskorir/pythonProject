print(54 + 4)
if 100 < 10:
    print("100 is greater than 10")
else:
    print("100 is less than 10")

yob = 2005
cy = 2022
age = cy - yob
print(age)  # this is your age that you can put manually
if age >= 18:
    print("Eligible to vote")
else:
    print("You are underage you cannot vote!!!")

print(2 ** 3)  # return 2 power 3

print(10 / 2)  # in single slash (/) it would include the decimal part

print(50 // 4)  # 2 slash (//) ignore the decimal part

print(55 % 4)  # module (%) use to return the reminder

a, b = 1, 2
print(a)
print(b)

b, a = a, b
print(a)
print(b)

x = 2
y = 4
result = x ** y
print(result)

print(2 == 3)
print(2 != 5)

string = "words"

print(string[0])  # ]
print(string[1])  # ]
print(string[2])  # -]> it will place each words start from 0 towards end
print(string[3])  # ]
print(string[4])  # ]

print(5 > 2 and 1 > 0)  # it will print true cuz both are true
print(3 > 2 or 2 > 5)  # it will print one of them if it is true else print false

print(True * 5)  # it'll return the correct answer 5
print(False * 20)  # it'll return 0(zero)

my_string = "I want to continue\nin the next new line"
print(my_string)  # \n is used to move the cursor to the next new line

string = "meru"
print(string[1:])  # if we want to start from a specific index and continue getting all the characters
print(string[:3])  # if we want to start from 0 to the specific index, we can simply specify the ending index

comrade = "when you are texting shiet in whatsapp group,\n Just print stupid 5 times!!!"
print(comrade)
string = "you are stupid; \n"
repeat_5_times = string * 5
print(repeat_5_times)

print("THIS IS NEXT PHASE BELOW......... STRING BUILD IN METHOD......>")
name = "i am engineer albz"
print(len(name))

string = "mine"
replace = string.replace("m", "N")
print(replace)

string = " i am fine "
print(string.strip())

sentence = "i am still schooling in university"
print(sentence.split(" "))
print("_".join(sentence))

animals = ["cat", "dog", "goat", "cow"]
print(" , ".join(animals))

string = "Hi i am here"
print(string.count("H"))  # this is case sensitive "H" is not equal to "h"
print(string.count("i"))
print(string.count("m"))
print(string.count("r"))
print(string.count("h"))

string = "hi there"
print(string.find("5"))
print(string.find("e"))
print(string.find("h"))

string = "UNIVERSITY"
print(string.lower())  # the result will appear in lower case
string = "school"
print(string.upper())

string = "how are you"
print(string.capitalize())  # it'll capitalize  the first character in sentence
print(string.title())  # it'll capitalize the first character in each word

string = "are you HERE?"
string2 = "YES"
print(string.isupper())  # return false because only HERE are in uppercase
print(string2.isupper())  # return true because that word is in uppercase

string = "12a"
string1 = "1.2"
string2 = "12"
print(string.isdecimal())
print(string1.isdecimal())
print(string2.isdecimal())

print("THIS IS NEXT PHASE BELOW......... STRING FORMATTING ......>")
greetings = "Good morning"
print(greetings)
greeting = "Good morning {}. Today is {} you have to go to church".format("Albanus", "sunday")
print(greeting)

# use to specify parameters inside curly braces below ***
greetings = "Today is  {0}. Have a nice {1}".format("sunday", "weekend")
print(greetings)

# we can specify parameters inside  format() method....NOTE a variable must start with an underscore or a letter
greetings = "Today is  {weekend}. Have a nice day {my_name}".format(my_name="Albanus", weekend="sunday")
print(greetings)

# we can combine both kind of argument
greetings = "My location is {center}. Building {0}, come at {time}".format("Furaha apartment", center="Ruiru",
                                                                           time="14:30")
print(greetings)

# Another way pf formating string using 'f' and 'F'
f_name = "Albanus"
weekend = "sunday"
greetings = f'Good morning {f_name}.Today is {weekend}'
print(greetings)
continent = "Africa"
greetings = F'''i am in continent of {continent}'''
print(greetings)

print("THIS IS NEXT PHASE BELOW......... LIST IN PYTHON ......>")
students = ["Albert", "Kamau", "John"]
students[0] = "Salim"  # we use this to change the name in the list
students.append("Kimani")  # we use append to add values to the list
print(students[3])

# SLICING
my_list = [1, 2, 3, 4]
print(my_list[2:])  # this will omit the first 2 and print the rest
print(my_list[:3])  # it'll print from 0-3 and omit the rest

string = ["a", "a", "a", "a", "a", "a"]
string[0] = "A"
print(string)

# concatenating the list
f_list = [1, 2, 3, 4]
s_list = [5, 6, 7, 8]
T_list = f_list + s_list
print(T_list)

# how to nest a list inside another list
math_point = [82, "math"]
math_point[0] = 56  # use to change the value math
physics_point = [69, "physics"]
subject = [math_point, physics_point]
print(subject)
print(subject[0])  # it'll access only the first part of the subject following the index position
# recursive of accessing the word math which hs been nested by the subject and also inside math_point
print(subject[0][1])

# LIST METHODS
my_list = ["albanus", "kip", 1, 6]
print(len(my_list))  # return "4". are used to count the number of indexes
mine = "albanus"
print(len(mine))  # return "7". are used to count the number of characters in the word

# HOW TO ADD AN ELEMENT TO A LIST (list can be added using [append()] function
mine = ["korir", "jonte"]
mine.append("noah")  # new added list
mine.append("alex")  # new added list
mine.remove("korir")  # use to remove element in the list
print(mine)

# add element to a specific position (element can be added to a list to a specific location using [insert()] function)
list = ["a", "c", "d"]
list.insert(1, "b")  # insert element at a certain position
list.append("e")  # add element at the end of the list
print(list)

# How to delete element from the list by using ->[pop()] function
list = [1, 2, 3, 4, 5]
list.pop()  # delete element from the list begin from right hand side by default
list.pop(1)  # delete specific element from the list
print(list)
# we can delete using the word "del"
list = [1, 2, 3, 4]
del list[2]
print(list)
# delete using slices
list = [1, 2, 3, 4, 5]
del list[:3]  # delete the first 3 element
print(list)
# we can REVERSE list using [reverse()] function
list = [1, 2, 3, 4, 5]
list.reverse()  # reverse the list start from the end
list.sort()  # use to return from reverse to normal arrangement
print(list)

# INDEX search
list = ["math", "chem", "Geo", "Bio"]
#        0        1       2      3
print(list.index("Geo"))  # return 2

# membership check use to check if the element are in the list by using [IN and NOT IN]
my_list = [1, 2, 3, 4]
print(1 in my_list)
char = ['a', 'b', 'c', 'd']
print('l' in char)
char = ['a', 'b', 'c', 'd']
print('u' not in char)
# sort list using [sort() function]
list = [1, 5, 8, 6, 5, 7, 9, 4, 4, 2, 0, 3]  # can be sort in the order of counting
list.sort()
mine = ['a', 'c', 'g', 'd', 'f', 'l', 'e']  # can be sort alphabetically
mine.sort()
print(list)
print(mine)

# LIST COMPREHENSION
numbers = [2, 3, 4, 5]
numbers_tenfold = []
for number in numbers:
    number = number * 10
    numbers_tenfold.append(number)
print(numbers_tenfold)

# comprehensive
numbers = [2, 3, 4, 5]
numbers_tenfold = [number * 10 for number in numbers]  # it'll multiply each number in the array by 10
print(numbers_tenfold)

# we can include condition
positive_numbers = []
numbers = [1, -2, 0, 2, 3, -6, 5, 9]
for number in numbers:
    if number > 0:
        positive_numbers.append(number + 100)
        print(positive_numbers)

# comprehensive
numbers = [1, -2, 0, 2, 3, -6, 5, 9]
positive_numbers = [number + 100 for number in numbers if number > 0]
print(positive_numbers)

# we can also use comprehension with multiple list
f_list = [2, 4, 6]
s_list = [50]
f_list.append(10)
d_list = [f_element + s_element for f_element in f_list for s_element in s_list]
print(d_list)

print("THIS IS NEXT PHASE BELOW......... TUPLES IN PYTHON ......>")
electronics = ("comps", "s-phone", "radio", "microwave")
# position        0         1         2         3
print(electronics)
print(len(electronics))
print(electronics[2])
print(electronics[:2])  # it'll display the first 2 nad exclude that 2
print(electronics[1:])  # it'll display from position 1 towards the end
print(electronics.index("radio"))  # it'll return 2, if you type Radio instead of radio it would  not display anything
# concatenate or merge two tuples
cars = ("harrier", "nissan", "toyota")
All = electronics + cars
print(All)  # it'll display all in one line, elements for electronics and cars

# MEMBERSHIP CHECK
cars = ("harrier", "nissan", "toyota")
print("lorry" in cars)
print("nissan" in cars)
print("nissan" not in cars)
print("lorry" not in cars)

# How to nest 2 tuples
sci_subject = ("phyc", "bio", "math")
hum_subject = ("histo", "geo", "CRE")
subjects = (sci_subject, hum_subject)  # we nest the two tuples into one tuple
print(subjects)
# immutability means you cannot add, delete or change the element after created


print("THIS IS NEXT PHASE BELOW......... DICTIONARY IN PYTHON ......>")
# KEY-VALUE AND DATA STRUCTURE
german_to_English = {"Wasser": "water", "Brot": "Bread", "Milch": "Milk"}
translation = german_to_English["Milch"]
print(translation)

# we can also get the value of element in a dictionary the value using["get()" function]and specify the key of the item
german_to_English = {"Wasser": "water", "Brot": "Bread", "Milch": "Milk"}
translation = german_to_English.get("Brot")
print(translation)

# we create dictionary using "dict()" function
words = dict([("computer", "is an electronic device use to enter data process and give expected output"),
              ("school", "This is a public place where people or children can go and learn")])
print(words)

# How to add value to a dictionary
words = {'a': 'alfa',
         'b': 'beta',
         'd': 'delta',
         }
words['g'] = 'gama'  # it'll add the word ("g": "gama") to the dictionary
words.pop("a")  # it'll remove only element that has been specified
words.popitem()  # using "popitem()" function with empty bracket it'll delete the added item or from the end
words['b'] = 'bravo'  # if we specify the key of an element that is already part of dictionary,
# that element is going to be modified or replace by the one that has been added
print(words)

# comprehension in dict
marks = {
    'Bio': 56,
    'Geo': 75,
    'chem': 59
}
element = marks.items()
print(element)

# create to add 10 marks to each subjects
arks = {
    'Bio': 56,
    'Geo': 75,
    'chem': 59
}
grade = marks.items()
grade_marks = {key: value + 10 for (key, value) in element}
print(grade_marks)

print("THIS IS NEXT PHASE BELOW......... SETS IN PYTHON ......>")
f_set = {1, 2, 3}
print(f_set)

# alternative method
e_set = set()
f_set = set((4, 5, 6))
print(f_set)

# adding element to a set using .add() function
f_set = {1, 2, 3}
f_set.add(7)
print(f_set)

my_set = {1, 2, 3}
my_set.update([4, 5, 6, 7])  # update() are used to add more than one element in a set
print(my_set)
my_set.update("ABC")
my_set.remove(2)  # are used to remove specific element from the set
my_set.discard("A")  # are used to remove or discard element in the set
print(my_set)

# set theory operation
f_set = {1, 2, 3}
s_set = {4, 5, 6}
union = f_set.union(s_set)  # union() method are used for concatenating the list 1 & 2
print(union)

# intersection
f_set = {1, 2, 3}
s_set = {2, 4, 5}
intersection = f_set.intersection(s_set)  # intersection() are used to give the common element in both list 1&2
print(intersection)

# Difference
f_set = {'a', 'b', 3}
s_set = {'b', 4, 6}
difference = f_set.difference(s_set)  # used to print the element that are in list 1 but not in 2 == "a", 3
print(difference)
diff = s_set.difference(f_set)  # used to print the element that are in list 2 but not in 1 == 4, 6
print(diff)

print("THIS IS NEXT PHASE BELOW......... TYPE CONVERSION IN PYTHON ......>")

# convert to an integer
two = int(2)  # use to convert integer literal into an integer
print(two)
five = int(5.6)  # use to convert float literal into an integer
print(five)
seven = int("7")  # use to convert string literal into an integer
print(seven)

# convert into float
int_two = float(2)  # use to convert integer literal into a float
print(int_two)

# convert into string
five = str(5)  # use to convert float literal into an integer
print(five)

print("THIS IS NEXT PHASE BELOW......... CONTROL FLOW IN PYTHON ......>")

# condition statement
age = input("Enter your age: ")
if age >= "18":
    print("Eligible to vote")
else:
    print("Wait until 2027")

# Looping/Iteration
# for loop
print("for loop")
for number in range(0, 5):
    print(number)  # it'll print numbers from 0 up to 4 and exclude 5

# while loop
print("While loop")
number = 1
while number < 7:
    print(number)
    number += 1

# iteration: Looping through data structures
stud = ["John", "James", "Joseph", "kamau"]
for stu in stud:
    print(stud)

# how tp stop for loop
my_list = [5, 4, 6, 9, -2, 8, 7]
for element in my_list:
    print("current number: ", element)
    if element < 0:
        print("we just found a negative number")
        break

# How to skip an iteration
my_sum = 0
my_list = [5, 4, 6, 9, -2, 8, 7]
for element in my_list:
    if element < 0:
        continue
    my_sum += element
print(my_sum)
print("ignore negative number")

print("THIS IS NEXT PHASE BELOW......... FUNCTION IN PYTHON ......>")


def add(f_no, s_no):
    m_sum = f_no + s_no
    return m_sum


result = add(5, 9)
print(result)


def add(q, z):
    answer = 0
    while z > q:
        answer = answer + z
        q = q + 1
    return answer


results = add(1, 5)  # we call this function with argument
print(results)


# default argument in functions
def get_user(fi_name, l_name):
    return f"hi {fi_name} {l_name} how are you doing?"


user = get_user("Albanus", "Korir")  # we call this function with argument
print(user)


# keyword argument list

