""" ===-- Puzzle class -----------*- Python3 -*-===//

This source file is part of the 'AI for Sudoku-Like puzzle' project developed by Jules Roussel.

===----------------------------------------------------------------------===

This is the Puzzle class.

===----------------------------------------------------------------------===
"""

#from ExperimentalClasses.backtracking_search_with_LCV_heuristic import BacktrackingSearch
#from ExperimentalClasses.depth_first_search import DepthFirstSearch
from FinalSolver.backtracking_search import BacktrackingSearch
# from ExperimentalClasses.breadth_first_search import BreadthFirstSearch
# from ExperimentalClasses.backtracking_search_with_LCV_heuristic import BacktrackingSearch
import time

# Puzzle constructor:

# Parameters:
# board size (int): represents the size of the grid.

# Attributes:
# grid: A list of list of set, which represents the rows, the columns and the square's domains, respectively, of the Puzzle s' grid.
# solution (Puzzle): represents the solution of the Puzzle, if one exists.
class Puzzle:
  def __init__(self, board_size_in):
    self.board_size = board_size_in
    self.grid = [[set(range(1, board_size_in + 1)) for _ in range(board_size_in)] for _ in range(board_size_in)]
    self.solution = None


  def get_square(self, row, col):

    # This method returns the value of the cell located at the specified row and column indices. 
    # If the cell's domain contains excatly one value, it returns that value.
    # Otherwise, it returns -1, indicating that the cell's value is still unassigned.
    # 
    # Parameters:
    # - row (int): The row index of square.
    # - col (int): The column index of the square.

    # Returns: The value of the square if it is assigned, otherwise -1.
    if len(self.grid[row][col]) == 1:
        return next(iter(self.grid[row][col]))
    else:
       return -1

  def set_square(self, row, col, value): 
  # This method assigns a specific value to the square located at the given row and column indices.
  # After setting the value, it clears the current domain of that square and starts the constraint 
  # propagation process to ensure all related constraints are maintained. If the constraint 
  # propagation fails due to an inconstancy, it returns False.

  # Parameters:
  # row (int): The row index of the square to be set.
  # col (int): The column index of the square to be set.
  # value (int): The value to assign to the square.

  # Returns: True if the constraint propagation after setting the square is successful, False otherwise.
    self.grid[row][col].clear()  
    self.grid[row][col].add(value)
    if not self.constraint_propagation(row, col):
      return False
    return True
  
  def solve_puzzle(self, input_board):
  # Attempts to solve a puzzle given an input grid.

  # This method takes the initial board configuration as input, in the form of a list of strings (corresponding to the rows and columns respectively), 
  # processes it to populate the puzzle grid, and then attempts to find a solution. It prints the user input, fills the board,
  # checks for a direct solution, and if necessary, initiates a backtracking search process.

  # Parameters:
  # input_board : The initial puzzle grid configuration, where each string
  #   in the list represents a row of the puzzle.

  # Returns: True if the puzzle is solved successfully, False if no solution is found and therefore not solvable.

    #Display the user input grid
    for row in input_board:
      print(row)
    start_time = time.time()
    #Fill the board with the data from the input grid
    self.fill_board(input_board)
    #If a solution is found, print it, print the time it took and return True
    if self.is_solution():
      end_time = time.time()
      print(f'Time taken: {end_time - start_time} seconds')
      self.write()
      self.solution = self.grid
      return True
    else:
      #If the board is still not filled, the backtracking process starts
      search = BacktrackingSearch(self)
      solution = search.solve()
      end_time = time.time()
      #If the backtracking search finds a solution, then the solution is printed with the time taken
      #and the number explored during the search, and return True
      if solution:
        # print(f"Number of nodes explore: {search.get_nodes_expanded()} nodes")
        print(f'Time taken: {end_time - start_time} seconds')
        solution.write()
        self.solution = solution.grid
        return True
      else:
        #Otherwise, print "no solution found" and return False, meaning that the puzzle is unsolvable
        print("No solution found")
        return False

  def constraint_propagation(self, row, col):
    # Abstract method for constraint propagation logic that must be overidden in subclasses.

    # This abstract method contains the logic to propagate constraints throughout the puzzle grid
    # after a new value has been set at the specified row and column. The implementation
    # will depend on the specific rules and constraints of the puzzle variant being solved.

    # Parameters:
    # row (int): The row index of the square where a value has been set.
    # col (int): The column index of the square where a value has been set.

    # Raises: NotImplementedError: If this method is called without an overriding implementation in a subclass.
    raise NotImplementedError("The 'constraint_propagation' method must be implemented by the puzzle-specific subclass due the unique constraints of the puzzle type.")
  
  def is_consistent(self, r, c):
    # Abstract method to check the consistency of the puzzle state after updates during constraint propagation, which must be overidden in subclasses.

    # This method should evaluate whether the puzzle remains solvable after constraints have been propagated 
    # from a given square. It must be implemented in subclasses to accommodate the specific constraints of the puzzle variant.
    # This abstract method checks the consistency between affected vraibles by the constraint propagation

    # Parameters:
    # r (int): The row index of the cell currently being evaluated for consistency.
    # c (int): The column index of the cell currently being evaluated for consistency.

    # Raises: NotImplementedError: If this method is called without an overriding implementation in a subclass.
    raise NotImplementedError("The 'is_consistent' method must be implemented by the puzzle-specific subclass due the unique constraints of the puzzle type.")


  def fill_board(self, fill_with):
    # Fills the board with initial values provided by the user, checking for validity of the input format.

    # This method populates the grid of the puzzle with initial values, ensuring that each input conforms to expected formats and constraints. It raises an error if the input does not match the grid size or contains invalid characters or values.

    # Parameters:
    # fill_with: A list of strings where each string represents a row of numbers separated by spaces (if the square does not have a value assigned).

    # Raises:
    # ValueError: If the input grid dimensions do not match the specified puzzle size or contain invalid characters or values outside the allowable domain.
    if len(fill_with) != self.board_size:
      raise ValueError("The input grid does not have the correct number of rows for the specified size of the Skyscraper puzzle.")
    for row in range(len(fill_with)):
      if len(row) != self.board_size:
        raise ValueError("The input grid does not have the correct number of columns for the specified size of the Skyscraper puzzle.")
      for col in range(len(fill_with)):
        if fill_with[row][col].isdigit():
          value = int(fill_with[row][col])
          if value > self.board_size:
            raise ValueError(f"Invalid digit {fill_with[row][col]}, expect to be lower or equal to {self.board_size}.")
          self.set_square(row, col, value)
        elif fill_with[row][col] != ' ':
          raise ValueError(f"Invalid character {fill_with[row][col]}, expected a digit or space.")

  def write(self):
    # Utility method that prints the current grid of the puzzle. It iterates through each row and column,
    # displaying the values contained in the grid's cells.
    for i in range(self.board_size):
      for j in range(self.board_size ):
        if len(self.grid[i][j]) != 1:
          print(" ", end="")
        else:
          print(next(iter(self.grid[i][j])), end="")
      print()
  
  
  def is_solution(self):
    # Determine if the current state of the puzzle is a solution.
    #
    # This method iterates over the board and checks each square to see if it has a single value assigned.
    # A solution is confirmed if the domain of every square contains exactly one element.
    #
    # Returns: True if all squares have a domain size of 1, indicating a complete solution. Otherwise, False.
    for i in range(0, self.board_size):
      for j in range(0, self.board_size):
        if len(self.grid[i][j]) != 1:
          return False
    return True

  
  def successors(self):
    # Generates all potential successors of the current Skyscraper puzzle state by attempting to place numbers 
    # in squares that do not yet have a fixed value.
    
    # A successor is defined as a puzzle state derived from the current state by making a legal move 
    # according to the constraints of the specific puzzle type. This method is essential for the backtracking search.

    # Returns: A list of puzzle instances, each representing a possible successor state. Each state
    #     is a new configuration of the grid where a single additional value has been set based on successful 
    #     constraint propagation of that value.
    
    # Raises:
    #     NotImplementedError: This method must be implemented by subclasses to adapt to the 
    #     specific rules different puzzle types, as the process of finding successors can vary significantly between different puzzles.

    raise NotImplementedError(
            "The 'successors' method must be implemented by the puzzle-specific subclass due to "
            "the different ways successors are selected based on the specific rules of the puzzle type."
        )

  def heuristic_value(self):
    # The abstract method is used to sort the potential values of a variable in the puzzle based on a heuristic.

    # This method is crucial for optimizing the backtracking search process by arranging 
    # potential values in the most effective order, according to the puzzle's specific constraints.

    # Raises: NotImplementedError: If this method is called without an overriding implementation in a subclass.
    raise NotImplementedError(
            "The 'heuristic value' method must be implemented by the puzzle-specific subclass, as "
            "the best heuristic to use varies according to the type of puzzle."
        )