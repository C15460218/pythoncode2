import java.rmi.NotBoundException;
import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.Scanner;
public class Cliente {
	private static final String IP = "127.0.0.1"; // Puedes cambiar a localhost
	private static final int PUERTO = 1100; //Si cambias aquí el puerto, recuerda cambiarlo en el servidor
	
    public static void main(String[] args) throws RemoteException, NotBoundException {
        Registry registry = LocateRegistry.getRegistry(IP, PUERTO);
        Interfaz interfaz = (Interfaz) registry.lookup("Calculadora"); //Buscar en el registro...
        Scanner sc = new Scanner(System.in);
        int eleccion;
        int numero1, numero2 = 0,resultado = 0;
        float resultadod = 0.0f;
        boolean divide = false;
        String menu = "\n\n------------------\n\n[-1] => Salir\n[0] => Sumar\n[1] => Restar\n[2] => Multiplicar\n[3] => Dividir\nElige: ";
        do {
            System.out.println(menu);

            try {
                eleccion = Integer.parseInt(sc.nextLine());
            } catch (NumberFormatException e) {
                eleccion = -1;
            }

            if(eleccion != -1){

            	System.out.println("Ingresa el número 1: ");
            	try{
                	numero1 = Integer.parseInt(sc.nextLine());
            	}catch(NumberFormatException e){
            		numero1 = 0;
                }
                
                if(eleccion != 0){
                    System.out.println("Ingresa el número 2: ");
                    try{
                        numero2 = Integer.parseInt(sc.nextLine());
                    }catch(NumberFormatException e){
                        numero2 = 0;
                    }
                }
                switch (eleccion) {
	                case 0:
	                    resultado = interfaz.sumar(numero1, numero2);
	                    break;
	                case 1:
	                    resultado = interfaz.restar(numero1, numero2);
	                    break;
	                case 2:
	                    resultado = interfaz.multiplicar(numero1, numero2);
	                    break;
                    case 3:
                        divide=true;
	                    resultadod = interfaz.dividir(numero1, numero2);
                        break;
                    case 4:
                        resultadod=interfaz.areacircunferencia(numero1);
                        break;
	            }

                if (divide){
                    System.out.println("Resultado => " + String.valueOf(resultadod));
                }
                else{
                    System.out.println("Resultado => " + String.valueOf(resultado));
                }
                System.out.println("Presiona ENTER para continuar");
                sc.nextLine();
            }
        } while (eleccion != -1);
    }
}