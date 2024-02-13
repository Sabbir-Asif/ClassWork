package Factory;

public class TextDocument extends Document {
	
	void open()
	{
		System.out.println("Open Text file");
	}
	void close()
	{
		System.out.println("close Text file");
	}
	void save()
	{
		System.out.println("save Text file");
	}
	void revert()
	{
		System.out.println("revert Text file");
	}

}
