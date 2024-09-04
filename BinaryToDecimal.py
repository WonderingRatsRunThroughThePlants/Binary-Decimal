def changeToDecimal(binary):
    value = 0
    for i in range(len(binary)):
        bit = int(binary[i])

        power = len(binary) - 1 - i

        value += bit * (2**power)
    return value

print(changeToDecimal("01001010"))