import random

a = [random.randint(0, 100) for i in range(random.choice([2,4,8,10,12]))]
a=[1,2,2,4]
print(a)

def snap(li):
    mid = len(li)//2
    li = random.choice([ li[:mid], li[mid:] ])
    return li
    
while sorted(a, reverse=True):
    print(a)
    print(len(a))
    a = snap(a)
    
    
