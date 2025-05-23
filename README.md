## EXPLANATION

Overview
This Java project implements a maze generator using recursive backtracking and a recursive depth-first search (DFS) algorithm to find a path from a defined start point (S) to an exit point (E).The application runs in the console and provides a visual representation of both the maze and the solution path.The project is structured into modular Java classes and meets all the specified coursework requirements

## Project Objectives &Features

Generate maze using recursive backtracking	
Solve maze using recursive DFS	
Start point and exit point clearly defined	(s, e)
User-defined or default maze size 
Modular code (separate classes)	 Classes:Main,maze,solver,utils 
GitHub with 8+ commits	
Sample output provided	
Explanation and documentation

## How the program works:

1. Maze Generation (in Maze.java)
The maze is generated using a recursive backtracking algorithm
A grid of walls is initialized then paths are carved by visiting random neighbors recursively
The entrance is set at (1, 1) and the exit at (rows-2, cols-2)
The maze always has one guaranteed path from start to exit
2. Pathfinding (Solver.java)
The maze is solved using recursive depth-first search (DFS)
The method visits adjacent cells (up,down left,right) backtracking when necessary
The recursion terminates when the exit is found
3. User Input (InputHandler.java)
Reads user input from the console for maze dimensions
If invalid input is entered (non-numeric or too small) defaults are applied
4. Displaying the Maze (MazePrinter.java)
Responsible for printing the maze to the console with:
#= wall
= empty path
S = start
E = exit
. = solution path

Maze-Recursive-Java/
src/:
Main.java          
Maze.java           
Solver.java         
utils.java 
MazePrinter.java    
sample_output.txt    
README.md               
.gitignore    

 ## Algorithms Used:
1)Maze Generation-Recursive Backtracking:
Begins at a random position
Recursively carves paths in random directions
Ensures that all cells are accessible from the start

## 2)Pathfinding –Recursive DFS:
Recursively explores all directions from the current cell
Marks path if it leads to the exit,otherwise backtracks

## Constraints Fulfilled:
Maze is always solvable
Recursive algorithm only for solving
No external libraries used
Clean project structure
Input handling output,documentation















 
