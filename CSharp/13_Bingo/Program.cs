var carton = new List<List<int>>
{
    new List<int> { 2, 12, 33, 45, 67 },
    new List<int> { 5, 23, 45, 77, 86 },
    new List<int> { 3, 34, 46, 56, 88, 97 },
};

var numerosSorteados1 = new List<int>
{
    1, 2, 3, 5, 10, 12, 23, 33, 34,
    45, 46, 56, 67, 68, 69, 75, 76,
    77, 80, 85, 86, 87, 88, 96, 97,
};

var numerosSorteados2 = new List<int>
{
    1, 2, 3, 5, 10, 12, 23, 33, 34,
    45, 46, 56, 67, 68, 69, 75, 76,
    77, 80, 85, 86, 87, 88, 96,
};

var numerosSorteados3 = new List<int>
{
    1, 2, 3, 5, 10, 12, 23, 33, 34,
    45, 46, 56, 67, 68, 69, 75, 76,
    77, 80, 85, 86, 87, 88, 96, 97,
};

var numerosSorteados4 = new List<int>
{
    1, 2, 3, 5, 10, 12, 23, 33, 34,
    45, 46, 56, 67, 68, 69, 75, 76,
    77, 80, 85, 86, 87, 88, 96,
};

bool resultado1 = Functions.TieneBingo(carton, numerosSorteados1);
bool resultado2 = Functions.TieneBingo(carton, numerosSorteados2);
bool resultado3 = Functions.TieneBingo(carton, numerosSorteados3);
bool resultado4 = Functions.TieneBingo(carton, numerosSorteados4);

Console.WriteLine($"Resultado 1: {resultado1}");  // True
Console.WriteLine($"Resultado 2: {resultado2}");  // False
Console.WriteLine($"Resultado 3: {resultado3}");  // True
Console.WriteLine($"Resultado 4: {resultado4}");  // False

public static class Functions
{
    public static bool TieneBingo(List<List<int>> carton, List<int> numeros)
    {
        // Reemplaza esto 👇por tu código 
        return true;
    }
}

