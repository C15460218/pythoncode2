# clase que muestra la herencia en ruby
load "punto.rb"

class Circunferencia < Punto
    def initialize(vRadio)
        @radio=vRadio
    end

    #Métodos GEt
    def getRadio()
        return @radio
    end
    #Método Set
    def setRadio(vRadio)
        @radio=vRadio
    end

    #Escribir un método que calcule el área de la circunferencia
    def getArea(vRadio)
        return Math::PI * (vRadio**2)
    end

end

cir = Circunferencia.new(3)

puts "El radio es: #{cir.getRadio()}"
cir.setX(10)
cir.setY(10)
puts "las coordenadas son: #{cir.getX()}, #{cir.getY()}"
puts "EL area de la circunferencia es: #{cir.getArea(cir.getRadio)}"