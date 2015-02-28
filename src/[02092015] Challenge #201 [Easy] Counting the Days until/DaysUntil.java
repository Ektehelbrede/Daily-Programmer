/**
 *  Will take a date in the format yyyy mm dd and determine the number of days
 *  from the current time until that date. Will first try to read from args;
 *  if this fails will then prompt for user input.
 * 
 *  @author Michael Mckee on 27/02/2015.
 *  @version 1.0
 */

import java.text.DateFormat;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Scanner;

public class DaysUntil 
{
    public static void main(String[] args)
    {
        try {
            String[] currentDateArray = new String[3];
            String[] proposedDateArray = new String[3];
            String input;

            int[] proposedDate = new int[3];
            int[] currentDate = new int[3];
            int[] differences = new int[3];

            // Get the current date.
            DateFormat dateFormat = new SimpleDateFormat("yyyy MM dd");
            Date now = new Date();
            String date = dateFormat.format(now);

            currentDateArray = date.split(" ");

            // Get the proposed date by either reading from args, or by prompting
            // the user to input a date.
            try {
                for (int i = 0; i < proposedDateArray.length; i++) {
                    proposedDateArray[i] = args[i];
                }
            } catch (IndexOutOfBoundsException e) {
                Scanner scanner = new Scanner(System.in);
                System.out.println("Please input a date in the form: " +
                        "yyyy mm dd");
                input = scanner.next();

                proposedDateArray = input.split(" ");
            }

            // Convert the proposed date and the current date to integer arrays, 
            // to make math easier.
            // Then calculate the difference between the current and proposed date.
            for (int i = 0; i < proposedDate.length; i++) {
                currentDate[i] = Integer.parseInt(currentDateArray[i]);
                proposedDate[i] = Integer.parseInt(proposedDateArray[i]);
                differences[i] = proposedDate[i] - currentDate[i];
            }

            // Print the difference between the current and proposed dates.
            System.out.println("The difference between the current date and the proposed date" +
                    " is: " + differences[0] + " years, " + differences[1] + " months, " +
                    differences[2] + " days.");
        }
        catch (Exception e)
        {
            System.out.println("Input was not in the correct format, please try again.");
        }
    }
}
