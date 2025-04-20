ip = [192, 128, 15, 46]
mask = [255, 255, 255, 240]

address = []
for i in range(0, len(ip)):
    address.append(ip[i] & mask[i])
print(address)
