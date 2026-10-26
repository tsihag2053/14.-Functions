#1. Print sum of all even numbers from 10 to 20

total = 0
for num in range(10, 21):
    if num % 2 == 0:
        total += num

print("Sum of all even numbers from 10 to 20:", total)