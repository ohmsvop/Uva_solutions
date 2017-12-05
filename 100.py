# The 3n + 1 problem

cycle_dict = {1:1}

def calculate_cycle(int_list):
    n = int_list[-1]
    if n not in cycle_dict.keys():
        if n % 2 == 0:
            int_list.append(int(n/2))
        else:
            int_list.append(3 * n + 1)
        calculate_cycle(int_list)
    else:
        int_list.reverse()
        for i in range(len(int_list)):
            cycle_dict[int_list[i]] = cycle_dict[int_list[0]] + i

def maximum_cycle(i,j):
    if i > j:
        i,j = j,i
    max_cycle = 0
    max_cycle_index = 0
    for n in range(i,j+1):
        calculate_cycle([n])
        if cycle_dict[n] > max_cycle:
            max_cycle = cycle_dict[n]
            max_cycle_index = n
    return max_cycle

while True:
    try:
        user_input = input()
        i,j = map(int,user_input.split())
        max_cycle = maximum_cycle(i,j)
        print(i, j, max_cycle)    
    except:
        break

#print(maximun_cycle(1,10))