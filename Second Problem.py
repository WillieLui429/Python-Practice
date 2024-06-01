def hex_to_dec(hex):
    j = 0
    dec = 0
    holder = 0
    for i in reversed(hex):
        if i == '0' or i == '1':
           holder = int(i) * pow(16, j)

        elif hex == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7':
            holder = int(i) * pow(16, j)

        elif hex == '8' or i == '9':
            holder = int(i) * pow(16, j)

        elif i == 'A' or i == 'a':
            holder = (10 * pow(16, j))

        elif i == 'B' or i == 'b':
            holder = (11 * pow(16, j))

        elif i == 'C' or i == 'c':
            holder = (12 * pow(16, j))

        elif i == 'D' or i == 'd':
            holder = (13 * pow(16, j))

        elif i == 'E' or i == 'e':
            holder = (14 * pow(16, j))

        elif i == 'F' or i == 'f':
            holder = (15 * pow(16, j))

        dec = dec + holder
        j = j+1
    return dec

hex = str(input("Enter an hexadecimal number:"))
print(hex_to_dec(hex))