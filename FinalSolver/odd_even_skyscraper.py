""" ===-- Odd Even Skyscraper class -----------*- Python3 -*-===//

This source file is part of the 'AI for Sudoku-Like puzzle' project developed by Jules Roussel.

===----------------------------------------------------------------------===

This is the Odd Even Skyscraper class.

===----------------------------------------------------------------------===
"""


from FinalSolver.skyscraper import Skyscraper


class OddEvenSkyscraper(Skyscraper):
  def __init__(self, board_size_in, odd_even_grid_in):
    # Cobstructor for OddEvenSkyscraper class.
    # Extends the Skyscraper class to incorporate odd and even constraints on the Skyscraper puzzle grid.
    # 
    # Parameters:
    # board_size_in (int): The size of the Skyscraper puzzle grid.
    # odd_even_grid_in (list of string): A list of string where each characters ('O' for odd and 'E' for even) defines the odd or even constraints for each square in the grid.
    super().__init__(board_size_in)
    self.grid = []
    self.odd_even_grid = odd_even_grid_in
    for i in range(board_size_in + 2):
      row = []
      for j in range(board_size_in + 2):
        if self.odd_even_grid[i][j] == 'E':
            row.append(set(num for num in range(1, board_size_in + 1) if num % 2 == 0))
        elif self.odd_even_grid[i][j] == 'O':
            row.append(set(num for num in range(1, board_size_in + 1) if num % 2 != 0))
        else:
            row.append(set(range(1, board_size_in + 1)))
      self.grid.append(row)

  def apply_variant_inferences(self):
    # Overrides the apply_variant_inferences method from the Skyscraper class to include the inferences specific to Odd/Even Skyscraper.
    board_size_max_index = self.board_size + 1
    board_size = self.board_size
    if self.odd_even_grid:
      for i in range(1, board_size_max_index):
        if self.board_size % 2 == 0:
          # Apply the first inference of odd/even Skyscraper if the grid size is even and if the 'visible skyscraper number' is at the start of the row.
          if self.odd_even_grid[0][i] == 'E' and self.odd_even_grid[1][i] == 'E':
            self.grid[0][i].discard(self.board_size)
            self.grid[1][i].discard(self.board_size)
          elif self.odd_even_grid[0][i] == 'O' and self.odd_even_grid[1][i] == 'O':
            self.grid[0][i].discard(1)
            self.grid[1][i].discard(self.board_size-1)
          # Apply the second inference of odd/even Skyscraper if the grid size is even and if the 'visible skyscraper number' is at the start of the row.
          if self.odd_even_grid[0][i] == 'O' and self.odd_even_grid[2][i] == 'E':
            self.grid[2][i].discard(self.board_size)
          elif self.odd_even_grid[0][i] == 'E' and self.odd_even_grid[2][i] == 'O':
            self.grid[2][i].discard(self.board_size-1)
          # Apply the first inference of odd/even Skyscraper if the grid size is even and if the 'visible skyscraper number' is at the end of the row.
          if self.odd_even_grid[board_size_max_index][i] == 'E' and self.odd_even_grid[board_size_max_index-1][i] == 'E':
            self.grid[board_size_max_index][i].discard(self.board_size)
            self.grid[board_size_max_index-1][i].discard(self.board_size)
          elif self.odd_even_grid[board_size_max_index][i] == 'O' and self.odd_even_grid[board_size_max_index-1][i] == 'O':
            self.grid[board_size_max_index][i].discard(1)
            self.grid[board_size_max_index-1][i].discard(self.board_size-1)
          # Apply the second inference of odd/even Skyscraper if the grid size is even and if the 'visible skyscraper number' is at the end of the row.
          if self.odd_even_grid[board_size_max_index][i] == 'O' and self.odd_even_grid[board_size_max_index-2][i] == 'E':
            self.grid[board_size_max_index-2][i].discard(self.board_size)
          elif self.odd_even_grid[board_size_max_index][i] == 'E' and self.odd_even_grid[board_size_max_index-2][i] == 'O':
            self.grid[board_size_max_index-2][i].discard(self.board_size-1)
          # Apply the first inference of odd/even Skyscraper if the grid size is even and if the 'visible skyscraper number' is at the start of the column.
          if self.odd_even_grid[i][0] == 'E' and self.odd_even_grid[i][1] == 'E':
            self.grid[i][0].discard(self.board_size)
            self.grid[i][1].discard(self.board_size)
          elif self.odd_even_grid[i][0] == 'O' and self.odd_even_grid[i][1] == 'O':
            self.grid[i][0].discard(1)
            self.grid[i][1].discard(self.board_size-1)
          # Apply the second inference of odd/even Skyscraper if the grid size is even and if the 'visible skyscraper number' is at the start of the column.
          if self.odd_even_grid[i][0] == 'O' and self.odd_even_grid[i][2] == 'E':
            self.grid[i][2].discard(self.board_size)
          elif self.odd_even_grid[i][0] == 'E' and self.odd_even_grid[i][2] == 'O':
            self.grid[i][2].discard(self.board_size-1)
          # Apply the first inference of odd/even Skyscraper if the grid size is even and if the 'visible skyscraper number' is at the end of the column.
          if self.odd_even_grid[i][board_size_max_index] == 'E' and self.odd_even_grid[i][board_size_max_index-1] == 'E':
            self.grid[i][board_size_max_index].discard(self.board_size)
            self.grid[i][board_size_max_index-1].discard(self.board_size)
          elif self.odd_even_grid[i][board_size_max_index] == 'O' and self.odd_even_grid[i][board_size_max_index-1] == 'O':
            self.grid[i][board_size_max_index].discard(1)
            self.grid[i][board_size_max_index-1].discard(self.board_size-1)
          # Apply the second inference of odd/even Skyscraper if the grid size is even and if the 'visible skyscraper number' is at the end of the column.
          if self.odd_even_grid[i][board_size_max_index] == 'O' and self.odd_even_grid[i][board_size_max_index-2] == 'E':
            self.grid[i][board_size_max_index-2].discard(self.board_size)
          elif self.odd_even_grid[i][board_size_max_index] == 'E' and self.odd_even_grid[i][board_size_max_index-2] == 'O':
            self.grid[i][board_size_max_index-2].discard(self.board_size-1)
        else:
          # Apply the first inference of odd/even Skyscraper if the grid size is odd and if the 'visible skyscraper number' is at the start of the row.
          if self.odd_even_grid[0][i] == 'E' and self.odd_even_grid[1][i] == 'O':
            self.grid[1][i].discard(self.board_size)
          elif self.odd_even_grid[0][i] == 'O' and self.odd_even_grid[1][i] == 'E':
            self.grid[0][i].discard(1)
            self.grid[0][i].discard(self.board_size)
            self.grid[1][i].discard(self.board_size-1)
          # Apply the second inference of odd/even Skyscraper if the grid size is odd and if the 'visible skyscraper number' is at the start of the row.
          if self.odd_even_grid[0][i] == 'O' and self.odd_even_grid[2][i] == 'O':
            self.grid[2][i].discard(self.board_size)
          elif self.odd_even_grid[0][i] == 'E' and self.odd_even_grid[2][i] == 'E':
            self.grid[2][i].discard(self.board_size-1)
          # Apply the first inference of odd/even Skyscraper if the grid size is odd and if the 'visible skyscraper number' is at the end of the row.
          if self.odd_even_grid[board_size_max_index][i] == 'E' and self.odd_even_grid[board_size_max_index-1][i] == 'O':
            self.grid[board_size_max_index-1][i].discard(self.board_size)
          elif self.odd_even_grid[board_size_max_index][i] == 'O' and self.odd_even_grid[board_size_max_index-1][i] == 'E':
            self.grid[board_size_max_index][i].discard(1)
            self.grid[board_size_max_index][i].discard(self.board_size)
            self.grid[board_size_max_index-1][i].discard(self.board_size-1)
          # Apply the second inference of odd/even Skyscraper if the grid size is odd and if the 'visible skyscraper number' is at the end of the row.
          if self.odd_even_grid[board_size_max_index][i] == 'O' and self.odd_even_grid[board_size_max_index-2][i] == 'O':
            self.grid[board_size_max_index-2][i].discard(self.board_size)
          elif self.odd_even_grid[board_size_max_index][i] == 'E' and self.odd_even_grid[board_size_max_index-2][i] == 'E':
            self.grid[board_size_max_index-2][i].discard(self.board_size-1)
          # Apply the first inference of odd/even Skyscraper if the grid size is odd and if the 'visible skyscraper number' is at the start of the column.
          if self.odd_even_grid[i][0] == 'E' and self.odd_even_grid[i][1] == 'O':
            self.grid[i][1].discard(self.board_size)
          elif self.odd_even_grid[i][0] == 'O' and self.odd_even_grid[i][1] == 'E':
            self.grid[i][0].discard(1)
            self.grid[i][0].discard(self.board_size)
            self.grid[i][1].discard(self.board_size-1)
          # Apply the second inference of odd/even Skyscraper if the grid size is odd and if the 'visible skyscraper number' is at the start of the column.
          if self.odd_even_grid[i][0] == 'O' and self.odd_even_grid[i][2] == 'O':
            self.grid[i][2].discard(self.board_size)
          elif self.odd_even_grid[i][0] == 'E' and self.odd_even_grid[i][2] == 'E':
            self.grid[i][2].discard(self.board_size-1)
          # Apply the first inference of odd/even Skyscraper if the grid size is odd and if the 'visible skyscraper number' is at the end of the column.
          if self.odd_even_grid[i][board_size_max_index] == 'E' and self.odd_even_grid[i][board_size_max_index-1] == 'O':
            self.grid[i][board_size_max_index-1].discard(self.board_size)
          elif self.odd_even_grid[i][board_size_max_index] == 'O' and self.odd_even_grid[i][board_size_max_index-1] == 'E':
            self.grid[i][board_size_max_index].discard(1)
            self.grid[i][board_size_max_index].discard(self.board_size)
            self.grid[i][board_size_max_index-1].discard(self.board_size-1)
          # Apply the second inference of odd/even Skyscraper if the grid size is odd and if the 'visible skyscraper number' is at the end of the column.
          if self.odd_even_grid[i][board_size_max_index] == 'O' and self.odd_even_grid[i][board_size_max_index-2] == 'O':
            self.grid[i][board_size_max_index-2].discard(self.board_size)
          elif self.odd_even_grid[i][board_size_max_index] == 'E' and self.odd_even_grid[i][board_size_max_index-2] == 'E':
            self.grid[i][board_size_max_index-2].discard(self.board_size-1)
        
        # Apply the third inference of odd/even Skyscraper.
        for j in range(1, board_size_max_index):
          if len(self.grid[i][j]) == 1 and next(iter(self.grid[i][j])) == board_size:
            if j > 1:
              self.grid[i][0].discard(1)
            if j < board_size:
              self.grid[i][board_size_max_index].discard(1)
            if i > 1:
              self.grid[0][j].discard(1)
            if i < board_size:
              self.grid[board_size_max_index][j].discard(1)
            for value_to_remove in range(j+1, board_size + 1):
              self.grid[i][0].discard(value_to_remove)
            for value_to_remove in range(board_size - j + 2, board_size + 1):
              self.grid[i][board_size_max_index].discard(value_to_remove)
            for value_to_remove in range(i+1, board_size + 1):
              self.grid[0][j].discard(value_to_remove)
            for value_to_remove in range(board_size - i + 2, board_size + 1):
              self.grid[board_size_max_index][j].discard(value_to_remove)
        if not self.grid[0][i] or not self.grid[1][i] or not self.grid[2][i]:
          return False
        if not self.grid[board_size_max_index][i] or not self.grid[board_size_max_index-1][i] or not self.grid[board_size_max_index-2][i]:
          return False
        if not self.grid[i][0] or not self.grid[i][1] or not self.grid[i][2]:
          return False
        if not self.grid[i][board_size_max_index] or not self.grid[i][board_size_max_index-1] or not self.grid[i][board_size_max_index-2]:
          return False
    return True
  
  def fill_board(self, fill_with):
    # Overrides the fill_board method from the Skyscraper class to adapt to the configuration of the Odd/Even Skyscraper puzzle grid that contains non-digit characters.
    for row in range(len(fill_with)):
      for col in range(len(fill_with)):
        if fill_with[row][col] != ' ' and fill_with[row][col] != 'E' and fill_with[row][col] != 'O':
          value = int(fill_with[row][col])
          self.set_square(row, col, value)

  def successors(self):
    # Overrides the successors method from the Skyscraper class to specifically create OddEvenSkyscraper objects during the value testing process.
    # Additionally, this method prioritises the 'visible skyscraper number' squares during the variable selection process to ensure the Odd/even constraint is effectively managed.
    odd_even_ext_square = None
    ext_squares_coordinate = []
    if self.odd_even_grid:
      for i in range(1, self.board_size + 1):
        ext_squares_coordinate.append((0, i))
        ext_squares_coordinate.append((self.board_size + 1, i))
        ext_squares_coordinate.append((i, 0))
        ext_squares_coordinate.append((i, self.board_size + 1))
      min_options_ext = float('inf')
      for ext_square in ext_squares_coordinate:
        options = len(self.grid[ext_square[0]][ext_square[1]])
        if 1 < options < min_options_ext:
          min_options_ext = options
          odd_even_ext_square = ext_square

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
    if odd_even_ext_square:
      i, j = odd_even_ext_square
    else:
      i, j = min_cell
    for option in self.grid[i][j]:
      test_if_successor = OddEvenSkyscraper(self.board_size, self.odd_even_grid)
      for k in range(self.board_size+2):
        for l in range(self.board_size+2):
          test_if_successor.grid[k][l] = self.grid[k][l].copy()
      if test_if_successor.set_square(i, j, option):
        successors.append(test_if_successor)
    return successors
  