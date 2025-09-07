from random import randint



def find_min_l(l):
    l_sum = []
    for l_inside_l in l:
        l_sum.append(sum(l_inside_l))

    def i(l, value):
        for i, v in enumerate(l):
            if v == value:
                return i

    return i(l_sum, min(l_sum))



n = int(input('Enter your n\n> '))

print(n-1)

#poland = [randint(-9999, 9999) for i in range(randint(3, 3))]

poland = [1,1,1,1,1,4,1,1,1,7]

print(len(poland))


l_divided = []
for ii in range(n):
    l_divided.append([])


poland.sort(reverse=True)
print(poland)


for i in poland:
    l_divided[find_min_l(l_divided)].append(i)
    


print(l_divided)