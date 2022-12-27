from vector import Vec

my_array = [1, 0, 0]

my_array2 = [0, 1, 0]

v1 = Vec(my_array)
v2 = Vec(my_array2)

print(f"v1 + v2 is equal to: {v1 + v2}")
print(f"v1 dotted with v2 is equal to: {v1 * v2}")
print(f"The length of v1 crossed v2 is equal to: {v1.vector_cross_length(v2, 90)}")
print(f"v1 times the length of v2 is: {v1.vector_length*v2.vector_length}")
print(f"Is v1 orthogonal to v2? {v1.is_orthogonal(v2)}")
print("\\n")
print(v1.properties)
print(v2.properties)