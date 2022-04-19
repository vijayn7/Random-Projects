using System;

namespace Methods_and_classes
{
    class Program
    {
        static void Main(string[] args)
        {

            MeetAlien();

            Console.WriteLine(Square(2));

            int result = MutiplyTwoNumbers(3, 5);

            if (result % 2 == 0)
            {
                Console.WriteLine("Even");
            }
            else
            {
                Console.WriteLine("Odd");
            }

            //wait for input before close
            Console.ReadKey();
        
        }

        static void MeetAlien() // how to make a method
        {
            Random numberGen = new Random(); //allows for random number

            string name = "X-" + numberGen.Next(10, 9999);
            int age = numberGen.Next(10, 500);

            Console.WriteLine("Hi, i'm " + name + ".");
            Console.WriteLine("I'm " + age + " years old.");
            Console.WriteLine("Oh, am I'm an alien.");
        }

        static int Square(int number)
        {
            int result = number*number;
            return result;
        }

        static int MutiplyTwoNumbers(int number1, int number2)
        {
            int result = number1 * number2;
            return result;
        }
    }
}
