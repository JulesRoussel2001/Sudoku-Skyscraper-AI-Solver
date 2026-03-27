""" ===-- Breadth First Search class -----------*- Python3 -*-===//

This source file is part of the 'AI for Sudoku-Like puzzle' project developed by Jules Roussel.

===----------------------------------------------------------------------===

This is the Breadth First Search class. 
Although this class is not used in the final version of the solver, it is employed for the evaluation part of the project.

===----------------------------------------------------------------------===
"""

from collections import deque

class BreadthFirstSearch:
  def __init__(self, start_from):
    self.Q = deque([start_from])
    self.nodes = 0

  def get_nodes_expanded(self):
    return self.nodes
        
  def solve(self):
    while self.Q:
        if self.Q[0].is_solution():
          return self.Q[0]
        self.nodes += 1

        current = self.Q.popleft()
        successors = current.successors()
        for successor in successors:
          self.Q.append(successor)
    return None