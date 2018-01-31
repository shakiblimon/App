
'''

def get_first_name(full_name):
    return full_name.split(" ")[0]

fallback_name = {
    "first_name": "UserFirstName",
    "last_name": "UserLastName"
}

raw_name = input("Please enter your name: ")
first_name = get_first_name(raw_name)

# If the user didn't type anything in, use the fallback name
if not first_name:
    first_name = get_first_name(fallback_name)

print("Hi, {}!".format(first_name))

'''
def fallback(submission):
    if not submission:
        return "fixed"
    else:
        return submission
name = fallback(input("What is your name??? >>  "))
print('hello ',name)