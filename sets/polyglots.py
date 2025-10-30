# https://coderun.yandex.ru/problem/polyglots

unique_set = set()
common_set = set()

for _ in range(int(input())):
    input_set = {input() for _ in range(int(input()))}

    if not common_set:
        common_set |= input_set
    else:
        common_set &= input_set

    unique_set |= input_set

print(len(common_set), *common_set, sep='\n')
print(len(unique_set), *unique_set, sep='\n')
