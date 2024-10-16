from distance.euclideanDistance import euclidean_distance

# 2D uzayda noktalar
points = [(2, 3), (5, 7), (1, 9), (8, 2), (3, 3)]

# Mesafeleri saklamak için liste
distances = []

# Her iki nokta arasındaki mesafeyi hesapla
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclidean_distance(points[i], points[j])
        distances.append(distance)

# Minimum mesafeyi bul ve yazdır
min_distance = min(distances)
print("Minimum Öklid Mesafesi:", min_distance)

