""" ===-- Sum Basket Skyscraper class -----------*- Python3 -*-===//

This source file is part of the 'AI for Sudoku-Like puzzle' project developed by Jules Roussel.

===----------------------------------------------------------------------===

This is the Sum Basket Skyscraper class.

===----------------------------------------------------------------------===
"""

from FinalSolver.skyscraper import Skyscraper
from FinalSolver.basket import Basket

class SumBasketSkyscraper(Skyscraper):
  def __init__(self, board_size_in, baskets_in):
    # Constructor for the Sum Basket Skyscraper class.

    # This constructor extends the Skyscraper class to include functionality for handling baskets.
    # The constructor can handle a dictionary of total sums and lists of coordinates (row, column), and a list of Basket.

    # Parameters:
    # board_size_in (int): The size of the Skyscraper grid.
    # baskets_in : A collection containing the baskets information.
    
    # Attributes:
    #  baskets (list of Basket): Stores the Basket instances corresponding to the baskets in the puzzle.
    super().__init__(board_size_in)
    self.baskets = []
    if baskets_in:
      if isinstance(baskets_in, dict):
        for basket in baskets_in.values():
          self.baskets.append(Basket(basket['sum'], basket['squares']))
      elif isinstance(baskets_in, list): 
        for basket in baskets_in:
          self.baskets.append(basket)

  def apply_variant_inferences(self):
    # Overrides the apply_variant_inferences method from the Skyscraper class to include the inferences specific to Skyscraper with Sum Baskets variant.
    board_size = self.board_size
    for basket in self.baskets:
      unassigned_basket_squares = []
      current_basket_sum = 0
      for square in basket.get_squares():
        (row, col) = square
        if len(self.grid[row][col]) == 1:
          current_basket_sum += next(iter(self.grid[row][col]))
        else:
          unassigned_basket_squares.append((row, col))
      # Apply the first inference of Skyscraper with Sum Baskets.
      if len(unassigned_basket_squares) == 1:
        last_basket_square = self.grid[unassigned_basket_squares[0][0]][unassigned_basket_squares[0][1]]
        value_to_add = basket.get_sum() - current_basket_sum
        if value_to_add in last_basket_square:
          last_basket_square.clear()
          last_basket_square.add(value_to_add)
        else:
          return False
      elif len(unassigned_basket_squares) > 1:
        # Apply the second inference of Skyscraper with Sum Baskets.
        if basket.get_sum() - current_basket_sum <= board_size:
          start_value_to_remove = (basket.get_sum() - current_basket_sum - (len(unassigned_basket_squares) - 1)) + 1
          for i in range(start_value_to_remove, board_size):
            for j in range(0, len(unassigned_basket_squares)):
              self.grid[unassigned_basket_squares[j][0]][unassigned_basket_squares[j][1]].discard(i)
              if not self.grid[unassigned_basket_squares[j][0]][unassigned_basket_squares[j][1]]:
                return False
        # Apply the third inference of Skyscraper with Sum Baskets.
        for i in range(1, board_size):
          if basket.get_sum() - current_basket_sum > (len(unassigned_basket_squares) - 1) * board_size + i:
            for j in range(0, len(unassigned_basket_squares)):
              self.grid[unassigned_basket_squares[j][0]][unassigned_basket_squares[j][1]].discard(i)
              if not self.grid[unassigned_basket_squares[j][0]][unassigned_basket_squares[j][1]]:
                return False
    return True
  
  def is_consistent(self, r, c):
    # Overrides the is_consistent method from the Skyscraper class to include the consistency check based on the 'Sum Baskets' constraint.
    for basket in self.baskets:
      unassigned_basket_squares = []
      current_basket_sum = 0
      for square in basket.get_squares():
        (row, col) = square
        if len(self.grid[row][col]) == 1:
          current_basket_sum += next(iter(self.grid[row][col]))
        else:
          unassigned_basket_squares.append((row, col))
      if len(unassigned_basket_squares) == 0 and basket.get_sum() != current_basket_sum:
          return False
    return super().is_consistent(r, c)



  def successors(self):
    # Overrides the successors method from the Skyscraper class to specifically create SumBasketSkyscraper objects during the value testing process.
    min_options = float('inf')
    min_cell = None
    for i in range(1, self.board_size + 1):
      for j in range(1, self.board_size + 1):
        options = len(self.grid[i][j])
        if 1 < options < min_options:
          min_options = options
          min_cell = (i, j)
    if not min_cell:
      return []

    successors = []
    i, j = min_cell
    for option in self.grid[i][j]:
      test_if_successor = SumBasketSkyscraper(self.board_size, self.baskets)
      for k in range(self.board_size+2):
        for l in range(self.board_size+2):
          test_if_successor.grid[k][l] = self.grid[k][l].copy()
      if test_if_successor.set_square(i, j, option):
        successors.append(test_if_successor)
    return successors
              
  