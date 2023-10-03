# string concatenation (aka how to put strings together)
# suppose we want to create a string that says  "Hello you , _______ "

user = "AP" # some string variable

# a few ways to do it
print("Hello you, "+user)
print("Hello you, {}".format(user))
print(f"Hello you, {user}")
print("Hello you, %s" %(user))


adj = input("Adjective : ")
verb1 = input("verb :")
madjib = f"alskjfljd {adj}! sldjlajsdf fsd\
ldasjflj {verb1}"
    
print (madjib)