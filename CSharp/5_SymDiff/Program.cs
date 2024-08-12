using System.Collections;

ArrayList list1 = new ArrayList { 1, 2, 3 };
ArrayList list2 = new ArrayList { 3, 4, 5 };

Console.WriteLine($"[{string.Join(",", Functions.SymmetricDifference(list1, list2))}]");

public static class Functions
{
    public static ArrayList SymmetricDifference(ArrayList list1, ArrayList list2)
    {
        // Reemplaza esto 👇por tu código 
        return new ArrayList() { 1, 2, 4, 5 };
    }
}

