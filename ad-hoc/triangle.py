# https://coderun.yandex.ru/problem/triangle

a, b, c = sorted(int(input()) for _ in range(3))
print('YES' if a + b > c else 'NO')
