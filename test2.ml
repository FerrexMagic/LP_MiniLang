SUBROUTINE int greet(string name) DO
print("Hola, " + name + "!");
return 0;
END
SUBROUTINE void main() DO
    greet("Juan");
END