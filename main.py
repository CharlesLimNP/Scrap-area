import memberA_module as moduleA
import memberB_module as moduleB

x, y, z = 121, 22, 33
print(f"{x} is an {moduleB.evenOrOdd(x)} number")

x, y, z = 121, 22, 33
print(f"The sum of {x}, {y}, {z} is {moduleA.add(x,y,z)}")

print(f"{x} is an {moduleB.evenOrOdd(x)} number")

sentence = "This sentence will be underlined"
moduleA.print_underline(sentence)