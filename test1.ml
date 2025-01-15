subroutine int greet(string name) do
    print("Hola, " + name + "!");
    return 0;
END
SUBROUTINE int pow(int base, int exponent)
    int pow;
    DO
    pow = 1;
    WHILE (exponent > 0) DO
        pow = pow * base;
        exponent = exponent - 1;
    END;
    return pow;
END


