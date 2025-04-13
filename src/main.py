// Main.java
public class Main {
    public static void main(String[] args) {
        int rows =InputHandler.getMazeSize("Enter number of rows (min 10): ");
        int cols= InputHandler.getMazeSize("Enter number of columns (min 10): ");

        Maze maze = new Maze(rows,cols);
        maze.generate();

        Solver solver = new Solver(maze);
        solver.solve();

        MazePrinter.printMaze(maze);
    }
}

