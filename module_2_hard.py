import random
def exit():
    list_ = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    lock = random.choice(list_)
    keys = []
    for j in range(1, lock):
        for k in range(j+1, lock):
            if lock % (j + k) == 0:
                    keys.append(f'{j} + {k}')
    return f'lock{lock}, keys{keys}'
result = exit()
print(result)


