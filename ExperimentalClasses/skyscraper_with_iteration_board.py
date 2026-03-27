""" ===-- Skyscraper class -----------*- Python3 -*-===//

This source file is part of the 'AI for Sudoku-Like puzzle' project developed by Jules Roussel.

===----------------------------------------------------------------------===

This is the Skyscraper class which employs a iteration board strategy rather than a queue strategy.
Although this class is not used in the final version of the solver, it is employed for the evaluation part of the project.

===----------------------------------------------------------------------===
"""
from FinalSolver.puzzle import Puzzle
from collections import deque

class Skyscraper(Puzzle):
  def __init__(self, board_size_in):
  #Constructor for the Skyscraper puzzle class.

  #Extends the Puzzle class to fit the Skyscraper puzzle specifics by adjusting the grid dimensions 
  #to accommodate 'visible skyscraper numbers' around the grid. These are clues given at the 
  #start and end of each row and column.
  #
  # Parameters:
  # board_size_in : Represents the size of the grid exclusive of the visible skyscraper clues.
  #                 The actual grid will have two extra rows and columns to accommodate these clues.

  # Attributes:
  # grid (list of list of sets): Initializes a grid where each cell starts with a full set of possible 
  #                              numbers from 1 to board_size_in. The grid includes an extra row and 
  #                              column at the beginning and end to handle the visible skyscraper numbers.
    super().__init__(board_size_in)
    self.grid = []
    self.grid = [[set(range(1, board_size_in + 1)) for _ in range(board_size_in + 2)] for _ in range(board_size_in + 2)]

  def constraint_propagation(self, row, col):
    # Implements the specific Skyscraper puzzle constraint propagation.

    # Overrides the abstract constraint_propagation method from the Puzzle class to handle
    # constraints specific to Skyscraper puzzles.

    # Parameters:
    # row (int): The row index of the cell where a new value has been set.
    # col (int): The column index of the cell where a new value has been set.

    # Returns:
    # bool: True if the propagation does not find any inconsistence, False otherwise.
    board_size = self.board_size
    board_size_with_visible_skyscraper_numbers = self.board_size + 2
    board_size_max_index = self.board_size + 1
    main_counter = 0
    if row == 0 and col in range(1,board_size_max_index):
      # Apply the first starting inference if the 'visible skyscraper number' square is at the first row.
      if next(iter(self.grid[0][col])) == 1:
        self.grid[1][col] = {board_size}
      # Apply the second starting inference if the 'visible skyscraper number' square is at the first row.
      elif next(iter(self.grid[0][col])) == board_size:
        for i in range(1, board_size + 1):
          self.grid[i][col] = {i}
      else:
        # Apply the fourth starting inference if the 'visible skyscraper number' square is at the first row.
        if next(iter(self.grid[0][col])) == 2:
          self.grid[2][col].discard(board_size-1)
        # Apply the third starting inference if the 'visible skyscraper number' square is at the first row.
        for i in range(1, next(iter(self.grid[0][col]))):
          counter = board_size
          while counter > board_size - i:
            self.grid[next(iter(self.grid[0][col]))-i][col].discard(counter)
            counter -= 1
          if not self.grid[next(iter(self.grid[0][col]))-i][col]:
            return False
    if row in range(1,board_size_max_index) and col == 0:
      # Apply the first starting inference if the 'visible skyscraper number' square is at the first column.
      if next(iter(self.grid[row][0])) == 1:
        self.grid[row][1] = {board_size}
      # Apply the second starting inference if the 'visible skyscraper number' square is at the first column.
      elif next(iter(self.grid[row][0])) == board_size:
        for i in range(1, board_size + 1):
          self.grid[row][i] = {i}
      else:
        # Apply the fourth starting inference if the 'visible skyscraper number' square is at the first column.
        if next(iter(self.grid[row][0])) == 2:
          self.grid[row][2].discard(board_size-1)
        # Apply the third starting inference if the 'visible skyscraper number' square is at the first column.
        for i in range(1, next(iter(self.grid[row][0]))):
          counter = board_size
          while counter > board_size - i:
            self.grid[row][next(iter(self.grid[row][0]))-i].discard(counter)
            counter -= 1
          if not self.grid[row][next(iter(self.grid[row][0]))-i]:
            return False
    if row == board_size_max_index and col in range(1,board_size_max_index):
      # Apply the first starting inference if the 'visible skyscraper number' square is at the last row.
      if next(iter(self.grid[board_size_max_index][col])) == 1:
        self.grid[board_size_max_index-1][col] = {board_size}
      # Apply the second starting inference if the 'visible skyscraper number' square is at the last row.
      elif next(iter(self.grid[board_size_max_index][col])) == board_size:
        for i in range(1, board_size + 1):
          self.grid[i][col] = {board_size + 1 - i}
      else:
        # Apply the fourth starting inference if the 'visible skyscraper number' square is at the last row.
        if next(iter(self.grid[board_size_max_index][col])) == 2:
          self.grid[board_size_max_index-2][col].discard(board_size-1)
        # Apply the third starting inference if the 'visible skyscraper number' square is at the last row.
        for i in range(1, next(iter(self.grid[board_size_max_index][col]))):
          counter = board_size
          while counter > board_size - i:
            self.grid[board_size_max_index - next(iter(self.grid[board_size_max_index][col])) + i][col].discard(counter)
            counter -= 1
          if not self.grid[board_size_max_index - next(iter(self.grid[board_size_max_index][col])) + i][col]:
            return False
    if row in range(1, board_size_max_index) and col == board_size_max_index:
      # Apply the first starting inference if the 'visible skyscraper number' square is at the last column.
      if next(iter(self.grid[row][board_size_max_index])) == 1:
        self.grid[row][board_size_max_index-1] = {board_size}
      # Apply the second starting inference if the 'visible skyscraper number' square is at the last column. 
      elif next(iter(self.grid[row][board_size_max_index])) == board_size:
        for i in range(1, board_size + 1):
          self.grid[row][i] = {board_size + 1 - i}
      else:
        # Apply the fourth starting inference if the 'visible skyscraper number' square is at the last column.
        if next(iter(self.grid[row][board_size_max_index])) == 2:
          self.grid[row][board_size_max_index-2].add(board_size-1)
        # Apply the third starting inference if the 'visible skyscraper number' square is at the last column.
        for i in range(1, next(iter(self.grid[row][board_size_max_index]))):
          counter = board_size
          while counter > board_size - i:
            self.grid[row][board_size_max_index - next(iter(self.grid[row][board_size_max_index])) + i].discard(counter)
            counter -= 1
          if not self.grid[row][board_size_max_index - next(iter(self.grid[row][board_size_max_index])) + i]:
            return False
    # Start the constraint propagation process
    while main_counter == 0:
      main_counter = 1
      # Apply the variant inferences
      if not self.apply_variant_inferences():
        return False
      for i in range(1, board_size_max_index):
        for j in range(1, board_size_max_index):
          # Apply the third advanced inference.
          current_set = self.grid[i][j]
          if len(current_set) > 1:
            for val in current_set:
              unique_in_row = True
              for k in range(1,board_size_max_index):
                if k != j:
                  if val in self.grid[i][k]:
                    unique_in_row = False
                    break
              if unique_in_row:
                self.grid[i][j].clear()
                self.grid[i][j].add(val)
                main_counter = 1
                break    
              unique_in_column = True
              for k in range(1,board_size_max_index):
                if k != i:
                  if val in self.grid[k][j]:
                    unique_in_column = False
                    break         
              if unique_in_column:
                self.grid[i][j].clear()
                self.grid[i][j].add(val)
                main_counter = 1
                break


          # Apply the first advanced inference.
          if len(self.grid[i][j]) == 1:
            value_to_remove = next(iter(self.grid[i][j]))
            for k in range(1,board_size_max_index):
              if k != i:
                if value_to_remove in self.grid[k][j]:
                  self.grid[k][j].discard(value_to_remove)
                  if not self.grid[k][j]:
                    return False
                  main_counter = 1
              if k != j:
                if value_to_remove in self.grid[i][k]:
                  self.grid[i][k].discard(value_to_remove)
                  if not self.grid[i][k]:
                    return False
                  main_counter = 1
          # Apply the second advanced inference.
          if len(self.grid[i][j]) == 2:
            for k in range(1,board_size_max_index):
              if k != i:
                if self.grid[i][j] == self.grid[k][j]:
                  for value_to_remove in self.grid[i][j]:
                    for l in range(1,board_size_max_index):
                      if l != i and l != k:
                        if value_to_remove in self.grid[l][j]:
                          self.grid[l][j].discard(value_to_remove)
                          if not self.grid[l][j]:
                            return False
                          main_counter = 1
              if k != j:
                if self.grid[i][j] == self.grid[i][k]:
                  for value_to_remove in self.grid[i][j]:
                    for l in range(1,board_size_max_index):
                      if l != j and l != k:
                        if value_to_remove in self.grid[i][l]:
                          self.grid[i][l].discard(value_to_remove)
                          if not self.grid[i][l]:
                            return False
                          main_counter = 1
          # Verify the consistency of the modified Skysraper puzzle by the inferences.
          if not self.is_consistent(i, j):
            return False
        
        if board_size < 8:
          row_to_check = self.grid[i][1:-1]
          row_to_check_with_visible_skyscraper_numbers = self.grid[i]
          # Apply the fourth advanced inference if the 'visible skyscraper number' square is at the first row.
          if len(row_to_check_with_visible_skyscraper_numbers[0]) == 1:
            visible_skyscraper_number = next(iter(row_to_check_with_visible_skyscraper_numbers[0]))
          else:
            visible_skyscraper_number = 0
          if visible_skyscraper_number > 1 and visible_skyscraper_number < board_size - 1:
            if len(row_to_check[0]) > 1:
              if visible_skyscraper_number == 2 and {board_size} in row_to_check:
                index = row_to_check.index({board_size})
                for j in range(1, index):
                  self.grid[i][1].discard(j)
                if not self.grid[i][1]:
                  return False
              if visible_skyscraper_number == 3 and {board_size} in row_to_check and {board_size-1} in row_to_check:
                index_sup = row_to_check.index({board_size})
                index_inf = row_to_check.index({board_size-1})
                if index_sup > index_inf:
                  for j in range(1, index_inf):
                    self.grid[i][1].discard(j)
                else:
                  self.grid[i][1].discard(board_size-2)
                if not self.grid[i][1]:
                  return False
              if visible_skyscraper_number == 4 and {board_size} in row_to_check and {board_size-1} in row_to_check and {board_size-2} in row_to_check:
                index_sup = row_to_check.index({board_size})
                index_mid = row_to_check.index({board_size - 1})
                index_inf = row_to_check.index({board_size - 2})
                if index_sup > index_mid and index_mid > index_inf:
                  for j in range(1, index_inf):
                    self.grid[i][1].discard(j)
                if index_mid > index_sup > index_inf or index_inf > index_sup > index_mid:
                  self.grid[i][1].discard(board_size - 3)
                if index_sup < index_mid and index_sup < index_inf:
                  self.grid[i][1].discard(board_size - 3)
                  self.grid[i][1].discard(board_size - 4)
                if not self.grid[i][1]:
                  return False
          # Apply the fourth advanced inference if the 'visible skyscraper number' square is at the last row.
          if len(row_to_check_with_visible_skyscraper_numbers[board_size_max_index]) == 1:
            visible_skyscraper_number = next(iter(row_to_check_with_visible_skyscraper_numbers[board_size_max_index]))
          else:
            visible_skyscraper_number = 0
          if visible_skyscraper_number > 1 and visible_skyscraper_number < board_size - 1:
            if len(row_to_check[board_size-1]) > 1:
              if visible_skyscraper_number == 2 and {board_size} in row_to_check:
                index = row_to_check.index({board_size})
                for j in range(1, board_size - index - 1):
                  self.grid[i][board_size].discard(j)
                if not self.grid[i][board_size]:
                  return False
              if visible_skyscraper_number == 3 and {board_size} in row_to_check and {board_size - 1} in row_to_check:
                index_sup = row_to_check.index({board_size})
                index_inf = row_to_check.index({board_size - 1})
                if index_sup < index_inf:
                  for j in range(1, board_size-index_inf-1):
                    self.grid[i][board_size].discard(j)
                else:
                  self.grid[i][board_size].discard(board_size-2)
                if not self.grid[i][board_size]:
                  return False
              if visible_skyscraper_number == 4 and {board_size} in row_to_check and {board_size - 1} in row_to_check and {board_size - 2} in row_to_check:
                index_sup = row_to_check.index({board_size})
                index_mid = row_to_check.index({board_size - 1})
                index_inf = row_to_check.index({board_size - 2})
                if index_sup < index_mid and index_mid < index_inf:
                  for j in range(1, board_size-index_inf-1):
                    self.grid[i][board_size].discard(j)
                if index_mid < index_sup < index_inf or index_inf < index_sup < index_mid:
                  self.grid[i][board_size].discard(board_size-3)
                if index_sup > index_mid and index_sup > index_inf:
                  self.grid[i][board_size].discard(board_size-3)
                  self.grid[i][board_size].discard(board_size-4)
                if not self.grid[i][board_size]:
                  return False
          column_to_check = [self.grid[j][i] for j in range(1, board_size+1)]
          column_to_check_with_visible_skyscraper_numbers = [self.grid[j][i] for j in range(board_size_with_visible_skyscraper_numbers)]
          # Apply the fourth advanced inference if the 'visible skyscraper number' square is at the first column.
          if len(column_to_check_with_visible_skyscraper_numbers[0]) == 1:
            visible_skyscraper_number = next(iter(column_to_check_with_visible_skyscraper_numbers[0]))
          else:
            visible_skyscraper_number = 0
          if visible_skyscraper_number > 1 and visible_skyscraper_number < board_size - 1:
            if len(column_to_check[0]) > 1:
              if visible_skyscraper_number == 2 and {board_size} in column_to_check:
                index = column_to_check.index({board_size})
                for j in range(1, index):
                  self.grid[1][i].discard(j)
                if not self.grid[1][i]:
                  return False
              if visible_skyscraper_number == 3 and {board_size} in column_to_check and {board_size-1} in column_to_check:
                index_sup = column_to_check.index({board_size})
                index_inf = column_to_check.index({board_size-1})
                if index_sup > index_inf:
                  for j in range(1, index_inf):
                    self.grid[1][i].discard(j)
                else:
                  self.grid[1][i].discard(board_size - 2)
                if not self.grid[1][i]:
                  return False
              if visible_skyscraper_number == 4 and {board_size} in column_to_check and {board_size - 1} in column_to_check and {board_size - 2} in column_to_check:
                index_sup = column_to_check.index({board_size})
                index_mid = column_to_check.index({board_size-1})
                index_inf = column_to_check.index({board_size-2})
                if index_sup > index_mid and index_mid > index_inf:
                  for j in range(1, index_inf):
                    self.grid[1][i].discard(j)
                if index_mid > index_sup > index_inf or index_inf > index_sup > index_mid:
                  self.grid[1][i].discard(board_size - 3)
                if index_sup < index_mid and index_sup < index_inf:
                  self.grid[1][i].discard(board_size - 3)
                  self.grid[1][i].discard(board_size - 4)
                if not self.grid[1][i]:
                  return False
          # Apply the fourth advanced inference if the 'visible skyscraper number' square is at the last column.
          if len(column_to_check_with_visible_skyscraper_numbers[board_size_max_index]) == 1:
            visible_skyscraper_number = next(iter(column_to_check_with_visible_skyscraper_numbers[board_size_max_index]))
          else:
            visible_skyscraper_number = 0
          if visible_skyscraper_number > 1 and visible_skyscraper_number < board_size - 1:
            if len(column_to_check[board_size-1]) > 1:
              if visible_skyscraper_number == 2 and {board_size} in column_to_check:
                index = column_to_check.index({board_size})
                for j in range(1, board_size - index - 1):
                  self.grid[board_size][i].discard(j)
                if not self.grid[board_size][i]:
                  return False
              if visible_skyscraper_number == 3 and {board_size} in column_to_check and {board_size - 1} in column_to_check:
                index_sup = column_to_check.index({board_size})
                index_inf = column_to_check.index({board_size - 1})
                if index_sup < index_inf:
                  for j in range(1, board_size-index_inf-1):
                    self.grid[board_size][i].discard(j)
                else:
                  self.grid[board_size][i].discard(board_size - 2)
                if not self.grid[board_size][i]:
                  return False
              if visible_skyscraper_number == 4 and {board_size} in column_to_check and {board_size - 1} in column_to_check and {board_size - 2} in column_to_check:
                index_sup = column_to_check.index({board_size})
                index_mid = column_to_check.index({board_size - 1})
                index_inf = column_to_check.index({board_size - 2})
                if index_sup < index_mid and index_mid < index_inf:
                  for j in range(1, board_size-index_inf-1):
                    self.grid[board_size][i].discard(j)
                if index_mid < index_sup < index_inf or index_inf < index_sup < index_mid:
                  self.grid[board_size][i].discard(board_size - 3)
                if index_sup > index_mid and index_sup > index_inf:
                  self.grid[board_size][i].discard(board_size - 3)
                  self.grid[board_size][i].discard(board_size - 4)
                if not self.grid[board_size][i]:
                  return False
              
        else:
          row_to_check = self.grid[i][1:-1]
          row_to_check_with_visible_skyscraper_numbers = [set(val) for val in self.grid[i]]
          # Apply the fifth advanced inference if the 'visible skyscraper number' square is at the first row.                     
          if len(row_to_check_with_visible_skyscraper_numbers[0]) == 1:
            visible_skyscraper_number = next(iter(row_to_check_with_visible_skyscraper_numbers[0]))
          else:
            visible_skyscraper_number = 0
          if visible_skyscraper_number > 1 and visible_skyscraper_number < board_size - 1:
            biggest_smallest_number = 0
            visible_skycrapers = 0
            highest_building_value = 0
            indexes_biggest_numbers = []
            num_empty_squares = 0
            for counter in range(0, board_size):
              if {board_size-counter} in row_to_check:
                biggest_smallest_number = board_size-counter
                indexes_biggest_numbers.append(row_to_check.index({board_size-counter})+1)
              else:
                break
            if biggest_smallest_number > 0:
              minimum_index_of_biggest_numbers = min(indexes_biggest_numbers)
              for index in range(minimum_index_of_biggest_numbers, board_size_max_index):
                if next(iter(row_to_check_with_visible_skyscraper_numbers[index])) > highest_building_value:
                  highest_building_value = next(iter(row_to_check_with_visible_skyscraper_numbers[index]))
                  visible_skycrapers += 1
                if len(row_to_check_with_visible_skyscraper_numbers[index]) > 1:
                  num_empty_squares += 1
              if visible_skycrapers == visible_skyscraper_number - 1 and minimum_index_of_biggest_numbers > 2:
                max_values = sorted(row_to_check_with_visible_skyscraper_numbers[1], reverse=True)[:num_empty_squares+1]
                if max_values:
                  for value_to_remove in range(1, max_values[-1]):
                    if value_to_remove in self.grid[i][1]:
                      self.grid[i][1].discard(value_to_remove)
                      if not self.grid[i][1]:
                        return False
              elif visible_skycrapers < visible_skyscraper_number - 1 and visible_skyscraper_number != 2 and visible_skycrapers != len(indexes_biggest_numbers):
                for counter in range(1, visible_skyscraper_number - visible_skycrapers):
                  for num in range(counter, visible_skyscraper_number - visible_skycrapers):
                    value_to_remove = biggest_smallest_number - (visible_skyscraper_number - visible_skycrapers - num)
                    if value_to_remove in self.grid[i][counter]:
                      self.grid[i][counter].discard(value_to_remove)
                      if not self.grid[i][counter]:
                        return False
          # Apply the fifth advanced inference if the 'visible skyscraper number' square is at the last row.  
          if len(row_to_check_with_visible_skyscraper_numbers[board_size_max_index]) == 1:
            visible_skyscraper_number = next(iter(row_to_check_with_visible_skyscraper_numbers[board_size_max_index]))
          else:
            visible_skyscraper_number = 0
          if visible_skyscraper_number > 1 and visible_skyscraper_number < board_size - 1:
            biggest_smallest_number = 0
            visible_skycrapers = 0
            highest_building_value = 0
            indexes_biggest_numbers = []
            num_empty_squares = 0
            row_to_check_with_visible_skyscraper_numbers.reverse()
            row_to_check.reverse()
            for counter in range(0, board_size):
              if {board_size-counter} in row_to_check:
                biggest_smallest_number = board_size-counter
                indexes_biggest_numbers.append(row_to_check.index({board_size-counter})+1)
              else:
                break
            if biggest_smallest_number > 0:
              minimum_index_of_biggest_numbers = min(indexes_biggest_numbers)
              for index in range(minimum_index_of_biggest_numbers, board_size_max_index):
                if next(iter(row_to_check_with_visible_skyscraper_numbers[index])) > highest_building_value:
                  highest_building_value = next(iter(row_to_check_with_visible_skyscraper_numbers[index]))
                  visible_skycrapers += 1
                if len(row_to_check_with_visible_skyscraper_numbers[index]) > 1:
                  num_empty_squares += 1
              if visible_skycrapers == visible_skyscraper_number - 1 and minimum_index_of_biggest_numbers > 2:
                max_values = sorted(row_to_check_with_visible_skyscraper_numbers[1], reverse=True)[:num_empty_squares+1]
                if max_values:
                  for value_to_remove in range(1, max_values[-1]):
                    if value_to_remove in self.grid[i][board_size_max_index-1]:
                      self.grid[i][board_size_max_index-1].discard(value_to_remove)
                      if not self.grid[i][board_size_max_index-1]:
                        return False
              elif visible_skycrapers < visible_skyscraper_number - 1 and visible_skyscraper_number != 2 and visible_skycrapers != len(indexes_biggest_numbers):
                for counter in range(1, visible_skyscraper_number - visible_skycrapers):
                  for num in range(counter, visible_skyscraper_number - visible_skycrapers):
                    value_to_remove = biggest_smallest_number - (visible_skyscraper_number - visible_skycrapers - num)
                    if value_to_remove in self.grid[i][board_size_max_index-counter]:
                      self.grid[i][board_size_max_index-counter].discard(value_to_remove)
                      if not self.grid[i][board_size_max_index-counter]:
                        return False
          column_to_check = [self.grid[j][i] for j in range(1, board_size+1)]
          column_to_check_with_visible_skyscraper_numbers = [set(self.grid[j][i]) for j in range(board_size_with_visible_skyscraper_numbers)]
          # Apply the fifth advanced inference if the 'visible skyscraper number' square is at the first column. 
          if len(column_to_check_with_visible_skyscraper_numbers[0]) == 1:
            visible_skyscraper_number = next(iter(column_to_check_with_visible_skyscraper_numbers[0]))
          else:
            visible_skyscraper_number = 0
          if visible_skyscraper_number > 1 and visible_skyscraper_number < board_size - 1:
            biggest_smallest_number = 0
            visible_skycrapers = 0
            highest_building_value = 0
            indexes_biggest_numbers = []
            num_empty_squares = 0
            for counter in range(0, board_size):
              if {board_size-counter} in column_to_check:
                biggest_smallest_number = board_size-counter
                indexes_biggest_numbers.append(column_to_check.index({board_size-counter})+1)
              else:
                break
            if biggest_smallest_number > 0:
              minimum_index_of_biggest_numbers = min(indexes_biggest_numbers)
              for index in range(minimum_index_of_biggest_numbers, board_size_max_index):
                if next(iter(column_to_check_with_visible_skyscraper_numbers[index])) > highest_building_value:
                  highest_building_value = next(iter(column_to_check_with_visible_skyscraper_numbers[index]))
                  visible_skycrapers += 1
                if len(column_to_check_with_visible_skyscraper_numbers[index]) > 1:
                  num_empty_squares += 1
              if visible_skycrapers == visible_skyscraper_number - 1 and minimum_index_of_biggest_numbers > 2:
                max_values = sorted(column_to_check_with_visible_skyscraper_numbers[1], reverse=True)[:num_empty_squares+1]
                if max_values:
                  for value_to_remove in range(1, max_values[-1]):
                    if value_to_remove in self.grid[1][i]:
                      self.grid[1][i].discard(value_to_remove)
                      if not self.grid[1][i]:
                        return False
              elif visible_skycrapers < visible_skyscraper_number - 1 and visible_skyscraper_number != 2 and visible_skycrapers != len(indexes_biggest_numbers):
                for counter in range(1, visible_skyscraper_number - visible_skycrapers):
                  for num in range(counter, visible_skyscraper_number - visible_skycrapers):
                    value_to_remove = biggest_smallest_number - (visible_skyscraper_number - visible_skycrapers - num)
                    if value_to_remove in self.grid[counter][i]:
                      self.grid[counter][i].discard(value_to_remove)
                      if not self.grid[counter][i]:
                        return False
          # Apply the fifth advanced inference if the 'visible skyscraper number' square is at the last column.            
          if len(column_to_check_with_visible_skyscraper_numbers[board_size_max_index]) == 1:
            visible_skyscraper_number = next(iter(column_to_check_with_visible_skyscraper_numbers[board_size_max_index]))
          else:
            visible_skyscraper_number = 0
          if visible_skyscraper_number > 1 and visible_skyscraper_number < board_size - 1:
            biggest_smallest_number = 0
            visible_skycrapers = 0
            highest_building_value = 0
            indexes_biggest_numbers = []
            num_empty_squares = 0
            column_to_check_with_visible_skyscraper_numbers.reverse()
            column_to_check.reverse()
            for counter in range(0, board_size):
              if {board_size-counter} in column_to_check:
                biggest_smallest_number = board_size-counter
                indexes_biggest_numbers.append(column_to_check.index({board_size-counter})+1)
              else:
                break
            if biggest_smallest_number > 0:
              minimum_index_of_biggest_numbers = min(indexes_biggest_numbers)
              for index in range(minimum_index_of_biggest_numbers, board_size_max_index):
                if next(iter(column_to_check_with_visible_skyscraper_numbers[index])) > highest_building_value:
                  highest_building_value = next(iter(column_to_check_with_visible_skyscraper_numbers[index]))
                  visible_skycrapers += 1
                if len(column_to_check_with_visible_skyscraper_numbers[index]) > 1:
                  num_empty_squares += 1
              if visible_skycrapers == visible_skyscraper_number - 1 and minimum_index_of_biggest_numbers > 2:
                max_values = sorted(column_to_check_with_visible_skyscraper_numbers[1], reverse=True)[:num_empty_squares+1]
                if max_values:
                  for value_to_remove in range(1, max_values[-1]):
                    if value_to_remove in self.grid[board_size_max_index-1][i]:
                      self.grid[board_size_max_index-1][i].discard(value_to_remove)
                      if not self.grid[board_size_max_index-1][i]:
                        return False
      
              elif visible_skycrapers < visible_skyscraper_number - 1 and visible_skyscraper_number != 2 and visible_skycrapers != len(indexes_biggest_numbers):
                for counter in range(1, visible_skyscraper_number - visible_skycrapers):
                  for num in range(counter, visible_skyscraper_number - visible_skycrapers):
                    value_to_remove = biggest_smallest_number - (visible_skyscraper_number - visible_skycrapers - num)
                    if value_to_remove in self.grid[board_size_max_index-counter][i]:
                      self.grid[board_size_max_index-counter][i].discard(value_to_remove)
                      if not self.grid[board_size_max_index-counter][i]:
                        return False
    
        row_to_check = self.grid[i][1:-1]
        row_to_check_with_visible_skyscraper_numbers = self.grid[i]
        row_complete = True
        for el in row_to_check:
          if len(el) > 1:
            row_complete = False
            break
        if not row_complete:
          if len(row_to_check_with_visible_skyscraper_numbers[0]) == 1:
            visible_skyscraper_number = next(iter(row_to_check_with_visible_skyscraper_numbers[0]))
          else:
            visible_skyscraper_number = 0
          ascending_order_conditions = True
          if visible_skyscraper_number > 1 and visible_skyscraper_number < board_size:
            for index in range(1, visible_skyscraper_number):
              if index != 1 and min(row_to_check_with_visible_skyscraper_numbers[index]) <= max(row_to_check_with_visible_skyscraper_numbers[index-1]):
                ascending_order_conditions = False
                break
            if ascending_order_conditions:
              # Apply the eighth advanced inference if the 'visible skyscraper number' square is at the first row. 
              start_value_to_remove = max(row_to_check_with_visible_skyscraper_numbers[visible_skyscraper_number-1]) + 1
              for value_to_remove in range(start_value_to_remove, board_size):
                if value_to_remove in self.grid[i][visible_skyscraper_number]:
                  self.grid[i][visible_skyscraper_number].discard(value_to_remove)
                  if not self.grid[i][visible_skyscraper_number]:
                    return False
              if {board_size} in row_to_check:
                # Apply the sixth advanced inference if the 'visible skyscraper number' square is at the first row. 
                highest_building_index =  row_to_check_with_visible_skyscraper_numbers.index({board_size})
                start_value_to_remove = max(row_to_check_with_visible_skyscraper_numbers[visible_skyscraper_number-1]) + 1
                for index in range(visible_skyscraper_number, highest_building_index):
                  for value_to_remove in range(start_value_to_remove, board_size):
                    if value_to_remove in self.grid[i][index]:
                      self.grid[i][index].discard(value_to_remove)
                      if not self.grid[i][index]:
                        return False
                # Apply the seventh advanced inference if the 'visible skyscraper number' square is at the first row. 
                if visible_skyscraper_number > 2:
                  start_value_to_remove = max(row_to_check_with_visible_skyscraper_numbers[visible_skyscraper_number-2]) + 1
                  for value_to_remove in range(start_value_to_remove, highest_building_index-1):
                    if value_to_remove in self.grid[i][visible_skyscraper_number-1]:
                      self.grid[i][visible_skyscraper_number-1].discard(value_to_remove)
                      if not self.grid[i][visible_skyscraper_number-1]:
                        return False
              
                  
          if len(row_to_check_with_visible_skyscraper_numbers[board_size_max_index]) == 1:
            visible_skyscraper_number = next(iter(row_to_check_with_visible_skyscraper_numbers[board_size_max_index]))
          else:
            visible_skyscraper_number = 0
          ascending_order_conditions = True
          if visible_skyscraper_number > 1 and visible_skyscraper_number < board_size:
            for index in range(board_size_max_index - visible_skyscraper_number + 1, board_size_max_index):
              if index != board_size_max_index - 1 and min(row_to_check_with_visible_skyscraper_numbers[index]) <= max(row_to_check_with_visible_skyscraper_numbers[index+1]):
                ascending_order_conditions = False
                break
            if ascending_order_conditions:
              # Apply the eighth advanced inference if the 'visible skyscraper number' square is at the last row. 
              start_value_to_remove = max(row_to_check_with_visible_skyscraper_numbers[board_size_max_index-visible_skyscraper_number+1]) + 1
              for value_to_remove in range(start_value_to_remove, board_size):
                if value_to_remove in self.grid[i][board_size_max_index-visible_skyscraper_number]:
                  self.grid[i][board_size_max_index-visible_skyscraper_number].discard(value_to_remove)
                  if not self.grid[i][board_size_max_index-visible_skyscraper_number]:
                    return False
              if {board_size} in row_to_check:
                # Apply the sixth advanced inference if the 'visible skyscraper number' square is at the last row. 
                highest_building_index =  row_to_check_with_visible_skyscraper_numbers.index({board_size})
                start_value_to_remove = max(row_to_check_with_visible_skyscraper_numbers[board_size_max_index-visible_skyscraper_number+1]) + 1
                for index in range(highest_building_index+1, board_size_max_index-visible_skyscraper_number+1):
                  for value_to_remove in range(start_value_to_remove, board_size):
                    if value_to_remove in self.grid[i][index]:
                      self.grid[i][index].discard(value_to_remove)
                      if not self.grid[i][index]:
                        return False
                # Apply the seventh advanced inference if the 'visible skyscraper number' square is at the last row. 
                if visible_skyscraper_number > 2:
                  start_value_to_remove = max(row_to_check_with_visible_skyscraper_numbers[board_size_max_index-visible_skyscraper_number+2]) + 1
                  for value_to_remove in range(start_value_to_remove, board_size - highest_building_index):
                    if value_to_remove in self.grid[i][board_size_max_index-visible_skyscraper_number+1]:
                      self.grid[i][board_size_max_index-visible_skyscraper_number+1].discard(value_to_remove)
                      if not self.grid[i][board_size_max_index-visible_skyscraper_number+1]:
                        return False
        column_to_check = [self.grid[j][i] for j in range(1, board_size+1)]
        column_to_check_with_visible_skyscraper_numbers = [self.grid[j][i] for j in range(board_size_with_visible_skyscraper_numbers)]
        column_complete = True
        for el in column_to_check:
          if len(el) > 1:
            column_complete = False
            break
        if not column_complete:
          if len(column_to_check_with_visible_skyscraper_numbers[0]) == 1:
            visible_skyscraper_number = next(iter(column_to_check_with_visible_skyscraper_numbers[0]))
          else:
            visible_skyscraper_number = 0
          ascending_order_conditions = True
          if visible_skyscraper_number > 1 and visible_skyscraper_number < board_size:
            for index in range(1, visible_skyscraper_number):
              if index != 1 and min(column_to_check_with_visible_skyscraper_numbers[index]) <= max(column_to_check_with_visible_skyscraper_numbers[index-1]):
                ascending_order_conditions = False
                break
            if ascending_order_conditions:
              # Apply the eighth advanced inference if the 'visible skyscraper number' square is at the first column. 
              start_value_to_remove = max(column_to_check_with_visible_skyscraper_numbers[visible_skyscraper_number-1]) + 1
              for value_to_remove in range(start_value_to_remove, board_size):
                if value_to_remove in self.grid[visible_skyscraper_number][i]:
                  self.grid[visible_skyscraper_number][i].discard(value_to_remove)
                  if not self.grid[visible_skyscraper_number][i]:
                    return False
              if {board_size} in column_to_check:
                # Apply the sixth advanced inference if the 'visible skyscraper number' square is at the first column. 
                highest_building_index =  column_to_check_with_visible_skyscraper_numbers.index({board_size})
                start_value_to_remove = max(column_to_check_with_visible_skyscraper_numbers[visible_skyscraper_number-1]) + 1
                for index in range(visible_skyscraper_number, highest_building_index):
                  for value_to_remove in range(start_value_to_remove, board_size):
                    if value_to_remove in  self.grid[index][i]:
                      self.grid[index][i].discard(value_to_remove)
                      if not self.grid[index][i]:
                        return False
                # Apply the seventh advanced inference if the 'visible skyscraper number' square is at the first column. 
                if visible_skyscraper_number > 2:
                  start_value_to_remove = max(column_to_check_with_visible_skyscraper_numbers[visible_skyscraper_number-2]) + 1
                  for value_to_remove in range(start_value_to_remove, highest_building_index-1):
                    if value_to_remove in self.grid[visible_skyscraper_number-1][i]:
                      self.grid[visible_skyscraper_number-1][i].discard(value_to_remove)
                      if not self.grid[visible_skyscraper_number-1][i]:
                        return False
          if len(column_to_check_with_visible_skyscraper_numbers[board_size_max_index]) == 1:
            visible_skyscraper_number = next(iter(column_to_check_with_visible_skyscraper_numbers[board_size_max_index]))
          else:
            visible_skyscraper_number = 0
          ascending_order_conditions = True
          if visible_skyscraper_number > 1 and visible_skyscraper_number < board_size:
            for index in range(board_size_max_index - visible_skyscraper_number + 1, board_size_max_index):
              if index != board_size_max_index - 1 and min(column_to_check_with_visible_skyscraper_numbers[index]) <= max(column_to_check_with_visible_skyscraper_numbers[index+1]):
                ascending_order_conditions = False
                break
            if ascending_order_conditions:
              # Apply the eighth advanced inference if the 'visible skyscraper number' square is at the last column. 
              start_value_to_remove = max(column_to_check_with_visible_skyscraper_numbers[board_size_max_index - visible_skyscraper_number+1]) + 1
              for value_to_remove in range(start_value_to_remove, board_size):
                if value_to_remove in self.grid[board_size_max_index - visible_skyscraper_number][i]:
                  self.grid[board_size_max_index - visible_skyscraper_number][i].discard(value_to_remove)
                  if not self.grid[board_size_max_index - visible_skyscraper_number][i]:
                    return False
              if {board_size} in column_to_check:
                # Apply the sixth advanced inference if the 'visible skyscraper number' square is at the last column. 
                highest_building_index =  column_to_check_with_visible_skyscraper_numbers.index({board_size})
                start_value_to_remove = max(column_to_check_with_visible_skyscraper_numbers[board_size_max_index-visible_skyscraper_number+1]) + 1
                for index in range(highest_building_index+1, board_size_max_index-visible_skyscraper_number+1):
                  for value_to_remove in range(start_value_to_remove, board_size):
                    if value_to_remove in self.grid[index][i]:
                      self.grid[index][i].discard(value_to_remove)
                      if not self.grid[index][i]:
                        return False
                # Apply the seventh advanced inference if the 'visible skyscraper number' square is at the last column. 
                if visible_skyscraper_number > 2:
                  start_value_to_remove = max(column_to_check_with_visible_skyscraper_numbers[board_size_max_index-visible_skyscraper_number+2]) + 1
                  for value_to_remove in range(start_value_to_remove, board_size - highest_building_index):
                    if value_to_remove in self.grid[board_size_max_index-visible_skyscraper_number+1][i]:
                      self.grid[board_size_max_index-visible_skyscraper_number+1][i].discard(value_to_remove)
                      if not self.grid[board_size_max_index-visible_skyscraper_number+1][i]:
                        return False
        
        row_to_check = self.grid[i][1:-1]
        row_to_check_with_visible_skyscraper_numbers = [set(val) for val in self.grid[i]]
        # Apply the ninth advanced inference if the 'visible skyscraper number' square is at the first row. 
        if len(row_to_check_with_visible_skyscraper_numbers[0]) == 1:
          visible_skyscraper_number = next(iter(row_to_check_with_visible_skyscraper_numbers[0]))
        else:
          visible_skyscraper_number = 0
        non_assigned_squares_index = []
        if visible_skyscraper_number > 1 and visible_skyscraper_number < board_size-1:
          if {board_size} in row_to_check:
            for index in range(1, row_to_check_with_visible_skyscraper_numbers.index({board_size})):
              if len(row_to_check_with_visible_skyscraper_numbers[index]) > 1:
                non_assigned_squares_index.append(index)
                if len(non_assigned_squares_index) > 1:
                  break
            if len(non_assigned_squares_index) == 1:
              for value in row_to_check_with_visible_skyscraper_numbers[non_assigned_squares_index[0]]:
                test_row = [set(val) for val in self.grid[i]]
                test_row[non_assigned_squares_index[0]] = {value}
                visible_skycrapers = 0
                highest_building_value = 0
                for square in test_row[1:-1]:
                  if next(iter(square)) > highest_building_value:
                    highest_building_value = next(iter(square))
                    visible_skycrapers += 1
                if visible_skycrapers != visible_skyscraper_number:
                  if value in self.grid[i][non_assigned_squares_index[0]]:
                    self.grid[i][non_assigned_squares_index[0]].discard(value)
                    if not self.grid[i][non_assigned_squares_index[0]]:
                      return False   
        # Apply the ninth advanced inference if the 'visible skyscraper number' square is at the last row.                              
        if len(row_to_check_with_visible_skyscraper_numbers[board_size_max_index]) == 1:
          visible_skyscraper_number = next(iter(row_to_check_with_visible_skyscraper_numbers[board_size_max_index]))
        else:
          visible_skyscraper_number = 0
        non_assigned_squares_index = []
        if visible_skyscraper_number > 1 and visible_skyscraper_number < board_size-1:
          if {board_size} in row_to_check:
            for index in range(row_to_check_with_visible_skyscraper_numbers.index({board_size})+1, board_size_max_index):
              if len(row_to_check_with_visible_skyscraper_numbers[index]) > 1:
                non_assigned_squares_index.append(index)
                if len(non_assigned_squares_index) > 1:
                  break
            if len(non_assigned_squares_index) == 1:
              for value in row_to_check_with_visible_skyscraper_numbers[non_assigned_squares_index[0]]:
                test_row = [set(val) for val in self.grid[i]]
                test_row[non_assigned_squares_index[0]] = {value}
                test_row.reverse()
                visible_skycrapers = 0
                highest_building_value = 0
                for square in test_row[1:-1]:
                  if next(iter(square)) > highest_building_value:
                    highest_building_value = next(iter(square))
                    visible_skycrapers += 1
                if visible_skycrapers != visible_skyscraper_number:
                  if value in self.grid[i][non_assigned_squares_index[0]]:
                    self.grid[i][non_assigned_squares_index[0]].discard(value)
                    if not self.grid[i][non_assigned_squares_index[0]]:
                      return False
        column_to_check = [self.grid[j][i] for j in range(1, board_size+1)]
        column_to_check_with_visible_skyscraper_numbers = [set(self.grid[j][i]) for j in range(board_size_with_visible_skyscraper_numbers)]
        # Apply the ninth advanced inference if the 'visible skyscraper number' square is at the first column. 
        if len(column_to_check_with_visible_skyscraper_numbers[0]) == 1:
          visible_skyscraper_number = next(iter( column_to_check_with_visible_skyscraper_numbers[0]))
        else:
          visible_skyscraper_number = 0
        non_assigned_squares_index = []
        if visible_skyscraper_number > 1 and visible_skyscraper_number < board_size-1:
          if {board_size} in column_to_check:
            for index in range(1, column_to_check_with_visible_skyscraper_numbers.index({board_size})):
              if len(column_to_check_with_visible_skyscraper_numbers[index]) > 1:
                non_assigned_squares_index.append(index)
                if len(non_assigned_squares_index) > 1:
                  break
            if len(non_assigned_squares_index) == 1:
              for value in column_to_check_with_visible_skyscraper_numbers[non_assigned_squares_index[0]]:
                test_column = [set(self.grid[j][i]) for j in range(board_size_with_visible_skyscraper_numbers)]
                test_column[non_assigned_squares_index[0]] = {value}
                visible_skycrapers = 0
                highest_building_value = 0
                for square in test_column[1:-1]:
                  if next(iter(square)) > highest_building_value:
                    highest_building_value = next(iter(square))
                    visible_skycrapers += 1
                if visible_skycrapers != visible_skyscraper_number:
                  if value in self.grid[non_assigned_squares_index[0]][i]:
                    self.grid[non_assigned_squares_index[0]][i].discard(value)
                    if not self.grid[non_assigned_squares_index[0]][i]:
                      return False
        # Apply the ninth advanced inference if the 'visible skyscraper number' square is at the last column.                              
        if len(column_to_check_with_visible_skyscraper_numbers[board_size_max_index]) == 1:
          visible_skyscraper_number = next(iter(column_to_check_with_visible_skyscraper_numbers[board_size_max_index]))
        else:
          visible_skyscraper_number = 0
        non_assigned_squares_index = []
        if visible_skyscraper_number > 1 and visible_skyscraper_number < board_size-1:
          if {board_size} in column_to_check:
            for index in range(column_to_check_with_visible_skyscraper_numbers.index({board_size})+1, board_size_max_index):
              if len(column_to_check_with_visible_skyscraper_numbers[index]) > 1:
                non_assigned_squares_index.append(index)
                if len(non_assigned_squares_index) > 1:
                  break
            if len(non_assigned_squares_index) == 1:
              for value in column_to_check_with_visible_skyscraper_numbers[non_assigned_squares_index[0]]:
                test_column = [set(self.grid[j][i]) for j in range(board_size_with_visible_skyscraper_numbers)]
                test_column[non_assigned_squares_index[0]] = {value}
                test_column.reverse()
                visible_skycrapers = 0
                highest_building_value = 0
                for square in test_column[1:-1]:
                  if next(iter(square)) > highest_building_value:
                    highest_building_value = next(iter(square))
                    visible_skycrapers += 1
                if visible_skycrapers != visible_skyscraper_number:
                  if value in self.grid[non_assigned_squares_index[0]][i]:
                    self.grid[non_assigned_squares_index[0]][i].discard(value)
                    if not self.grid[non_assigned_squares_index[0]][i]:
                      return False

    return True

  def is_consistent(self, r, c):
    # Overrides the abstract is_consistent method from the Puzzle class to check the consistency of the Skyscraper puzzle
    # state based on the specific constraints of Skyscraper puzzle.

    # Parameters:
    # r (int): The row index of the cell currently being evaluated for consistency.
    # c (int): The column index of the cell currently being evaluated for consistency.

    # Returns:
    # bool: True if the puzzle is consistent, False otherwise.
    board_size = self.board_size
    board_size_with_visible_skyscraper_numbers = self.board_size + 2
    board_size_max_index = self.board_size + 1
    #Check the 'visisble skyscraper number' constraint is satisfied if the 'visisble skyscraper number' is at the start of the row.
    row_to_check = [set(s) for s in self.grid[r][1:-1]]
    row_to_check_with_visible_skyscraper_numbers = [set(s) for s in self.grid[r]]
    counter_square_filled = 0
    for square in row_to_check:
      if len(square) == 1:
        counter_square_filled += 1
    if len(row_to_check_with_visible_skyscraper_numbers[0]) == 1 and counter_square_filled == board_size:
      left_visible_skyscraper_number =  next(iter(row_to_check_with_visible_skyscraper_numbers[0]))
      counter_skycraper = 1
      max_skycraper = next(iter(row_to_check[0]))
      for value in row_to_check:
        if next(iter(value)) > max_skycraper:
          max_skycraper = next(iter(value))
          counter_skycraper += 1
      if counter_skycraper != left_visible_skyscraper_number:
        return False
    #Check the 'visisble skyscraper number' constraint is satisfied if the 'visisble skyscraper number' is at the end of the row.
    row_to_check.reverse()
    row_to_check_with_visible_skyscraper_numbers.reverse()
    if len(row_to_check_with_visible_skyscraper_numbers[0]) == 1 and counter_square_filled == board_size:
      right_visible_skyscraper_number = next(iter(row_to_check_with_visible_skyscraper_numbers[0]))
      counter_skycraper = 1
      max_skycraper = next(iter(row_to_check[0]))
      for value in row_to_check:
        if next(iter(value)) > max_skycraper:
          max_skycraper = next(iter(value))
          counter_skycraper += 1
      if counter_skycraper != right_visible_skyscraper_number:
        return False

    #Check the 'visisble skyscraper number' constraint is satisfied if the 'visisble skyscraper number' is at the start of the column.
    column_to_check = [set(s) for s in [self.grid[j][c] for j in range(1, board_size_max_index)]]
    column_to_check_with_visible_skyscraper_numbers = [set(s) for s in [self.grid[j][c] for j in range(board_size_with_visible_skyscraper_numbers)]]
    counter_square_filled = 0
    for square in column_to_check:
      if len(square) == 1:
        counter_square_filled += 1
    if len(column_to_check_with_visible_skyscraper_numbers[0]) == 1 and counter_square_filled == board_size:
      top_visible_skyscraper_number =  next(iter(column_to_check_with_visible_skyscraper_numbers[0]))
      counter_skycraper = 1
      max_skycraper = next(iter(column_to_check[0]))
      for value in column_to_check:
        if next(iter(value)) > max_skycraper:
          max_skycraper = next(iter(value))
          counter_skycraper += 1
      if counter_skycraper != top_visible_skyscraper_number:
        return False
    #Check the 'visisble skyscraper number' constraint is satisfied if the 'visisble skyscraper number' is at the end of the column.
    column_to_check.reverse()
    column_to_check_with_visible_skyscraper_numbers.reverse()
    if len(column_to_check_with_visible_skyscraper_numbers[0]) == 1 and counter_square_filled == board_size:
      bottom_visible_skyscraper_number = next(iter(column_to_check_with_visible_skyscraper_numbers[0]))
      counter_skycraper = 1
      max_skycraper = next(iter(column_to_check[0]))
      for value in column_to_check:
        if next(iter(value)) > max_skycraper:
          max_skycraper = next(iter(value))
          counter_skycraper += 1
      if counter_skycraper != bottom_visible_skyscraper_number:
        return False
    return True

  def apply_variant_inferences(self):
    # Abstract method that contains the inferences specific to the variant of the Skyscraper puzzle to incorparate them in the constraint propagation process.

    # Return True by default.
    return True
  
  def propagate_from_single_value(self, main_queue, current_value_queue, row, col):
    # This method is called everytime the uniqueness value inference in rows or columns reduce a domain into a single value.
    # It ensures the prioritisation of the uniqueness value in rows and columns inferences, by executing them repeatedly, until no additional 
    # reductions in domain sizes occur within the rows or columns.
    #Parameters:
    # main_queue: queue from the constraint propagation process
    # current_value_queue: set that stores the value of the queue from the constraint propagation process
    # row: The row of the square with a single value
    # col: The colum of the square with a single value
    board_size_max_index = self.board_size + 1
    local_queue = deque([(row, col)])
    while local_queue:
      r, c = local_queue.popleft()
      value_to_remove = next(iter(self.grid[i][i]))

      for i in range(1, board_size_max_index):
        if i != c and value_to_remove in self.grid[i][i]:
          self.grid[i][i].discard(value_to_remove)
          if not self.grid[i][i]:
            return False
          if len(self.grid[i][i]) == 1:
            if (r, i) not in current_value_queue:
              main_queue.append((r, i))
              current_value_queue.add((r, i))
            local_queue.append((r, i))
        if i != r and value_to_remove in self.grid[i][i]:
          self.grid[i][i].discard(value_to_remove)
          if not self.grid[i][i]:
            return False
          if len(self.grid[i][i]) == 1:
            if (i, c) not in current_value_queue:
              main_queue.append((i, c))
              current_value_queue.add((i, c))
            local_queue.append((i, c))

    return True


  def write(self):
    # Overrides the write method from the Puzzle class to adapt to the configuration of the Skyscraper puzzle grid.
    for i in range(self.board_size + 2):
      for j in range(self.board_size + 2):
        if len(self.grid[i][j]) != 1:
          print(" ", end="")
        else:
          print(next(iter(self.grid[i][j])), end="")
      print()

  
  def is_solution(self):
    # Overrides the is_solution method from the Puzzle class to adapt to the configuration of the Skyscraper puzzle grid.
    for i in range(1, self.board_size + 1):
      for j in range(1, self.board_size + 1):
        if len(self.grid[i][j]) != 1:
          return False
    return True

  def fill_board(self, fill_with):
    # Overrides the fill_board method from the Puzzle class to adapt to the configuration of the Skyscraper puzzle grid.
    if len(fill_with) != self.board_size + 2:
      raise ValueError("The input grid does not have the correct number of rows for the specified size of the Skyscraper puzzle.")
    for row in range(len(fill_with)):
      if len(fill_with[row]) != self.board_size + 2:
        raise ValueError("The input grid does not have the correct number of columns for the specified size of the Skyscraper puzzle.")
      for col in range(len(fill_with)):
        if fill_with[row][col].isdigit():      
          value = int(fill_with[row][col])
          if value > self.board_size:
            raise ValueError(f"Invalid digit {fill_with[row][col]}, expect to be lower or equal to {self.board_size}.")
          self.set_square(row, col, value)
        elif fill_with[row][col] != ' ':
          raise ValueError(f"Invalid character {fill_with[row][col]}, expected a digit or space.")
  
  def successors(self):
    # Overrides the successors method from the Puzzle class to adjust the selection vraiable process specifically for the Skyscraper puzzle.
    # The variable is chosen by applying the Minimum Remaining Value heuristic. It then checks if the values of the
    # selected variable could lead to a potential successor. Each viable successor is added to the successors list.
    min_options = float('inf')
    min_cell = None
    # Apply the Minimum Remaining Value heuristic
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
      test_if_successor = Skyscraper(self.board_size)
      for k in range(self.board_size+2):
        for l in range(self.board_size+2):
          test_if_successor.grid[k][l] = self.grid[k][l].copy()
      if test_if_successor.set_square(i, j, option):
        successors.append(test_if_successor)
    return successors

  def heuristic_value(self):
    # Overrides the successors method from the Puzzle class to adjust the selection value process specifically for the Skyscraper puzzle.
    # It employs the minimum unassigned variables heuristic strategy, by counting the number of square with domain'length superior to one.
    count = 0
    for i in range(1, self.board_size + 1):
      for j in range(1, self.board_size + 1):
        if len(self.grid[i][j]) != 1:
          count += 1
    return count