var res1 = Functions.BuscarPalabras("Hola Mundo", "Mundo");
var res2 = Functions.BuscarPalabras("Hola Mundo", "Python");
var res3 = Functions.BuscarPalabras("Primero resuelve el problema y luego escribe el código", "el");

Console.WriteLine($"Resultado 1: [{string.Join(", ", res1)}]");
Console.WriteLine($"Resultado 2: [{string.Join(", ", res2)}]");
Console.WriteLine($"Resultado 3: [{string.Join(", ", res3)}]");

// Implementa en esta clase la función que corresponda

public static class Functions
{
    public static List<int> BuscarPalabras(string frase, string palabra)
    {
        // Reemplaza esto 👇por tu código 
        return new List<int>() { 2, 7 };
    }
}

