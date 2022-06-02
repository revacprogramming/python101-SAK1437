
count = 0
sum = 0
try:
    while True:
        num = input("Enter a number: ")
        if num == "done":
            break
        sum += int(num)
        count += 1
    print(count,sum,sum/count)
except ValueError :    
    print('invalid entry')