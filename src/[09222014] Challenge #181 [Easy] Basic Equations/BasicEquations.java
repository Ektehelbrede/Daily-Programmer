import java.util.Scanner;

/**
 * Determine the intersection point of two linear equations (for example:
 * y=2x+2 and y=5x-4).
 *
 * Will attempt to read the two equations from args[0] and args[1], otherwise
 * will ask for user input. Will print the point a which these equations
 * intercept (if they do).
 *
 * @author Michael Mckee 6964289
 */

public class BasicEquations
{
  public static void main(String[] args)
  {
    // Variables to hold information about the two equations. [Split creates an
    // empty string in [0].]
    String[] equation1;
    String[] equation2;

    // [Learn more about regex.]
    String delimiters = "(y=)|(x\\+?)";

    // Variables to hold slopes, y intercepts, and (x, y) intersect coordinates.
    double m1;
    double m2;

    double b1;
    double b2;

    double intersectX;
    double intersectY;

    /*
      Try to obtain the equations from args[]. If no equation is given, obtain
      one from the user instead. The equations will be stripped of unnecessary
      parts to ease equation via the delimiter "(y=)|(x\\+?)".
     */
    try
    {
      equation1 = args[0].split(delimiters);
    }
    catch (IndexOutOfBoundsException ex)
    {
      Scanner scanner = new Scanner(System.in);
      System.out.println("Please input the first equation in the form"
        + " y=ax+b: ");
      equation1 = scanner.next().split(delimiters);
    }

    try
    {
      equation2 = args[1].split(delimiters);
    }
    catch (IndexOutOfBoundsException ex)
    {
      Scanner scanner = new Scanner(System.in);
      System.out.println("Please input the second equation in the form"
        + " y=ax+b: ");
      equation2 = scanner.next().split(delimiters);
    }

    m1 = Double.parseDouble(equation1[1]);
    m2 = Double.parseDouble(equation2[1]);

    try
    {
      b1 = Double.parseDouble(equation1[2]);
    }
    catch (IndexOutOfBoundsException ex)  // Given equation is of the form y=mx.
    {
      b1 = 0;
    }

    try
    {
      b2 = Double.parseDouble(equation2[2]);
    }
    catch (IndexOutOfBoundsException ex)  // Given equation is of the form y=mx.
    {
      b2 = 0;
    }

    intersectX = (b2 - b1) / (m1 - m2);
    intersectY = (m1 * intersectX) + b1;

    System.out.println("The given equations intersect is: " + "(" + intersectX
      + ", " + intersectY + ")");
  }
}
