""" ===-- GT Hint Skyscraper class -----------*- Python3 -*-===//

This source file is part of the 'AI for Sudoku-Like puzzle' project developed by Jules Roussel.

===----------------------------------------------------------------------===

This is the GT Hint Skyscraper class.

===----------------------------------------------------------------------===
"""

from FinalSolver.skyscraper import Skyscraper
from FinalSolver.GThint import GTHint
import math

class GTHintSkyscraper(Skyscraper):
  def __init__(self, board_size_in, GThints_in):
    # Constructor for the GT Hint Skyscraper class.

    # This constructor extends the Skyscraper class to incorporate GTHints which add additional constraints
    # based on comparison between the 'visible skyscrpaer number' square and its adjacent square in the Skyscraper puzzle.
    # The constructor can handle a can handle a dictionary of exterior squares, comparators 
    # and interior squares, corresponding to the ‘visible skyscraper number’, the comparator between 
    # the ‘visible skyscraper number’ and its adjacent square, and its adjacent square, respectively, and a list of GTHint.
    # The exterior squares and interior squares are represented by tuples, corresponding to the square coordinates.

    # Parameters:
    #  board_size_in (int): The size of the Skyscraper puzzle grid.
    # GThints_in : A collection containing the GTHints information.
    
    # Attributes:
    #  GThints (list of GTHint): A list of GTHint instances.
    super().__init__(board_size_in)                            
    self.GThints = []
    if GThints_in:
      if isinstance(GThints_in, dict):
        for GThint in GThints_in.values():
          self.GThints.append(GTHint(GThint['ext_square'], GThint['comparator'], GThint['int_square']))
      elif isinstance(GThints_in, list): 
        for GThint in GThints_in:
          self.GThints.append(GThint)

  def apply_variant_inferences(self):
     # Overrides the apply_variant_inferences method from the Skyscraper class to include the inferences specific to Skyscraper with GTHint.
    for GThint in self.GThints:
      ext_square_coordinate = GThint.get_ext_square()
      int_square_coordinate = GThint.get_int_square()
      comparator = GThint.get_comparator()
      # Apply the first inference for Skyscraper with GTHint.
      if comparator == '=':
        self.grid[ext_square_coordinate[0]][ext_square_coordinate[1]].discard(1)
        self.grid[int_square_coordinate[0]][int_square_coordinate[1]].discard(1)
        if self.board_size % 2 == 0:
          half_board_size = (self.board_size / 2) + 1
          for i in range(half_board_size, self.board_size+1):
            self.grid[ext_square_coordinate[0]][ext_square_coordinate[1]].discard(i)
            self.grid[int_square_coordinate[0]][int_square_coordinate[1]].discard(i)
        else:
          half_board_size = math.floor(self.board_size / 2)
          for i in range(0, half_board_size):
            self.grid[ext_square_coordinate[0]][ext_square_coordinate[1]].discard(self.board_size - i)
            self.grid[int_square_coordinate[0]][int_square_coordinate[1]].discard(self.board_size - i)
      # Apply the second inference for Skyscraper with GTHint.
      elif comparator == '>':
        self.grid[ext_square_coordinate[0]][ext_square_coordinate[1]].discard(1)
        if self.board_size % 2 == 0:
          half_board_size = (self.board_size / 2) + 1
          for i in range(half_board_size, self.board_size+1):
            self.grid[int_square_coordinate[0]][int_square_coordinate[1]].discard(i)
        else:
          half_board_size = math.ceil(self.board_size / 2)
          for i in range(half_board_size, self.board_size+1):
            self.grid[int_square_coordinate[0]][int_square_coordinate[1]].discard(i)
      # Apply the third inference for Skyscraper with GTHint.
      elif comparator == '<':
        self.grid[int_square_coordinate[0]][int_square_coordinate[1]].discard(1)
        self.grid[int_square_coordinate[0]][int_square_coordinate[1]].discard(2)
        if self.board_size % 2 == 0:
          half_board_size = (self.board_size / 2) + 1
          for i in range(half_board_size, self.board_size+1):
            self.grid[ext_square_coordinate[0]][ext_square_coordinate[1]].discard(i)
        else:
          half_board_size = math.ceil(self.board_size / 2)
          for i in range(half_board_size, self.board_size+1):
            self.grid[ext_square_coordinate[0]][ext_square_coordinate[1]].discard(i)
      if not self.grid[ext_square_coordinate[0]][ext_square_coordinate[1]] or not self.grid[int_square_coordinate[0]][int_square_coordinate[1]]:
        return False
    return True
  
  def is_consistent(self, r, c):
    # Overrides the is_consistent method from the Skyscraper class to include the consistency check based on the 'GTHints' constraint.
    for GThint in self.GThints:
      ext_square_coordinate = GThint.get_ext_square()
      int_square_coordinate = GThint.get_int_square()
      comparator = GThint.get_comparator()
      ext_square = self.grid[ext_square_coordinate[0]][ext_square_coordinate[1]]
      int_square = self.grid[int_square_coordinate[0]][int_square_coordinate[1]]
      if len(ext_square) == 1 and len(int_square) == 1:
        if comparator == ">" and next(iter(ext_square)) <= next(iter(int_square)) or comparator == "=" and next(iter(ext_square)) != next(iter(int_square)) or comparator == "<" and next(iter(ext_square)) >= next(iter(int_square)):
          return False
    return super().is_consistent(r, c)

  def successors(self):
    # Overrides the successors method from the Skyscraper class to specifically create GTHintSkyscraper objects during the value testing process.
    # Additionally, this method prioritises the 'visible skyscraper number' squares during the variable selection process to ensure the GTHint constraint is effectively managed.

    GThint_ext_square = None
    for GThint in self.GThints:
      ext_square = GThint.get_ext_square()
      if len(self.grid[ext_square[0]][ext_square[1]]) != 1:
        GThint_ext_square = ext_square
        break

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
    if GThint_ext_square: 
      i, j = GThint_ext_square
    else:
      i, j = min_cell
    for option in self.grid[i][j]:
      test_if_successor = GTHintSkyscraper(self.board_size, self.GThints)
      for k in range(self.board_size+2):
        for l in range(self.board_size+2):
          test_if_successor.grid[k][l] = self.grid[k][l].copy()
      if test_if_successor.set_square(i, j, option):
        successors.append(test_if_successor)
    return successors
              