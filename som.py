def compute_multiples_sum(n):
    return sum(i for i in range(1, n) if i % 3 == 0 or i % 5 == 0 or i % 7 == 0)

print(compute_multiples_sum(11))  # 40
print(sum(int(89),int(8)))