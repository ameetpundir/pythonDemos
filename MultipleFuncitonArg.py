def bar(first, second, third, **abc):
    if abc.get("action") == "sum":
        print("The sum is: %d" %(first + second + third))

    if abc.get("action") == "div":
            print ("The div is : %d" %(first/second))
            
    if abc.get("number") == "first":
        return first
    if abc.get("number") == "second":
        return second
result = bar(4, 2, 3, action = "div", number = "second")
print("Result: %d" %(result))


# Setup
actor = {"name": "John Cleese", "rank": "awesome"}

actor = {"name": "John Cleese", "rank": "awesome"}

def get_last_name():
    return actor["name"].split()[1]

get_last_name()
print("All exceptions caught! Good job!")
print("The actor's last name is %s" % get_last_name())

import json
json_string = json.dumps([1, 2, 3, "a", "b", "c"])
print(json_string)
print(json.loads(json_string))