def CalcVolume(length, width, height):
    # global area
    area = length * width
    volume = area * height
    return volume


area = 0
volume = CalcVolume(3, 4, 5)
print(area)
