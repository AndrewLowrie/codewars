def fake_bin(fakebinary):
    numbers = [int(i) for i in fakebinary]
    return ''.join(['1' if (i >= 5) else '0' for i in numbers])

print fake_bin("45385593107843568")
#01011110001100111
