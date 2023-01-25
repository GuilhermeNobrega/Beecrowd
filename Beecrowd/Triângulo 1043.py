A,B,C = map(float,input().split())
maior_lado = max(A,B,C)
print(maior_lado)




A,B,C = map(float,input().split())
if C>A-B and C<B+A and B>C-A and B<A+C and A>C-B and A<B+C:
    print("Perimetro:",A+B+C)
else:
    formula = (A+B)*C/2
    print(f"Area = {formula}")

