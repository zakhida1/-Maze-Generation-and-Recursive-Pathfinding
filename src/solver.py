/ Solver.java
public class Solver {
    private final Maze maze;
    private final boolean[][] visited;

    public Solver(Maze maze) {
        this.maze = maze;
        visited = new boolean[maze.grid.length][maze.grid[0].length];
    }

    public boolean solve() {
        return dfs(1, 1);
    }

    private boolean dfs(int r, int c) {
        if (r < 0 || r >= maze.grid.length || c < 0 || c >= maze.grid[0].length ||
                maze.grid[r][c] == '#' || visited[r][c]) {
            return false;
        }
        visited[r][c] = true;

        if (maze.grid[r][c] == 'E') {
            return true;
        }

        if (maze.grid[r][c] != 'S') {
            maze.grid[r][c] = '.';
        }

        if (dfs(r + 1, c) || dfs(r - 1, c) || dfs(r, c + 1) || dfs(r, c - 1)) {
            return true;
        }

        if (maze.grid[r][c] != 'S') {
            maze.grid[r][c] = ' ';
        }
        return false;
    }
}
