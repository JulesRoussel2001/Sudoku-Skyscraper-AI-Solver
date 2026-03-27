""" ===-- Breadth First Search class -----------*- Python3 -*-===//

This source file is part of the 'AI for Sudoku-Like puzzle' project developed by Jules Roussel.

===----------------------------------------------------------------------===

This is the Depth First Search class. 
Although this class is not used in the final version of the solver, it is employed for the evaluation part of the project.

===----------------------------------------------------------------------===
"""

class DepthFirstSearch:
  def __init__(self, start_from):
    self.start_from = start_from
    self.nodes = 0

  def get_nodes_expanded(self):
    return self.nodes
        
  def solve(self, current=None):
    if current is None:
            current = self.start_from

    if current.is_solution():
        return current

    self.nodes += 1
    for successor in current.successors():
      solution = self.solve(successor)
      if solution is not None:
          return solution
  
    return None