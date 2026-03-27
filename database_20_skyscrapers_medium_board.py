#from FinalSolver.skyscraper import Skyscraper
#from ExperimentalClasses.skyscraper_with_iteration_board import Skyscraper
from ExperimentalClasses.skyscraper_with_LCV_heuristic import Skyscraper

def main():

  board_1 = [
          "0322210",
          "4     1",
          "2     2",
          "2     3",
          "1     5",
          "2     3",
          "0231340"
      ]
    
  board = Skyscraper(5)
  board.solve_puzzle(board_1)

  board_2 = [
        "0122330",
        "1     3",
        "3     3",
        "2     2",
        "3     1",
        "2     4",
        "0213320"
    ]
  
  board = Skyscraper(5)
  board.solve_puzzle(board_2)

  board_3 = [
        "042120",
        "3    2",
        "3    1",
        "2    2",
        "1    4",
        "012330"
    ]

  
  board = Skyscraper(4)
  board.solve_puzzle(board_3)

  board_4 = [
        "022  10",
        "   1   ",
        "3      ",
        "       ",
        "1     2",
        "       ",
        "0   4 0"
    ]

  
  board = Skyscraper(5)
  board.solve_puzzle(board_4)

  board_5 = [
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
  board.solve_puzzle(board_5)

  board_6 = [
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
  board.solve_puzzle(board_6)

  board_7 = [
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
  board.solve_puzzle(board_7)

  board_8 = [
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
  board.solve_puzzle(board_8)


  board_9 = [
        "022120",
        "3    2",
        "1    3",
        "2    1",
        "2    2",
        "031420"
    ]

  board = Skyscraper(4)
  board.solve_puzzle(board_9)

  board_10 = [
        "0   30",
        "     3",
        "      ",
        "      ",
        "     3",
        "02 2 0"
    ]

  board = Skyscraper(4)
  board.solve_puzzle(board_10)

  board_11 = [
        "0125330",
        "1     4",
        "2     3",
        "3     2",
        "4     1",
        "2     2",
        "0231320"
    ]
  
  board = Skyscraper(5)
  board.solve_puzzle(board_11)

  board_12 = [
        "0213230",
        "2     3",
        "1     2",
        "3     2",
        "4     2",
        "4     1",
        "0333210"
    ]
  
  board = Skyscraper(5)
  board.solve_puzzle(board_12)

  board_13 = [
        "02 22 0",
        "       ",
        "    2  ",
        "2     1",
        "       ",
        "      2",
        "0 5   0"
    ]
  
  board = Skyscraper(5)
  board.solve_puzzle(board_13)

  board_14 = [
        "04313320",
        "2    4 2",
        "32     1",
        "2 6    3",
        "2  3   2",
        "1   2  3",
        "5      2",
        "02332140"
    ]

  
  board = Skyscraper(6)
  board.solve_puzzle(board_14)

  board_15 = [
        "01233330",
        "1      5",
        "2  2   3",
        "2    4 2",
        "4      2",
        "2   4  3",
        "4      1",
        "03222310"
    ]

  
  board = Skyscraper(6)
  board.solve_puzzle(board_15)

  board_16 = [
        "0  4  20",
        "       3",
        "4      2",
        "4       ",
        "   2   3",
        "3       ",
        "        ",
        "04 234 0"
    ]

  
  board = Skyscraper(6)
  board.solve_puzzle(board_16)

  board_17 = [
        "022324130",
        "2      12",
        "2  21   2",
        "1 5     5",
        "2  1  4 4",
        "5 3     1",
        "2       3",
        "3       2",
        "032241320"
    ]

  board = Skyscraper(7)
  board.solve_puzzle(board_17)

  board_18 = [
        "0    0",
        "     4",
        "2     ",
        "      ",
        "      ",
        "021  0"
    ]

  
  board = Skyscraper(4)
  board.solve_puzzle(board_18)

  board_19 = [
        "0323140",
        "3     2",
        "2     2",
        "1     3",
        "3     2",
        "4     1",
        "0242210"
    ]

  
  board = Skyscraper(5)
  board.solve_puzzle(board_19)

  board_20 = [
        "02223130",
        "3  2   2",
        "3    3 2",
        "1    2 3",
        "2   5  3",
        "2      3",
        "421    1",
        "03332210"
    ]

  
  board = Skyscraper(6)
  board.solve_puzzle(board_20)



main()

  