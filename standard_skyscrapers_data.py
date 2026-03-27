#from ExperimentalClasses.skyscraper_without_heuritics import Skyscraper
#from ExperimentalClasses.skyscraper_with_iteration_board import Skyscraper
#from ExperimentalClasses.skyscraper_without_set import Skyscraper
#from ExperimentalClasses.skyscraper_with_LCV_heuristic import Skyscraper
from FinalSolver.skyscraper import Skyscraper


def main():
  medium_board = [
        "022  10",
        "   1   ",
        "3      ",
        "       ",
        "1     2",
        "       ",
        "0   4 0"
    ]

  
  board = Skyscraper(5)
  board.solve_puzzle(medium_board)

  easy_board = [
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
  board.solve_puzzle(easy_board )


  
  hard_huge_board = [
        "0243 4   0",
        "    5 1   ",
        "4      544",
        "          ",
        "   1 54  3",
        "2        5",
        " 1     3 4",
        "5        1",
        " 7       2",
        "0 2  1 4 0"
    ]

  board = Skyscraper(8)
  board.solve_puzzle(hard_huge_board)
  
  second_hard_huge_board = [
        "0  53 2 40",
        "3   3     ",
        "3      82 ",
        "    5    2",
        "32        ",
        "   3     4",
        "31 5     4",
        "    6 2   ",
        "         1",
        "024  4   0"
    ]

  board = Skyscraper(8)
  board.solve_puzzle(second_hard_huge_board)


  third_hard_huge_board = [
        "032     40",
        "4  1     3",
        "  3      4",
        "4         ",
        "2      5  ",
        "2      1 5",
        " 1  43   2",
        "4    1    ",
        "          ",
        "0 342352 0"
    ]

  board = Skyscraper(8)
  board.solve_puzzle(third_hard_huge_board)
  

  hard_mega_board = [
        "0226332 310",
        "2     3   1",
        "2     2   3",
        "4  5 3   62",
        "3 2    8  4",
        " 7  45 19  ",
        "   6   7 5 ",
        "3   2   6  ",
        "1 52 8 6  3",
        "3   7     2",
        "02412343320"
    ]

  board = Skyscraper(9)
  board.solve_puzzle(hard_mega_board)

  hard_big_board = [
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
  board.solve_puzzle(hard_big_board)
  

main()
