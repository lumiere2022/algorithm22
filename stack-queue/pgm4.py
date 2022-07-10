def solution(prices):
    answer = []
    for i in range(len(prices)-1):
        answer.append(0)
        for x in range(i+1, len(prices)):
            answer[-1]+=1
            if prices[i] > prices[x]:
                break
    answer.append(0)
    return answer
