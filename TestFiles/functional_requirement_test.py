from FinalSolver.skyscraper import Skyscraper
from FinalSolver.sum_basket_skyscraper import SumBasketSkyscraper
from FinalSolver.GT_hint_skyscraper import GTHintSkyscraper
from FinalSolver.odd_even_skyscraper import OddEvenSkyscraper


def main():
  #Tests for the puzzle input requirement:

  correct_input_grid = [
        "022  10",
        "   1   ",
        "3      ",
        "       ",
        "1     2",
        "       ",
        "0   4 0"
    ]

  
  board = Skyscraper(5)
  board.solve_puzzle(correct_input_grid)

  # non_digits_input_grid = [
  #       "0tt  o0",
  #       "   o   ",
  #       "t      ",
  #       "       ",
  #       "o     t",
  #       "       ",
  #       "0   f 0"
  #   ]

  
  # board = Skyscraper(5)
  # board.solve_puzzle(non_digits_input_grid)

  # incorrect_dimension_input_grid = [
  #       "022  10",
  #       "   1   ",
  #       "3      ",
  #       "       ",
  #       "1     2",
  #       "       ",
  #       "      2",
  #       "0   4 0"
  #   ]
  
  # board = Skyscraper(5)
  # board.solve_puzzle(incorrect_dimension_input_grid)


  #Tests for the constraints handling requirement:

  sum_baskets_board = [
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

  baskets = { 1: {"sum": 13, "squares": [(2, 2), (2, 3), (3, 2), (3, 3)]},
            2: {"sum": 19, "squares": [(2, 5), (2, 6), (3, 5), (3, 6)]},
            3: {"sum": 20, "squares": [(3, 4), (4, 3), (4, 4), (4, 5), (5, 4)]},
            4: {"sum": 22, "squares": [(5, 2), (5, 3), (6, 2), (6, 3)]},
            5: {"sum": 14, "squares": [(5, 5), (5, 6), (6, 5), (6, 6)]}}
  
  board = SumBasketSkyscraper(7, baskets_in=baskets)
  board.solve_puzzle(sum_baskets_board)

  GTHint_board = [
    "0     0",
    "       ",
    "       ",
    "       ",
    "       ",
    "       ",
    "0     0"
  ]

  GThints = { 1: {"ext_square": (0, 1), "comparator": ">" , "int_square": (1, 1)},
            2: {"ext_square": (0, 4), "comparator": "<" , "int_square": (1, 4)},
            3: {"ext_square": (2, 0), "comparator": "=" , "int_square": (2, 1)},
            4: {"ext_square": (3, 6), "comparator": ">" , "int_square": (3, 5)},
            5: {"ext_square": (5, 0), "comparator": ">" , "int_square": (5, 1)},
            6: {"ext_square": (5, 6), "comparator": "<" , "int_square": (5, 5)},
            7: {"ext_square": (6, 3), "comparator": "=" , "int_square": (5, 3)},
            8: {"ext_square": (6, 5), "comparator": "=" , "int_square": (5, 5)}}

  board = GTHintSkyscraper(5, GThints_in= GThints)
  board.solve_puzzle(GTHint_board)

  odd_even_board = [
      "0EOEEOOE0",
      "EEOOOOEEE",
      "OOEOEOOEE",
      "EOOEOEOEE",
      "EOEOEOEOE",
      "OEOEOEOOO",
      "EOEOEOEOO",
      "EEOEOEOOO",
      "0EOOEEOO0"
  ]

  board = OddEvenSkyscraper(7, odd_even_grid_in=odd_even_board)
  board.solve_puzzle(odd_even_board)
  
  #Tests for the solution puzzle requirement:

  standard_skyscraper_test = [
        "0122330",
        "1     3",
        "3     3",
        "2     2",
        "3     1",
        "2     4",
        "0213320"
    ]
  
  standard_skyscraper_solution_test = [
        [{0},{1},{2},{2},{3},{3},{0}],
        [{1},{5},{4},{2},{1},{3},{3}],
        [{3},{1},{3},{5},{4},{2},{3}],
        [{2},{3},{2},{1},{5},{4},{2}],
        [{3},{2},{1},{4},{3},{5},{1}],
        [{2},{4},{5},{3},{2},{1},{4}],
        [{0},{2},{1},{3},{3},{2},{0}]
    ]

  board = Skyscraper(5)
  board.solve_puzzle(standard_skyscraper_test)
  solution = board.solution
  assert solution == standard_skyscraper_solution_test, "Test failed: expected solution does not match actual solution."
  print("Test passed: the solution matched the expected solution.")

  sum_basket_test = [
        "0 3 30",
        "      ",
        "1     ",
        "      ",
        "3     ",
        "0    0"
    ]
  
  baskets = { 1: {"sum": 11, "squares": [(2, 2), (2, 3), (3, 2), (3, 3)]}}
  sum_basket_skyscraper_solution_test = [
        [{0},{1,2,3,4},{3},{1,2,3,4},{3},{0}],
        [{1,2,3,4},{3},{1},{4},{2},{1,2,3,4}],
        [{1},{4},{2},{3},{1},{1,2,3,4}],
        [{1,2,3,4},{1},{4},{2},{3},{1,2,3,4}],
        [{3},{2},{3},{1},{4},{1,2,3,4}],
        [{0},{1,2,3,4},{1,2,3,4},{1,2,3,4},{1,2,3,4},{0}]
    ]

  board = SumBasketSkyscraper(4, baskets_in=baskets)
  board.solve_puzzle(sum_basket_test)
  solution = board.solution
  assert solution == sum_basket_skyscraper_solution_test, "Test failed: expected solution does not match actual solution."
  print("Test passed: the solution matched the expected solution.")

  #Tests for the feedback solver requirement:

  correct_board = [
        "0322210",
        "4     1",
        "2     2",
        "2     3",
        "1     5",
        "2     3",
        "0231340"
  ]
  
  board = Skyscraper(5)
  board.solve_puzzle(correct_board)

  incorrect_board = [
        "0522210",
        "4     1",
        "2     2",
        "2     3",
        "1     5",
        "2     3",
        "0231340"
  ]

  board = Skyscraper(5)
  board.solve_puzzle(incorrect_board)

  #Tests for the complexity level requirement:

  easy_board = [
        "031323220",
        "2  36   3",
        "3       1",
        "1  5 2  2",
        "3 6    42",
        "2       3",
        "3  27   3",
        "3     3 4",
        "033122350"
    ]

  board = Skyscraper(7)
  board.solve_puzzle(easy_board)

  medium_board = [
        "043321220",
        "4     5 3",
        "3       2",
        "4    2  1",
        "3342    3",
        "2       3",
        "2   4 1 5",
        "1    1  2",
        "012324420"
    ]

  board = Skyscraper(7)
  board.solve_puzzle(medium_board)

  hard_board = [
        "032   420",
        " 3       ",
        "3       4",
        "       13",
        "2     1  ",
        "4 5      ",
        "3   1    ",
        "    3   1",
        "0  44   0"
    ]

  board = Skyscraper(7)
  board.solve_puzzle(hard_board)

  expert_big_board = [
        "053  4 40",
        "  3      ",
        "        3",
        "2       2",
        "    2    ",
        "  1      ",
        "2       3",
        "22      5",
        "0      40"
    ]

  board = Skyscraper(7)
  board.solve_puzzle(expert_big_board)

  #Tests for the grid size requirement:

  grid_size_4 = [
        "042120",
        "3    2",
        "3    1",
        "2    2",
        "1    4",
        "012330"
    ]

  
  board = Skyscraper(4)
  board.solve_puzzle(grid_size_4)

  grid_size_5 = [
        "022  10",
        "   1   ",
        "3      ",
        "       ",
        "1     2",
        "       ",
        "0   4 0"
    ]

  
  board = Skyscraper(5)
  board.solve_puzzle(grid_size_5)

  grid_size_6 = [
        "01332420",
        "1     33",
        "4 4    1",
        "2      3",
        "2    3 2",
        "2   1  2",
        "3    4 3",
        "03213240"
    ]

  
  board = Skyscraper(6)
  board.solve_puzzle(grid_size_6)

  grid_size_7 = [
        "043321220",
        "4     5 3",
        "3       2",
        "4    2  1",
        "3342    3",
        "2       3",
        "2   4 1 5",
        "1    1  2",
        "012324420"
    ]

  board = Skyscraper(7)
  board.solve_puzzle(grid_size_7)

  grid_size_8 = [
        "0233431250",
        "2    4   3",
        "36   5   2",
        "3    13  3",
        "423      2",
        "1   1  6 4",
        "3 41     3",
        "6  5     1",
        "2  23    3",
        "0214332420"
    ]

  board = Skyscraper(8)
  board.solve_puzzle(grid_size_8)

  grid_size_9 = [
        "03232235310",
        "4    4  1 1",
        "3  1   4  3",
        "1   52  6 4",
        "313  6    2",
        "44        4",
        "2    7  942",
        "2    3 2  3",
        "3 8   2 4 3",
        "456 3     3",
        "05332221450"
    ]

  board = Skyscraper(9)
  board.solve_puzzle(grid_size_9)


  

main()

  


# Easy 7 x 7 puzzle: 0.0060918331146240234 seconds
# Medium 7 x 7: 0.005488872528076172 seconds
# Hard 7x7: 0.00706791877746582 seconds
# Expert 7x7: 0.020127058029174805 seconds
# Hard 4x4: 0.0007369518280029297 seconds
# Medium 5x5 : 0.0014243125915527344 seconds
# Medium 6x6: 0.003117799758911133 seconds
# Medium 7x7: 0.005471944808959961 seconds
# Medium 8x8: 0.010318994522094727 seconds
# Medium 9x9 : 0.015100955963134766 seconds
# GTHint: 0.002574920654296875 seconds 
# Odd/Even (1): 0.0025479793548583984 seconds
# Odd/EVen (2): 0.04574275016784668 seconds
# Sum Baskets (1): 0.17772507667541504 seconds
# Sum Baskets (2): 0.03207206726074219 seconds
# Hard 5x5: 0.0020868778228759766 seconds
# Easy 6x6: 0.004044055938720703 seconds
# Expert 7x7: 0.018978118896484375 seconds
# Expert 8x8: 0.1190028190612793 seconds
# Hard 9x9: 0.12268805503845215 seconds

 


