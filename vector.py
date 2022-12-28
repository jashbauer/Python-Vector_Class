
class Vec:

    def __init__(self, x: list):
        self.elements = x
        self.dim = len(x)
        self.vector_length = self.vec_length()
        self.vector_length_squared = self.vector_length**2
        self.v_unit = self.unit_of_v()
        self.properties = {
            "Elements": self.elements,
            "Dimension": self.dim,
            "Length": self.vector_length,
            "Length Squared": self.vector_length_squared,
            "Unit Version": self.v_unit
        }

    def scale(self, c: float) -> list:
        """Returns a c scaled up version of the vector."""
        scaled = [comp*c for comp in self.elements]
        return scaled

    def vec_length(self) -> float:
        """Returns the length (magnitude) of supplied vector."""
        import math
        squared_sum = 0
        for element in self.elements:
            squared_sum += element**2

        return math.sqrt(squared_sum)

    def unit_of_v(self) -> list:
        """Returns unit vector pointing to the same direction of v."""
        unit = []
        for element in self.elements:
            unit.append(element / self.vector_length)

        return unit

    def __add__(self, other_vec):
        """Returns the sum of two vectors."""
        if self.dim != other_vec.dim:
            raise Exception("Vector sum not defined for vectors of unequal dimensions!")
        else:
            summed_vec = []
            for i in range(self.dim):
                summed_vec.append(self.elements[i] + other_vec.elements[i])

            return summed_vec

    def __mul__(self, other_vec):
        """Returns the dot product between two vectors"""
        if self.dim != other_vec.dim:
            raise Exception("Vector dot product not defined for vectors of unequal dimensions!")
        else:
            dotted = 0
            for i in range(self.dim):
                dotted += (self.elements[i])*(other_vec.elements[i])

            return dotted

    def vector_cross_length(self, other_vec, theta):
        """Returns length of cross product between two vectors. Theta must be in degrees."""
        import math
        if self.dim != 3 or other_vec.dim != 3:
            raise Exception("Cross product not defined outside of R3")
        else:
            return self.vector_length*other_vec.vector_length*math.sin(math.radians(theta))

    def is_orthogonal(self, other_vec) -> bool:
        """Returns a boolean indicating orthogonality between two vectors."""
        if self * other_vec == 0:
            return True
        else:
            return False
