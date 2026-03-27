# Final Individual Project: 'AI for Sudoku-Like Puzzle'
### Developed by Jules Roussel

## Project Overview
This project includes an AI solver designed for solving Sudoku-like puzzles, specifically focusing on the Skyscraper puzzle and its broader family. The solver implements Constraint Satisfaction Problem techniques to efficiently solve the puzzles at different levels of complexity and sizes.

## Repository Structure
- **FinalSolver/**: Contains all the Python classes used in the final version of the Skyscraper solver.
- **ExperimentalClasses/**: Contains additional classes that were used during the evaluation phase of the project but are not part of the final solver.
- **TestFiles/**: Includes Python scripts designed to test the functionality of the Skyscraper solver.

## Getting Started

### Prerequisites
Ensure you have Python 3 installed on your system. You can verify your Python version by running: 'python --version'

### Installation instructions
1. Download the project zip file and extract it to the desired location on your computer.
2. Navigate to the extracted directory.

### Using the solver
1. Open the skyscraper_solver file located at the root of the project folder.
2. Initialise your Skyscraper grid in the form of a list of strings, where each string represent a row of the puzzle grid.
3. Initialise additional item for the vraiant if needed.
4. Create a Skyscraper object corresponding to the correct variant by passing the grid size and any additional items as parameters
5. Solve the puzzle by calling the solve_puzzle method on your Skyscraper object with your grid.


### Running the solver:
Run the solver using a Python script. For example, to solve a predefined puzzle: python skyscraper_solver.py

## Documentation
Further documentation detailing the usage of each class and method can be found in the code files as comments.

## Sources
All packages used by this solver are standard components of the Python library.

## Support
For any additional information or support, please contact jules.roussel@kcl.ac.uk.
