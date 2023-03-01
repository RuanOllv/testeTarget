string = input("Digite uma string: ")
nova_string = ""

for i in range(len(string)-1, -1, -1):
    nova_string += string[i]

print("A string invertida é:", nova_string)

