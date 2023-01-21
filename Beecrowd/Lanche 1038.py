cod,quant = map(int,input().split())
if cod ==1:
    dogao = 4
    soma_dogao = quant*dogao
    print(f"Total: R$ {soma_dogao:.2f}")
elif cod ==2:
    salada = 4.50
    soma_salada = quant*salada
    print(f"Total: R$ {soma_salada:.2f}")
elif cod == 3:
    bacon = 5
    soma_bacon = quant*bacon
    print(f"Total: R$ {soma_bacon:.2f}")
elif cod == 4:
    torrada = 2
    soma_torrada = quant*torrada
    print(f"Total: R$ {soma_torrada:.2f}")
elif cod == 5:
    refri = 1.50
    soma_refri = quant*refri
    print(f"Total: R$ {soma_refri:.2f}")

