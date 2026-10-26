#3. Print all even and odd numbers from 1 to 10

n = 10
print("Even numbers from 1 to", n, ":")
for i in range(1, 11):
    if i % 2 == 0:
        print(i)

print("Odd numbers from 1 to", n, ":")
for i in range(1, 11):
    if i % 2 != 0:
        print(i)