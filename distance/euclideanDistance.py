import math

def euclidean_distance(point1, point2):
    """İki nokta arasındaki Öklid mesafesini hesaplar."""
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
