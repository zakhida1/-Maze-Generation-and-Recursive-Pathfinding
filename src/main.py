import java.util.Scanner;

public class InputHandler {
    private Scanner scanner;

    public InputHandler() {
        scanner = new Scanner(System.in);
    }

    public int[] getMazeDimensions() {
        int rows, cols;
        while (true) {
            try {
                System.out.print("Enter maze dimensions (minimum 10x10): ");
                rows = scanner.nextInt();
                cols = scanner.nextInt();
                if (rows >= 10 && cols >= 10) {
                    return new int[]{rows, cols};
                } else {
                    System.out.println("Both values must be >= 10.");
                }
            } catch (Exception e) {
                System.out.println("Invalid input. Please enter two integers.");
                scanner.nextLine(); // clear buffer
            }
        }
    }

    public void close() {
        scanner.close();
    }
}
