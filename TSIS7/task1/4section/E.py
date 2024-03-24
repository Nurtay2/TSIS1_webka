N = int(input())

power_of_two = 1
k = 0

# Находим наименьшее целое число k, для которого 2^k >= N
while power_of_two < N:
    power_of_two *= 2
    k += 1

print(k)