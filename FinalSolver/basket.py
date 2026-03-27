""" ===-- Basket class -----------*- Python3 -*-===//

This source file is part of the 'AI for Sudoku-Like puzzle' project developed by Jules Roussel.

===----------------------------------------------------------------------===

This is the Basket class. Basket instances are compositional elements of the SumBasketSkyscaper class.

===----------------------------------------------------------------------===
"""

class Basket:
  def __init__(self, sum_in, squares_in):
    # Constructor for the Basket class.

    # Parameters:
    # sum_in (int): The target sum for the squares in this basket.
    # squares_in (list of tuple): Coordinates of the squares in this basket, each represented as a tuple.

    self.sum = sum_in
    self.squares = squares_in

  def get_sum(self):
    # Retrieves the sum associated with the basket.

    # Returns: The given sum for the squares in this basket.
    return self.sum

  def get_squares(self):
    # Retrieves the list of squares associated with the basket.

    # Returns: A list of tuples where each tuple represents the row and column indexes of a square that is part of this basket.
    return self.squares