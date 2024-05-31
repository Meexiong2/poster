# for x in range(2,13):
#     print(f'formula = {x}')
#     for y in range(1,13):
#         print(f'{x} x {y} = {x*y}')

start = int(input('start formula = '))
stop = int(input('stop formula = '))

for x in range(start,stop+1):
    print(f'formula = {x}')
    for y in range(1,13):
        print(f'{x} x {y} = {x*y}')