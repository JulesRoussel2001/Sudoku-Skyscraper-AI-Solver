""" ===-- GThint class -----------*- Python3 -*-===//

This source file is part of the 'AI for Sudoku-Like puzzle' project developed by Jules Roussel.

===----------------------------------------------------------------------===

This is the GTHint class. GTHint instances are compositional elements of the GTHintSkyscraper class.

===----------------------------------------------------------------------===
"""

class GTHint:
  def __init__(self, ext_square_in, comparator_in, int_square_in):
    # Constructor for theGTHint class.

    # Parameters:
    # ext_square_in : The coordinates of the 'visible skyscraper number' square, represented as a tuple.
    # comparator_in : The comprator between the 'visible skyscraper number' square and its adjacent square.
    # int_square_in : The coordinates of the adjacent square, represented as a tuple.
    self.ext_square = ext_square_in
    self.comparator = comparator_in
    self.int_square = int_square_in

  def get_ext_square(self):
    # Retrieves the coordinate of the 'visible skyscraper number' square of the GTHint.

    # Returns: A tuple which represents the row and column indexes of the 'visible skyscraper number' square.
    return self.ext_square
  
  def get_int_square(self):
    # Retrieves the coordinate of the adjacent square of the GTHint.

    # Returns: A tuple which represents the row and column indexes of the adjacent square.
    return self.int_square
  
  def get_comparator(self):
    # Retrieves the comparator between the 'visible skyscraper number' square and its adjacent square.

    # Returns: A string representing the comparator.
    return self.comparator