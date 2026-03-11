myset = {"apple", "banana", "cherry"}
thisset = {"apple", "banana", "cherry"}
print(thisset)
#Set items are unordered, unchangeable, and do not allow duplicate values.

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

# The values True and 1 are considered the same value in sets, and are treated as duplicates

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

#The values False and 0 are considered the same value in sets, and are treated as duplicates
print(len(thisset))
set1 = {"abc", 34, True, 40, "male"}
myset = {"apple", "banana", "cherry"}
print(type(myset))
fruits=set(["loyola","xavier","gonzaga"])
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
empty_set=set()