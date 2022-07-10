import heapq

def solution(jobs):
    answer, time, idx = 0, 0, 0
    start = -1
    ready = []
    size = len(jobs)
    
    while idx < size:
        for job in jobs:
            if start < job[0] <= time:
                heapq.heappush(ready, (job[1], job[0]))
        if ready:
            cur = heapq.heappop(ready)
            start = time
            time += cur[0]
            answer += time - cur[1]
            idx += 1
        else:
            time += 1
        
    return answer // size
