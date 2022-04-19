using System;
using System.Collections.Generic;

namespace Project_1
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Title = "Project_1"; //changes the console title
            Console.ForegroundColor = ConsoleColor.Green; //changes the text color
            Console.WindowHeight = 40; //changes the height of the window (in lines)

            Console.WriteLine("Hello, what's your name?"); //displays text in the console
            string name = Console.ReadLine();
            Console.WriteLine("Hi, " + name + ", nice to meet you");

            double num1; // creates a variable
            double num2;
            double num3;
            double num4;
            double num5;

            string[] text =
            {
                "red",
                "green",
                "blue",
                "purple"
            };

            Console.WriteLine(text[3]);

            Array.Sort(text);
            
            Console.WriteLine(text[3]);

            List<string> shoppingList = new List<string>(); //Creates a list

            shoppingList.Add("oranges"); //adds to the list
            shoppingList.Add("apples");
            shoppingList.Remove("oranges"); //removes an item from a list by text
            shoppingList.RemoveAt(0); //removes an item from a list at an index

            // use listName.count or arrayName.length to get the length of a list or array in interger form



            Console.WriteLine("\nList five numbers. Hit enter after each number");
            num1 = Convert.ToDouble(Console.ReadLine());
            num2 = Convert.ToDouble(Console.ReadLine());
            num3 = Convert.ToDouble(Console.ReadLine());
            num4 = Convert.ToDouble(Console.ReadLine());
            num5 = Convert.ToDouble(Console.ReadLine());

            Console.WriteLine("\n" + num1 + ", " + num2 + ", " + num3 + ", " + num4 + ", " + num5);

            double mean = (num1 + num2 + num3 + num4 + num5)/5;
            double allAdded = (num1 + num2 + num3 + num4 + num5);
            double allMutiplied = (num1 * num2 * num3 * num4 * num5);

            Console.WriteLine("Mean: " + mean + "\nAll Added together: " + allAdded + "\nAll Mutiplied:" + allMutiplied);

            Console.ReadKey();

        }
    }
}
