dictionary = {"name": "essy",
              "age": 18,
              "town": "nairobi"
              }

print(dictionary)
print(dictionary["town"])
print(dictionary["age"])
print(dictionary["name"])

x = dictionary["town"]

y = dictionary.get("town")

new_dictionary = dictionary.copy()
print(new_dictionary)