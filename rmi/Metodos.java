public class Metodos {

    public Metodos(){

    }

    private static void mensaje(){
        System.out.println("Hola soy un método estático");
    }

    private int suma(int n1, int n2){
        return n1+n2;
    }

    private int resta(int n1, int n2){
        return n1-n2;
    }

    private int multiplicacion(int n1, int n2){
        return n1*n2;
    }

    private float divide(int n1, int n2){
        return (float)n1/(float)n2;
    }



    public static void main(String[] args) {

        Metodos op = new Metodos();

        System.out.println("La suma es: "+op.suma(4,5));
        System.out.println("La resta es: "+op.resta(4,5));
        System.out.println("La multiplicacióon es: "+op.multiplicacion(4,5));
        System.out.println("La división es: "+op.divide(4,5));
        mensaje();
    }
}