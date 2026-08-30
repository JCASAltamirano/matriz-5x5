import java.util.Scanner;
public class Matriz5x5 {
    public static void main(String[] args) {
        // Objeto Scanner para permitir el ingreso de datos por consola
        Scanner sc = new Scanner(System.in);
        int[][] matriz = new int[5][5];
        System.out.println("=== INGRESE LOS DATOS A LA MATRIZ 5x5 ===");
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                System.out.print("Ingrese el valor numérico para la posición [" + i + "][" + j + "]: ");
                matriz[i][j] = sc.nextInt();
            }
        }
        System.out.println("\n=== MATRIZ INGRESADA ===");
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                System.out.print(matriz[i][j] + "\t");
            }
            System.out.println();
        }
        sc.close();
    }
}