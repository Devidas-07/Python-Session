import random
print(random.random())

litst = [1, 2, 3, 4, 5]
print(random.choice(litst))
for i in range(5):
    print(random.choice(litst), end=" ")
print(random.sample(litst, 4))