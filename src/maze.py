// Maze.java
import java.util.Random;

public class Maze {
    private final int rows,cols;
    public char[][] grid;
    private final Random rand=new Random();

    public Maze(int rows,int cols) {
        this.rows = rows % 2 == 0 ? rows + 1 : rows;
        this.cols=cols % 2 == 0 ? cols + 1 : cols;
        grid=new char[this.rows][this.cols];
        initializeMaze();
    }
