num = int(input("number: "))
bi = bin(num)
bi = bi.replace("0b", "")

print(bi)