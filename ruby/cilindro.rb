#cargar dato
load "circunferencia.rb"


class Cilindro < Circunferencia
    def initialize(altura)
        @a=altura
    end

    #Métodos GEt
    def getAltura()
        return @a
    end
    #Método Set
    def setAltura(cAltura)
        @a=cAltura
    end
end


#Definir el objeto Cilindro
ca = Cilindro.new(10)
ca.setRadio(8)
puts "El área del cilindro es:  #{ca.getArea(ca.getRadio())}"
puts "La altura del cilindro es: #{ca.getAltura()}"
puts "El volumen del cilindro es: #{ca.getArea(ca.getRadio())*ca.getAltura()}"