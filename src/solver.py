public class MazeSolver {
    private final char[][] maze;
    private final boolean[][] visited;
    private final int rows, cols;
    private static final char PATH = ' ';
    private static final char VISITED = '.';
    private final int[] dx = {-1, 1, 0, 0};
    private final int[] dy = {0, 0, -1, 1};

    public MazeSolver(char[][] maze) {
        this.maze = maze;
        this.rows = maze.length;
        this.cols = maze[0].length;
        this.visited = new boolean[rows][cols];
    }
    public boolean solve() {
        return dfs(1, 1, rows - 2, cols - 2);
    }
    private boolean dfs(int x, int y, int endX, int endY) {
        if (!inBounds(x, y) || maze[x][y] != PATH || visited[x][y]) return false;

        visited[x][y] = true;
        maze[x][y] = VISITED;

        if (x == endX && y == endY) return true;

        for (int i = 0; i < 4; i++) {
            if (dfs(x + dx[i], y + dy[i], endX, endY)) return true;
        }
        maze[x][y] = PATH; // backtrack
        return false;
    }
    private boolean inBounds(int x, int y) {
        return x >= 0 && y >= 0 && x < rows && y < cols;
    }
}

