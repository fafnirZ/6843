
for i in range(0, 10000):
    if i < 10:
        print(f'000{i}')
    elif i < 100 and i >= 10:
        print(f'00{i}')
    elif i < 1000 and i >= 100:
        print(f'0{i}')
    else:
        print(i)

