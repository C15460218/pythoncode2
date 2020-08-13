import java.rmi.Remote;
import java.rmi.RemoteException;

/*
	Declarar firma de métodos que serán sobrescritos
*/
public interface Interfaz extends Remote {
    int sumar(int n1, int n2) throws RemoteException;
    int restar(int n1, int n2) throws RemoteException;
    int multiplicar(int n1, int n2) throws RemoteException;
    float dividir(int n1, int n2) throws RemoteException;
}