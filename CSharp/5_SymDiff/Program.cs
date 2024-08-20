List<int> list1 = new List<int> { 1, 2, 3 };
List<int> list2 = new List<int> { 3, 4, 5 };

Console.WriteLine($"[{string.Join(",", Functions.SymmetricDifference(list1, list2))}]");

public static class Functions
{
    public static List<int> SymmetricDifference(List<int> list1, List<int> list2)
    {
        // Reemplaza esto 👇por tu código 
        return new List<int>() { 1, 2, 4, 5 };
    }
}
