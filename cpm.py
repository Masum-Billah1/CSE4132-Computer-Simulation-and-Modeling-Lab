def LCM(seed,a,c,mod):
    total = 13
    for i in range(total):
        print(seed, end=' ')
        seed = (a * seed + c) % mod
    print()

f = open('input.txt', 'r')
content = f.read()
numbers = content.split()

task = 5
for i in range(task):
    task-=1
    seed = int(numbers[i*4+0])
    a = int(numbers[i*4+1])
    c = int(numbers[i*4+2])
    mod = int(numbers[i*4+3])
    LCM(seed,a,c,mod)

f.close()