bilangan_max = 0

while True:
    bilangan = int(input('masukkan bilangan:'))
    if bilangan == 0 :
        break
    if bilangan > bilangan_max:
        bilangan_max = bilangan

print(f'bilangan terbesar: {bilangan_max}')