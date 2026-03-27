from FinalSolver.skyscraper import Skyscraper
#from ExperimentalClasses.skyscraper_with_iteration_board import Skyscraper
#from ExperimentalClasses.skyscraper_with_LCV_heuristic import Skyscraper
#from ExperimentalClasses.skyscraper_without_heuritics import Skyscraper
#from ExperimentalClasses.skyscraper_without_set import Skyscraper
def main():

  board_1 = [
        "01243522330",
        "          3",
        "4   75  8  ",
        "       9  3",
        "  1 3   4 4",
        "33    1 5 2",
        "  57  2   3",
        " 5   6 1  1",
        "2   1   3 5",
        "3  4      2",
        "03 33423130"
    ]
  
  board = Skyscraper(9)
  board.solve_puzzle(board_1)

  board_2 = [
        "0    441230",
        "3         3",
        "3     15  2",
        "   4       ",
        "2 2 8     4",
        " 6 1  4 5 2",
        "6 5    2  1",
        "21 7 2  4 4",
        "4   5     2",
        "2  3      4",
        "023 1324430"
    ]
  
  board = Skyscraper(9)
  board.solve_puzzle(board_2)

  board_3 = [
          "05431322450",
          "   3    6 5",
          "4         2",
          "3      24 3",
          "2 1   2   2",
          "2   28    4",
          " 129  5   2",
          "1    6    3",
          "6  4    5 1",
          "4         2",
          "023 2 23120"
      ]
  
  board = Skyscraper(9)
  board.solve_puzzle(board_3)

  board_4 = [
          "04 1 323440",
          "3         5",
          "2 2 1    53",
          "2     1   3",
          "3        63",
          "3  5 3  2 3",
          "5   6 4  22",
          "4 3  7 9  3",
          "2    2  6 1",
          "    4 3   2",
          "0133354 320"
      ]

  board = Skyscraper(9)
  board.solve_puzzle(board_4)

  board_5 = [
          "022 3 1 3 0",
          "          3",
          "2     73  4",
          "2 5      63",
          "1   3 1   3",
          "4 6  2   72",
          "3  9 8  5  ",
          "3  26 5   2",
          " 4 6       ",
          "4      43  ",
          "023 423 310"
      ]
  
  board = Skyscraper(9)
  board.solve_puzzle(board_5)

  board_6 = [
          "05 12233520",
          "3         3",
          "   59     5",
          "4 6     3 1",
          "     6    2",
          "2   7 96  3",
          "2  1 4    3",
          "5  6  1  4 ",
          "1   43 2  5",
          "3     2   4",
          "0234 132250"
      ]

  board = Skyscraper(9)
  board.solve_puzzle(board_6)

  board_7 = [
          "04433221240",
          "52 6      3",
          "5 6   3   2",
          "     6    3",
          "  1 2   5 2",
          "   8    1  ",
          "3   13 2  3",
          "   5   4 2 ",
          "3   9 2   2",
          "1  3      4",
          "01232343 30"
      ]
  
  board = Skyscraper(9)
  board.solve_puzzle(board_7)

  board_8 = [
          "024335321 0",
          "2         2",
          "5 3 7     2",
          "5  4   1  1",
          "4     4   3",
          "1    2   63",
          "2  2  6 5 3",
          "46  3   2 3",
          "  4 1     4",
          "3  7     2 ",
          "03223133540"
      ]

  board = Skyscraper(9)
  board.solve_puzzle(board_8)

  board_9 = [
          "0341 42 5 0",
          "2 2    8  3",
          "   2 1  3 2",
          "4   4 5   1",
          "2  3   1  4",
          "1 1 3 8  73",
          "3         2",
          " 8  6     5",
          "   1   6 53",
          "5 6 1 4   3",
          "0  32 413 0"
      ]
  
  board = Skyscraper(9)
  board.solve_puzzle(board_9)

  board_10 = [
          "03432512340",
          "5       2 3",
          "2   9     3",
          "35      3 2",
          "4 17 8     ",
          "1   5 2 6 4",
          "2 3  1    3",
          "2  6 2    2",
          "3 2 3 6   1",
          "4  3    7 4",
          "04233124320"
      ]
  
  board = Skyscraper(9)
  board.solve_puzzle(board_10)

  board_11 = [
          "023 5 42420",
          "3   1   4  ",
          "1    8 2  4",
          "   6 7   52",
          "4   7  65 1",
          "2  7 3   23",
          "3   2  39 2",
          "4 2        ",
          "4  8 2  3 4",
          "3        33",
          "032 13 3340"
      ]
  
  board = Skyscraper(9)
  board.solve_puzzle(board_11)

  board_12 = [
          "0 33244  20",
          "          3",
          "3  3 4    2",
          "2     4 5 1",
          "5    5 8   ",
          "2  4    8 3",
          "     26   2",
          "       14  ",
          "  6 2    33",
          "3         5",
          "052413 4 40"
      ]
  
  board = Skyscraper(9)
  board.solve_puzzle(board_12)

  board_13 = [
        "03242343210",
        "4      2  1",
        "23 4 86   3",
        "  5    4  2",
        "36 3    1 2",
        "1 8       5",
        "27 2 5  46 ",
        "4         3",
        "4       7 3",
        "3 7 2  6  5",
        "053133 4440"
    ]
  
  board = Skyscraper(9)
  board.solve_puzzle(board_13)

  board_14 = [
          "03342 3 120",
          "     6     ",
          "4         1",
          "1 1  7 4  2",
          "2   6 4   3",
          "4    5    3",
          "3   2   8 3",
          "27 4   3  4",
          "3 3      63",
          "33        2",
          "05 51423430"
      ]
  
  board = Skyscraper(9)
  board.solve_puzzle(board_14)

  board_15 = [
          "04122332340",
          "        4 5",
          "2 2   8   3",
          "4   1   2  ",
          "4    94   3",
          "    4 1   1",
          "  81   7 5 ",
          "5   7   1 3",
          "4      5 23",
          "1  2      2",
          "01 42 24320"
      ]
  
  board = Skyscraper(9)
  board.solve_puzzle(board_15)

  board_16 = [
          "044212 3330",
          "          3",
          "  7 4   3 4",
          "36  3     2",
          "4 4  9   73",
          "31      5  ",
          "1  5   6  4",
          "  2      1 ",
          "2   84 2   ",
          "2     2   5",
          "0412  53520"
      ]
  
  board = Skyscraper(9)
  board.solve_puzzle(board_16)

  board_17 = [
          "04433223130",
          "4         2",
          "26   4    3",
          "    4   1  ",
          "3 8 9 76 25",
          "34 6      2",
          "3 4    9  2",
          "23  8 4 7 4",
          "1         4",
          "3   1  2  1",
          "0   4 23410"
      ]

  board = Skyscraper(9)
  board.solve_puzzle(board_17)

  board_18 = [
          "043233521 0",
          "6  5  1   2",
          "26  8  5 73",
          "3 8        ",
          "2 6   5 3 1",
          "3     83  4",
          "1    1    3",
          "37      1 3",
          "3 4       3",
          "24    6   2",
          "0 134235 20"
      ]
  
  board = Skyscraper(9)
  board.solve_puzzle(board_18)

  board_19 = [
          "0 24 352310",
          "4 6 8 5   1",
          "   4     72",
          "36  9   3 3",
          "2    2 5  5",
          "4     8 9 2",
          "2   3      ",
          "43   5    4",
          "1     2    ",
          "3    3 2  3",
          "023 23   30"
      ]

  board = Skyscraper(9)
  board.solve_puzzle(board_19)

  board_20 = [
          "02 34 12  0",
          "2    2    2",
          "3 2 3    42",
          "3  3  4    ",
          "4 3       3",
          "1   8   4 3",
          "  4  9    3",
          " 8 9  3  53",
          "2    6 1  4",
          "4  4  7 5  ",
          "04  52 3410"
      ]
  
  board = Skyscraper(9)
  board.solve_puzzle(board_20)




main()