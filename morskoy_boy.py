l_of_ships = [0]+list(reversed(list(map(int, input('Enter (XL, L, M, S)> ').split(' ')))))
field_size = int(input('Enter n> '))
print(l_of_ships)


def get_index(l):
    for ship in range(len(l)-1, 0, -1):
        if l[ship]>0:
            return ship


f = lambda n, x: n-x-1

field_list = []
for i in range(field_size):
    print(l_of_ships)
    bigest_ship_index = get_index(l_of_ships)
    next_ship_size = f(field_size, bigest_ship_index)
    l_of_ships[bigest_ship_index] = l_of_ships[bigest_ship_index]-1
    l_of_ships[next_ship_size] = l_of_ships[next_ship_size]-1
    field_list.append([bigest_ship_index, next_ship_size])

print(field_list)