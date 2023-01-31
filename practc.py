sci_subject = ("phyc", "bio", "math")
hum_subject = ("histo", "geo", "CRE")
subjects = (sci_subject, hum_subject)  # we nest the two tuples into one tuple
print(subjects)
german_to_English = {"Wasser": "water", "Brot": "Bread", "Milch": "Milk"}
translation = german_to_English["Milch"]
print(translation)

# we create dictionary using "dict()" function
words = dict([("computer", "is an electronic device use to enter data process and give expected output"),
              ("school", "This is a public place where people or children can go and learn")])
print(words)

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

a, b = 12, 15
a, b = b, a
print(a)
print(b)

f_set = {1, 2, 3}
f_set.add(7)
f_set.update([8, 9, 10])  # we have to put in [] bracket
f_set.discard(1)
print(f_set)

f_set = {1, 2, 3}
s_set = {2, 4, 5}
intersection = f_set.intersection(s_set)  # intersection() are used to give the common element in both list 1&2
print(intersection)


# addition
def add(q, z):
    answer = 0
    while z > q:
        answer = answer + z
        q = q + 1
    return answer


results = add(1, 3)
print(results)  # the result will be 6


# multiplication
def add(q, z):
    answer = 1
    while z > q:
        answer = answer * z
        q = q + 1
    return answer


results = add(1, 3)
print(results)  # the result will be 9


