# Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.

n = int(input("Numbers of Sequence: "))
seq = []

for i in range(n):
    if len(seq) < 2:
        seq.append(1)
    else:
        seq.append(seq[i-2] + seq[i-1])

print(seq)