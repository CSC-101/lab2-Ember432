def smallest(n:float, m:float) -> float:
    if n < m:
        return n             # For which calls below is this statement evaluated? None
    else:
        return m

first = smallest(3, 2)       # What is the value of first? 2
second = smallest(2, 2)      # What is the value of second? Is this a reasonable result? Why or why not? 2, not reasonable because 2 is not necessarily "smaller" than 2
print()