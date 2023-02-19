n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
result = 0

for i in range(0, m):
  result += a[b[i] - 1]

print(result)
