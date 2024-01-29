def row_sum_odd_numbers(n):
    #your code here
    r = 1
    sum = 0
    siste_tall = -1
    for i in range(n):
        sum = 0
        for a in range(r):
            siste_tall += 2
            sum+=siste_tall
        r+=1
    return sum

print(row_sum_odd_numbers(2))
print(row_sum_odd_numbers(4))