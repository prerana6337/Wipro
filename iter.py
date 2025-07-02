import itertools
data=input("enter characters:")
permute=list(itertools.permutations(data))
print("All Permutations:")
for p in permute:
    print(' '.join(p))