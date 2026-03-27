from FinalSolver.sum_basket_skyscraper import SumBasketSkyscraper
from FinalSolver.GT_hint_skyscraper import GTHintSkyscraper
from FinalSolver.odd_even_skyscraper import OddEvenSkyscraper
from FinalSolver.skyscraper import Skyscraper

def main():
  #Example of how to use the solver:

  """ Initialise your Skyscraper grid in the form of a list of strings, where each string represent a row of the puzzle grid:

  my_board = [
      "0 5  5  0",
      "         ",
      "        5",
      "5        ",
      "         ",
      "        5",
      "5        ",
      "         ",
      "0  4  5 0"
  ]

  Initialise additional item for the vraiant if needed:

  baskets = { 1: {"sum": 13, "squares": [(2, 2), (2, 3), (3, 2), (3, 3)]},
            2: {"sum": 19, "squares": [(2, 5), (2, 6), (3, 5), (3, 6)]},
            3: {"sum": 20, "squares": [(3, 4), (4, 3), (4, 4), (4, 5), (5, 4)]},
            4: {"sum": 22, "squares": [(5, 2), (5, 3), (6, 2), (6, 3)]},
            5: {"sum": 14, "squares": [(5, 5), (5, 6), (6, 5), (6, 6)]}}

  
  Create a Skyscraper object corresponding to the correct variant by passing the grid size and any additional items as parameters:

  board = SumBasketSkyscraper(7, baskets_in=baskets)

  Solve the puzzle by calling the solve_puzzle method on your Skyscraper object with your grid:

  board.solve_puzzle(my_board)

  Run your solution by running 'python3 skyscraper_solver.py' in your terminal. Make sure you are in the correct directory where skyscraper_solver.py is located.
"""



main()