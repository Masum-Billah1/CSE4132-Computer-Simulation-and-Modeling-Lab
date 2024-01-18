import numpy as np

f = open('cpm_input.txt','r')
content = f.read()
numbers = content.split()

#maximum node
size = 0
for i in range(len(numbers)):
    if i %3 == 1:
        size = max(size,int(numbers[i]))

#array_index = node
#forward[array_index][0] = earliest start
#forward[array_index][1] = latest finish
foward = np.zeros((size,2))

#forward pass
no_of_edge = len(numbers)//3
for i in range(no_of_edge):
    activity = int(numbers[i * 3 + 2])
    end_node = int(numbers[i * 3 + 1])
    start_node = int(numbers[i * 3])

    if (foward[start_node - 1][1] + activity) > (foward[end_node - 1][1]):
        foward[end_node - 1][0] = foward[start_node - 1][1]
        foward[end_node - 1][1] = foward[end_node - 1][0] + activity

#backward[array_index][0] = latest start
#forward[array_index][1] = latest finish
#forward[array_index][2] = slack time
backward = np.zeros((size,2))

#backword pass
iteration = no_of_edge-1
temp = size

backward = np.zeros((size,2))
max_int_value = np.iinfo(np.int64).max
backward[backward == 0] = 999

backward[size-1][0] = foward[size-1][0]
backward[size-1][1] = foward[size-1][1]
# backward[size-1][2] = 0 #slack time of last node is zero
Temp = no_of_edge-1
while(temp>=0):
    temp-=1
    iteration = no_of_edge-1
    while(iteration >= 0):
        iteration -=1
        activity = int(numbers[iteration * 3 + 2])
        end_node = int(numbers[iteration * 3 + 1])
        start_node = int(numbers[iteration * 3])

        if backward[start_node-1][1] > backward[end_node-1][0]:
            backward[start_node-1][1] = backward[end_node-1][0]
            activity = foward[start_node-1][1] - foward[start_node-1][0]
            backward[start_node-1][0] = backward[start_node-1][1]-activity


#Critical Path
print('Critical Path: ', end=" ")
slack_time = np.zeros(size)
for i in range(size):
    slack_time[i] = backward[i][0]-foward[i][0]
    if slack_time[i] == 0:
        print(i+1,end=" ")
        if i!=(size-1):
            print('->',end=" ")
