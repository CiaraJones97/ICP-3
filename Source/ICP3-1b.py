x= input("Enter a sentence: ")

my_sets = {'a', 'e', 'i','o','u'}
count = 0
for i in (x.lower()):
    if i in my_sets:
        count = count + 1

print("count of vowels is: ", format(count))
