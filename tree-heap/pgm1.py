import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville:
        num1 = heapq.heappop(scoville)
        if num1 < K:
            if not scoville:
                return -1
            num2 = heapq.heappop(scoville)
            heapq.heappush(scoville, num1 + num2*2)
            answer+=1
        else:
            return answer
