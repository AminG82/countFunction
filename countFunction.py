#Write a function to count unique values in a list

def count_unique(items):
    result ={}
    for item in items:
        result[item] = result.get(item , 0) +1
    return result

genders =["Male" , "Female" , "Male"]
print(count_unique(genders))