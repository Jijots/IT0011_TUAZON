A = {'a', 'g', 'b', 'c', 'd', 'f'}
B = {'b', 'c', 'h', 'l', 'm', 'o'}
C = {'c', 'd', 'f', 'j', 'k'}

a_result = len(A | B)
print(f"a. Elements in A and B: {a_result}")

b_result = B - (A | C)
print(f"b. Elements in B that are not in A and C: {b_result} (Count: {len(b_result)})")

c1 = {'h', 'i', 'j', 'k'}
c2 = A & C
c3 = (A & B) | {'h'}
c4 = A & C - B
c5 = A & B & C
c6 = B - (A | C)

print(f"c.i: {c1}")
print(f"c.ii: {c2}")
print(f"c.iii: {c3}")
print(f"c.iv: {c4}")
print(f"c.v: {c5}")
print(f"c.vi: {c6}")
