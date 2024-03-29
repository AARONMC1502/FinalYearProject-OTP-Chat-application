import binascii

def toText(binary):
    text = "".join([chr(int(binary[i: i + 8], 2)) for i in range(0, len(binary), 8)])
    return text

def toBinary(text, *kwargs):
    byteText = bytes(text, *kwargs)
    binText = bin(int(binascii.hexlify(byteText), 16))

    if len(binText) % 8 != 0:
        formattedBinMessage = "0" + binText[2:]
    else:
        formattedBinMessage = binText[2:]

    return formattedBinMessage

def HMACToBinary(text, *kwargs):
    byteText = bytes(text, *kwargs)
    binText = bin(int(binascii.hexlify(byteText), 16))[2:]

    while True:
        if len(binText) < 512:
            binText = "".join(("0", binText))
        else:
            break
    return binText