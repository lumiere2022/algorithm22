question_list = list(input())

answer_list = []
answer = 0
temp = 1

for i, elem in enumerate(question_list):
    if elem == '(':
        answer_list.append(elem)
        temp *= 2
    elif elem == '[':
        answer_list.append(elem)
        temp *= 3
    elif elem == ')':
        if not answer_list or answer_list[-1] == '[':
            answer = 0
            break
        if question_list[i-1] == '(':
            answer += temp
        answer_list.pop()
        temp //= 2
    else:
        if not answer_list or answer_list[-1] == '(':
            answer = 0
            break
        if question_list[i-1] == '[':
            answer += temp

        answer_list.pop()
        temp //= 3

if answer_list:
    print(0)
else:
    print(answer)
