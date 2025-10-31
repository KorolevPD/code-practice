# https://coderun.yandex.ru/problem/speleologist-way

from collections import deque


def get_possible_dirs(v, n):
    moves = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1),
             (0, 0, -1))

    for x, y, z in moves:
        nx, ny, nz = v[0] + x, v[1] + y, v[2] + z
        if 0 <= nx < n and 0 <= ny < n and 0 <= nz < n:
            yield (nx, ny, nz)


space = set()

n = int(input())
for z in range(n):
    empty_line = input().strip()
    for y in range(n):
        for x, block in enumerate(list(input())):
            if block == '.':
                space.add((x, y, z))
            elif block == 'S':
                start = ((x, y, z))

queue = deque([(start, 0)])
visited = {start}
while queue:
    v, dist = queue.popleft()

    if v[2] == 0:
        print(dist)
        break

    for next_dir in get_possible_dirs(v, n):
        if next_dir not in visited and next_dir in space:
            visited.add(next_dir)
            queue.append((next_dir, dist + 1))
