# Version 0.3 - Alpha - Wed 5 April 2023.
# This should be a general (geometric) Vector implementation (any column size).

import math

"""
    Mathematical Vector (Row Vector, 1 by n Matrix)
"""
class Vector ():
    """
        Initialize the Vector given a row_vector:list.
        Raises ValueError if row_vector:list is empty
    """
    def __init__ (self, row_vector:list):
        if len (row_vector) == 0:
            raise ValueError
        self.row = row_vector[:]        # Store a copy, not a reference
        self.dim = len (row_vector)

    """
        Vector Addition
        Raises ValueError if used on anything other than Vectors.
        Raises ValueError if dimensions are different. 
    """
    def __add__ (self, other):
        if type (other) == Vector and self.dim == other.dim:
            C = [a + b for a, b in zip (self.row, other.row)]
            return Vector (C)
        else:
            raise ValueError
        

    """
        Scalar Vector multiplication
    """
    def __mul__ (self, scalar):
        return (Vector ([scalar * x for x in self.row]))
    def __rmul__ (self, scalar):
        return (Vector.__mul__ (self, scalar))

    """
        Vector Subtraction defined as
        A + (-B).
        Raises ValueError if used on anything other than Vectors.
        Raises ValueError if dimensions are different.
    """
    def __sub__ (self, other):
        if type (other) == Vector and self.dim == other.dim:
            return (self + (-1) * other)
        else:
            raise ValueError
    
    """
        The magnitude of the Vector,
        not using the Inner (Dot) Product,
        but Pythagoras.
        This should be redefined;
        The VectorSpace decides the InnerProduct,
        and "length" is defined as: <Vec1, Vec1> ^ 1/2
    """
    def __abs__ (self):
        # Pythagorean one
        #return sum ( [x ** 2 for x in self.row] ) ** (1/2)
        # Inner product
        return (Vector.dotP(self, self) ** (1/2))

    """
        Returns something printable
    """
    def __str__ (self):
        return "1x%d Vector\n" % (self.dim) + str (self.row)
    
    """
        Dot Product of two Vectors.
        This would be an Inner Product.
        Defined by sum of multiplication of the elements.
    """
    def dotP (self, other):
        return sum ([a * b for a, b in zip (self.row, other.row)])
    
    """
        TODO: Cross Product
        Having Vectors as a child class of a parent Matrix class would make this easier.
    """
    
    """
        Get the absolute valued distance from A to B, same as B - A.
    """
    def distance (A, B):
        return (abs (B - A))
    
    """
        Get the direction from A to B, same as B - A.
    Maybe Normalize this(?)
    """
    def direction (A, B):
        return (B - A)
    
    """
        Return a Normalized version of the vector.
        abs == 1
    """
    def normalize (self):
        return self * (1.0 / abs (self))

# Run a feature test
if __name__ == "__main__":
    print ("This file is not meant to be run as __main__, only for testing!\n")
    
    A = Vector ([1, 0])
    B = Vector ([0, 1])
    C = abs (B - A)
    print ("%s" % (C))

