A,B = map(int,input().split())
maior = max(A,B)
menor = min(A,B)
formula = maior%menor
if formula==0:
    print('Sao Multiplos')
else:
    print('Nao sao multiplos')