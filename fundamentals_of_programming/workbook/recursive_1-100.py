def seq(n):
    if n > 0:
        seq(n-1)
    print(n)  # stack


seq(100)
