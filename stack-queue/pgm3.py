def solution(bridge_length, weight, truck_weights):
    answer = 0
    ing = [0 for _ in range(bridge_length)] #다리의 길이만큼 채우기 -> 길이 유지
    
    while ing:
        answer+=1
        ing.pop(0)
        if truck_weights:
            if sum(ing) + truck_weights[0] <= weight: #순서대로 => 0번째 인덱스에 있는 값 더하기
                truck = truck_weights.pop(0)
                ing.append(truck)
            else:
                ing.append(0) # -> 다리 길이 유지
        
    return answer
