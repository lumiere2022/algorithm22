def findMax(temp):
    max = -1
    for i in range(len(temp)):
        if temp[i][0] >= max:
            max = temp[i][0]
    return max

def solution(priorities, location):
    temp = []
    for index in range(len(priorities)):
        if index == location:
            temp.append([priorities[index], 1])
        else:
            temp.append([priorities[index], 0])
    
    max = findMax(temp)
            
    order = 0
    while(len(temp) != 0):
        if temp[0][0] < max:
            temp.append(temp.pop(0))
        else:
            if temp[0][1] == 1:
                temp.pop(0)
                order+=1
                return order
            else:
                temp.pop(0)
                order+=1
                max = findMax(temp)
