def rgb_to_xy(rgb):
    r = float(rgb[0])
    g = float(rgb[1])
    b = float(rgb[2])
    X = 0.412453 * r + 0.357580 * g + 0.180423 * b
    Y = 0.212671 * r + 0.715160 * g + 0.072169 * b
    Z = 0.019334 * r + 0.119193 * g + 0.950227 * b
    x = X / (X + Y + Z)
    y = Y / (X + Y + Z)
    return x, y


def hexa_to_xy(hexa):
    rgb = hexa.lstrip('#')
    rgb = tuple(int(rgb[i:i + 2], 16) for i in (0, 2, 4))
    return rgb_to_xy(rgb=rgb)
