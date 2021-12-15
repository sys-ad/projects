# String Datatype
letter= "A"
my_sentence= """Lorem Ipsum is simply dummy text of the printing and
typesetting industry. Lorem Ipsum has been the industry's standard 
dummy text ever since the 1500s, when an unknown printer took a 
galley of type and scrambled it to make a type specimen book. 
It has survived not only five centuries, but also the leap into 
electronic typesetting, remaining essentially unchanged. It was 
popularised in the 1960s with the release of Letraset sheets containing 
Lorem Ipsum passages, and more recently with desktop publishing software 
like Aldus PageMaker including versions of Lorem Ipsum. gwtwtwtwew gwgewgtewgte gewgegeghehs"""

# Boolean
# True or False

# print(type(False))

# # Integer
# # 1...100

# print(type(100))

# # Float

# print(type(0.0000005))

# "+" Concatenation

# initialization
my_str= "Hello, "
name= input("What is your name, good sir? ").lower()
weather= input("What is the weather like today? ")



def greeting():
    return f"{my_str} {name}, the weather forcast today is {weather}."

# print(f"{my_str} {name}, the weather forcast today is {weather}.")

print(greeting())