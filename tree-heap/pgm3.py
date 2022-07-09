import heapq

def solution(operations):
    heap = []
    
    for operator in operations:
        if operator != "D 1" and operator != "D -1":
            heapq.heappush(heap, int(operator[1:]))
        elif heap and operator == "D 1":
            heap = heapq.nlargest(len(heap), heap)[1:]
            heapq.heapify(heap)
        elif heap and operator == "D -1":
            heapq.heappop(heap)
            
    if not heap:
        return [0, 0]
    return [heapq.nlargest(1, heap)[0], heapq.heappop(heap)]
