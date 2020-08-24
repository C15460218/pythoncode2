#modulo principal 
load "funciones.rb"

ciclo = "s"
while (ciclo == "S" or ciclo == "s")
    print "--- Operaciones Básicas con Ruby ---\n"
    print "Introduce primer número: "
    n1 = Integer(gets.chomp)
    print "Introduce segundo número: "
    n2 = Integer(gets.chomp)

    print mensaje()+"\n"
    print "La suma es: ",suma(n1,n2),"\n"
    print "La resta es: ",resta(2,3),"\n"
    print "La multiplicación es: ",multiplica(2,3),"\n"
    print "La división es: ",divide(2,3),"\n"
    compara(n1,n2)
    cuenta(n1,n2)
    puts "El area de la circunferencia es: #{getArea(n1)}"
    puts "Desea otra operación? [S/N] "
    ciclo = gets.chomp
end