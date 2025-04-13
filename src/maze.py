// Maze.java
import java.util.Random;

public class Maze {
    private final int rows, cols;
    public char[][] grid;
    private final Random rand = new Random();

    public Maze(int rows, int cols) {
        this.rows = rows % 2 == 0 ? rows + 1 : rows;
        this.cols = cols % 2 == 0 ? cols + 1 : cols;
        grid = new char[this.rows][this.cols];
        initializeMaze();
    }

    private void initializeMaze() {
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                grid[r][c] = '#';
            }
        }
          if (isValid(nr, nc)) {
                grid[r + dir[0] / 2][c + dir[1] / 2] = ' ';
                grid[nr][nc] = ' ';
                carvePath(nr, nc);
            }
        }
    }

    private boolean isValid(int r, int c) {
        return r > 0 && r < rows - 1 && c > 0 && c < cols - 1 && grid[r][c] == '#';
    }

    private void shuffleArray(int[][] array) {
        for (int i = array.length - 1; i > 0; i--) {
            int index = rand.nextInt(i + 1);
            int[] temp = array[i];
            array[i] = array[index];
            array[index] = temp;
        }
    }
}
   }

    public void generate() {
        carvePath(1, 1);
        grid[1][1] = 'S';
        grid[rows - 2][cols - 2] = 'E';
    }

    private void carvePath(int r, int c) {
        int[][] dirs = {{0, 2}, {2, 0}, {0, -2}, {-2, 0}};
        shuffleArray(dirs);

        for (int[] dir : dirs) {
            int nr = r + dir[0];
            int nc = c + dir[1];
   
