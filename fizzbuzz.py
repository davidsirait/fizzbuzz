#!/home/david/miniconda3/envs/pacmann38_wsl/bin/python3

# menerima input angka dari user 
n = int(input("Masukkan angka : "))

# loop dari 1 sampai n dan cetak fizz, buzz atau fizzbuzz
for i in range(1, n+1):
    if i%15==0:
        print("fizzbuzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else:
        print(str(i))
