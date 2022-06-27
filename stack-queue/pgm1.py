import math

def solution(progresses, speeds):
    stack_pro = []
    stack_spe = []
    dday = []
    len_list = len(speeds)

    for i in range(len_list):  
        stack_pro.append(progresses.pop())
        stack_spe.append(speeds.pop())

    for x in range(len_list):
        dday.append(math.ceil((100 - stack_pro.pop())/stack_spe.pop()))
        print(dday)

    answer = []

    day = dday[0]
    index = 0

    for y in range(len_list):
        if(y==0):
            answer.append(1)
            continue
        if(day >= dday[y]):
            answer[index]+=1
        else:
            answer.append(1)
            day = dday[y]
            index+=1

    return answer
