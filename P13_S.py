tuple1 = (45,453,24,4,534,6,534,234324,32423,4,324,3,454541,1)

def tuple_avg(a_tuple):
    count = 0
    total = 0
    for i in a_tuple:
        print(a_tuple[count])
        count += 1
        total += i
    print("Average:", total/count)

tuple_avg(tuple1)
