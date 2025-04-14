import java.util.*;

public class MazeGenerator {
    private final int rows, cols;
    private final char[][] maze;
    private static final char WALL = '#';
    private static final char PATH = ' ';
    private final Random random = new Random();

    public MazeGenerator(int rows, int cols) {
        this.rows = rows;
        this.cols = cols;
        maze = new char[rows][cols];
        for (int i = 0; i < rows; i++) {
            Arrays.fill(maze[i], WALL);
        }
    }

    public char[][] generate() {
        generateMaze(1, 1);

        maze[1][1] = PATH;
        maze[rows - 2][cols - 2] = PATH;
        return maze;
    }

    private void generateMaze(int x, int y) {
        maze[x][y] = PATH;

        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        Collections.shuffle(Arrays.asList(directions));

        for (int[] dir : directions) {
            int nx = x + dir[0] * 2;
            int ny = y + dir[1] * 2;

            if (inBounds(nx, ny) && maze[nx][ny] == WALL) {
                maze[x + dir[0]][y + dir[1]] = PATH;
                generateMaze(nx, ny);
            }
        }
    }

    private boolean inBounds(int x, int y) {
        return x > 0 && y > 0 && x < rows - 1 && y < cols - 1;
    }
}

