package Factory;

 class csvDocument  extends Document{
	
	void open()
	{
		System.out.println("Open CSV file");
	}
	void close()
	{
		System.out.println("close CSV file");
	}
	void save()
	{
		System.out.println("save CSV file");
	}
	void revert()
	{
		System.out.println("revert Text file");
	}

}
