A,B,C = map(float,input().split())
if A<B+C and B<C+A and C<A+B:
    perimetro = A+B+C
    print(f"Perimetro = {perimetro:.1f}")
else:
    formula = (A+B)*C/2
    print(f"Area = {formula:.1f}")

