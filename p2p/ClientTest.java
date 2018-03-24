import javax.swing.JFrame;

public class ClientTest {
	public static void main(String[] args) {
		Client Jonkam;
		Jonkam = new Client("192.168.1.65");
		Jonkam.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		Jonkam.startRunning();
	}
}