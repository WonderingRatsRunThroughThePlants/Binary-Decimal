def changeToBinary(decimal):
    if not (0 <= decimal <= 255):
        print("Has to be between 0 and 255")

    binary = ""

    for i in range(7,-1,-1):
        if decimal & (1 << i):
            binary+="1"
        else:
            binary+="0"
    
    return binary

print(changeToBinary("10"))