#inorder(중위 순회)를 반대로 실행

k = int(input())
inputs = list(map(int, input().split()))
tree = [[] for _ in range(k)] #트리를 리스트로 표현 -> 인덱스에 접근하여 출력하기 위해

def make_tree(begin, end, idx):
    if begin == end:
        tree[idx].append(inputs[begin])
        return
    mid = (begin + end) // 2
    tree[idx].append(inputs[mid])
    make_tree(begin, mid-1, idx+1) #왼쪽 자식
    make_tree(mid+1, end, idx+1) #오른쪽 자식

make_tree(0, len(inputs)-1, 0)

for i in range(k):
    for j in tree[i]:
        print(j, end=' ')
    print()
