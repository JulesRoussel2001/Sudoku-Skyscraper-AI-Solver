from FinalSolver.sum_basket_skyscraper import SumBasketSkyscraper
from FinalSolver.GT_hint_skyscraper import GTHintSkyscraper
from FinalSolver.odd_even_skyscraper import OddEvenSkyscraper

def main():
  medium_board = [
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
  board.solve_puzzle(medium_board)

  odd_even_board = [
      "0EOEOOO0",
      "OEEOEOOE",
      "OEOEOEOE",
      "EOOEEOEE",
      "EOEEOOEO",
      "OEOOOEEO",
      "OOEOEEOE",
      "0OOEOOE0"
  ]

  board = OddEvenSkyscraper(6, odd_even_grid_in=odd_even_board)
  board.solve_puzzle(odd_even_board)
  
  odd_even_board = [
      "0EOEOOE0",
      "EOOEEEOO",
      "EOEOEOEO",
      "EOEEEOOE",
      "OEOEOEOE",
      "EEOOOEEE",
      "OEEOOOEE",
      "0OOOEEE0"
  ]

  board = OddEvenSkyscraper(6, odd_even_grid_in=odd_even_board)
  board.solve_puzzle(odd_even_board)

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

  hard_big_board = [
          "0  5  4 0",
          "         ",
          "4        ",
          "         ",
          "        1",
          "2        ",
          "        4",
          "4        ",
          "0 4  3  0"
      ]

  baskets = { 1: {"sum": 12, "squares": [(2, 3), (2, 4), (3, 3), (3, 4)]},
              2: {"sum": 15, "squares": [(3, 5), (3, 6), (4, 5), (4, 6)]},
              3: {"sum": 20, "squares": [(4, 2), (4, 3), (5, 2), (5, 3)]},
              4: {"sum": 20, "squares": [(5, 4), (5, 5), (6, 4), (6, 5)]}}
  board = SumBasketSkyscraper(7, baskets_in=baskets)
  board.solve_puzzle(hard_big_board)
  
    
  hard_big_board = [
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
  board.solve_puzzle(hard_big_board)
  
  
main()