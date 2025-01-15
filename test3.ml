SUBROUTINE int pow(int base, int exponent)
    int pow;
    SUBROUTINE int mult (int a, int b) DO
        return a * b;
    END
    DO
    pow = 1;
    WHILE (exponent > 0) DO
        pow = mult(pow, base);
        exponent = exponent - 1;
    END;
    return pow;
END