public class Main {
    public static void main(String[] args) {
        InputHandler inputHandler = new InputHandler();
        int[] dimensions = inputHandler.getMazeDimensions();
        int rows = dimensions[0];
        int cols = dimensions[1];

        MazeGenerator generator = new MazeGenerator(rows, cols);
        char[][] maze = generator.generate();

        MazeSolver solver = new MazeSolver(maze);
        boolean solved = solver.solve();

        System.out.println("\nGenerated Maze:");
        printMaze(maze);

        if (solved) {
            System.out.println("\nSolved Maze:");
            printMaze(maze);
        } else {
            System.out.println("\nNo path found from start to exit!");
        }

        inputHandler.close();
    }

    private static void printMaze(char[][] maze) {
        for (char[] row : maze) {
            for (char c : row) {
                System.out.print(c);
            }
            System.out.println();
        }
    }
}
