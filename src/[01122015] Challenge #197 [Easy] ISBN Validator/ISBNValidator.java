/**
 *  Determines if an ISBN Number is valid or not based on the definition of 
 *  a valid ISBN Number. The ISBN Number is first read from args[0], asking
 *  for user input if args[0] is empty.  
 *  
 *  @author Michael Mckee on 27/02/2015.
 *  @version 1.0
 */

import java.util.Scanner;

public class ISBNValidator 
{
    public static void main(String[] args)
    {
        String isbnNumber;
        char[] isbnNumberArray = new char[10];
        int[] isbnValues = new int[10];
        int multiplier = 10;
        int sum = 0;
        int remainder;
        
        /*
            Try to obtain the ISBN number from args[0], if this fails request
            a number from the user.
         */
        try
        {
            isbnNumber = args[0];
        }
        catch (IndexOutOfBoundsException e)
        {
            Scanner scanner = new Scanner(System.in);
            System.out.println("Please input a 10 digit ISBN number to be " +
                    "checked: ");
            isbnNumber = scanner.next();
        }
        
        isbnNumberArray = isbnNumber.toCharArray();
        
        // Convert the given String ISBN number to individual integers. The final
        // check digit may be X if representing 10.
        for (int i = 0; i < isbnValues.length - 1; i++)
        {
            isbnValues[i] = Character.getNumericValue(isbnNumberArray[i]);
        }
        
        if (isbnNumberArray[9] == 'X')
        {
            isbnValues[9] = 10;
        }
        else
        {
            isbnValues[9] = Character.getNumericValue(isbnNumberArray[9]);
        }
        
        /*
            Verify the ISBN number through the process:
                Obtain the sum of 10 times the first digit, 9 times the second
                digit, 8 times the third digit...
                If sum % 11 is 0, the ISBN is valid; otherwise it is not valid.
         */
        for (int i = 0; i < isbnValues.length; i++)
        {
            sum += multiplier * isbnValues[i];
            multiplier--;
        }
        
        remainder = sum % 11;
        
        if (remainder == 0)
        {
            System.out.println(isbnNumber + " is a valid ISBN Number!");
        }
        
        else
        {
            System.out.println(isbnNumber + " is not a valid ISBN Number.");
        }
    }
}
