def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    

def subset_set(S):
    if len(S) == 0:
        return [[]]
    else:
        subsets = subset_set(S[1:])
        return subsets + [[S[0]] + subset for subset in subsets]