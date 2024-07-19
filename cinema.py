def check(n, k, friends):
    flag = False
    while not flag:
        sum_of_friends = sum(friends)
        if sum_of_friends > k:
            flag = False
            reduce(n, k, friends)
        else:
            flag = True
    return flag
    
def reduce(n, k, friends):
    try:
        friends.pop(0)
    except:
        raise("Can't have any employee!")
    check(n, k, friends)

n, k = map(int, input().split())
friends = sorted([int(x) + 1 for x in input().split()], reverse=True)

print(f"{n} {k} {friends}")

