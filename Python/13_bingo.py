def tiene_bingo(carton: list[list[int]], numeros: list[int]):
    # Unifico los números del carton en 1 sola lista
    numeros_carton = [num for fila in carton for num in fila]

    # Recorro esa lista y si alguno no esta en números
    # entonces no tiene bingo.
    for num in numeros_carton:
        if num not in numeros:
            return False
    # Si están todos, tiene bingo.
    return True


if __name__ == "__main__":
    print(
        tiene_bingo(
            [[2, 12, 33, 45, 67], [5, 23, 45, 77, 86], [3, 34, 46, 56, 88, 97]],
            [
                1,
                2,
                3,
                5,
                10,
                12,
                23,
                33,
                34,
                45,
                46,
                56,
                67,
                68,
                69,
                75,
                76,
                77,
                80,
                85,
                86,
                87,
                88,
                96,
                97,
            ],
        )
    )  # True
    print(
        tiene_bingo(
            [[2, 12, 33, 45, 67], [5, 23, 45, 77, 86], [3, 34, 46, 56, 88, 97]],
            [
                1,
                2,
                3,
                5,
                10,
                12,
                23,
                33,
                34,
                45,
                46,
                56,
                67,
                68,
                69,
                75,
                76,
                77,
                80,
                85,
                86,
                87,
                88,
                96,
            ],
        )
    )  # False
    print(
        tiene_bingo(
            [[2, 12, 33, 45, 67], [5, 23, 45, 77, 86], [3, 34, 46, 56, 88, 97]],
            [
                1,
                2,
                3,
                5,
                10,
                12,
                23,
                33,
                34,
                45,
                46,
                56,
                67,
                68,
                69,
                75,
                76,
                77,
                80,
                85,
                86,
                87,
                88,
                96,
                97,
            ],
        )
    )  # True
    print(
        tiene_bingo(
            [[2, 12, 33, 45, 67], [5, 23, 45, 77, 86], [3, 34, 46, 56, 88, 97]],
            [
                1,
                2,
                3,
                5,
                10,
                12,
                23,
                33,
                34,
                45,
                46,
                56,
                67,
                68,
                69,
                75,
                76,
                77,
                80,
                85,
                86,
                87,
                88,
                96,
            ],
        )
    )  # True
