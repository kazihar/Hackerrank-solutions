
happiness = 0
n , m = (int(i) for i in input().split())
array = list(map(int, input().strip().split()))
A = set(map(int, input().strip().split()))
B = set(map(int, input().strip().split()))

for i in array:
    if i in A:
        happiness += 1
    if i in B:
        happiness -= 1

print(happiness)
