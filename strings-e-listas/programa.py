#Declarando strings

string01 = "Olá mundo"
string02 = 'Olá mundo'

print(string01 == string02)

#Concatenando Strings

string01 = "Olá " + "mundo!"

print("\n")
print(string01)

string01 = "Olá " "mundo!"

print("\n")
print(string01)

#Interpolando Strings

print("\n")
print("Eu quero {}!!!".format("café"))

print("\n")
print("{} quer {}!!!".format("Fulana", "café"))

print("\n")
print("{0}! {0}! {0}!".format("CAFÉ"))

print("\n")
print("{0}!{1}!{2}!".format("uno", "dos", "tres"))

print("\n")
print("{nome}, son of {pai}, is not impressed!".format(nome = "Gimli", pai = "Gloin"))

# enumerate()

print("\n", enumerate("AAAAAAAAAAAAAAAAAAAA"))

# .split()

print("\n","Eu quero café")
print("\n","Eu quero café".split())

# .join()

print("\n","[\"Eu\", \"quero\", \"café\"]")
print("\n"," ".join(["Eu", "quero", "café"]))

# .find()

print("\n","Eu quero café".find("q"))

# .replace()

print("\n","Eu quero café".replace("café", "amor"))
