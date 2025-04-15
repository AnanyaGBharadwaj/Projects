import java.util.Random;
import java.util.Scanner;
class Game {
    public int num;
    public int NumOfGuesses;
    public int input;

    public int getNumOfGuesses() {
        return NumOfGuesses;
    }

    public void setNumOfGuesses(int NumOfGuesses) {
        this.NumOfGuesses = NumOfGuesses;
    }


    Game() {
        Random r = new Random();
        this.num = r.nextInt(10);
    }

    void takeUserInput() {
        System.out.println("Guess the number");
        Scanner sc = new Scanner(System.in);
        input = sc.nextInt();
    }

    boolean isCorrectNum() {
        NumOfGuesses++;
        if (num == input) {
            System.out.format("Yes, right number is %d guessed in %d attempts\n",num,NumOfGuesses);
            return true;
        } else if (input < num) {
            System.out.println("too low");
        } else if (input > num) {
            System.out.println("too high");
        }
        return false;
    }
}
public class Main {
    public static void main(String[] args) {
        Game g = new Game();
        boolean b = false;
        while (!b) {
            g.takeUserInput();
            b = g.isCorrectNum();
            System.out.println(b);
        }
    }
}
