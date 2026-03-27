""" ===-- Backtracking Search class -----------*- Python3 -*-===//

This source file is part of the 'AI for Sudoku-Like puzzle' project developed by Jules Roussel.

===----------------------------------------------------------------------===

This is the Backtracking Search class.

===----------------------------------------------------------------------===
"""

class  BacktrackingSearch:
    # Constructor for the Backtracking Search class.

    # This constructor sets up the backtracking search process by initialising with the current state of the
    # puzzle at the point where the search begins.

    # Parameters:
    # start_from : The current state of the puzzle from which the backtracking search will start.
    #   This should be an instance of a Puzzle or its subclass that has been set up with a specific configuration
    #   and is ready to be solved.

    # Attributes:
    # start_from (Puzzle): Stores the current state of the puzzle.
    # nodes (int): A counter to track the number of nodes explored during the search to assess the algorithm's efficiency.
    def __init__(self, start_from):
        self.start_from = start_from
        self.nodes = 0

    def get_nodes_expanded(self):
        # Retrieves the number of nodes that have been explored during the backtracking search.

        # This method is used to evaluate the efficiency of the backtracking search algorithm by
        # reporting the total number of nodes that have been explored since
        # the start of the search.

        # Returns: The total number of nodes explored in the current search instance.
        return self.nodes

    def solve(self, current=None):

    # This method attempts to solve the puzzle using a recursive backtracking approach. It is the main part of the backtracking search, trying to find a solution by exploring
    # each possible state of the puzzle starting from the 'current' state. If no state is provided,
    # it starts from the initial state passed in the class constructor.

    # Parameters:
    # current (Puzzle, optional): The current state of the puzzle from which to attempt to find a solution.
    #  If none is provided, the search starts from the initial state.

    # Returns:
    # Puzzle: The solved puzzle, if a solution is found.
    # None: If no solution can be found.

    # The method increases the node count each time it is called to keep track of the number of states explored.
    # It orders potential successors based on their heuristic values to first explore the most favorable options. This approach reduce the total number of states that need to be examined.

    # Recursion continues until a solution is found or all possibilities are explored without finding a solution.

        if current is None:
            current = self.start_from

        if current.is_solution():
            return current

        self.nodes += 1
        
        sorted_successors = sorted(current.successors(), key=lambda x: x.heuristic_value())

        for successor in sorted_successors:
            solution = self.solve(successor)
            if solution is not None:
                return solution

        return None