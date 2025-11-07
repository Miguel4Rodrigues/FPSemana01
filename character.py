name = []
attack = []
defence = []

for i in range(3):
    name.insert(i, input())
    attack.insert(i, int(input()))
    defence.insert(i, int(input()))

characters = [[name[0], (attack[0], defence[0])], [name[1], (attack[1], defence[1])], [name[2], (attack[2], defence[2])]]

print(characters)

#prints the biggest attack value
if max(attack) == attack[0]:
    print("Ataque "+ name[0] + " " + str(max(attack)))

elif max(attack) == attack[1]:
    print("Ataque "+ name[1] + " " + str(max(attack)))

elif max(attack) == attack[2]:
    print("Ataque "+ name[2] + " " + str(max(attack)))


#prints the biggest defence value
if max(defence) == defence[0]:
    print("Defesa "+ name[0] + " " + str(max(defence)))

elif max(defence) == defence[1]:
    print("Defesa "+ name[1] + " " + str(max(defence)))

elif max(defence) == defence[2]:
    print("Defesa "+ name[2] + " " + str(max(defence)))