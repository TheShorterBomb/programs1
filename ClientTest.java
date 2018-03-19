import javax.swing.JFrame;

public class ClientTest {
	public static void main(String[] args) {
		Client Jonkam;
		Jonkam = new Client("127.0.0.1");
		Jonkam.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		Jonkam.startRunning();
	}
}