# https://coderun.yandex.ru/problem/nvp-with-response-recovery

input()
max = 0
result = []
for n in map(int, input().split()):
    for n in map(int, input().split()):
        if n >= max:
            max = n
            result.append(str(n))

print(' '.join(result))
