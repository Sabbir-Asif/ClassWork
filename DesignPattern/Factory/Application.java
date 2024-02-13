package Factory;

public  class Application {
	
	public static Document createDocument( String documentType)
	{
		if(documentType.equalsIgnoreCase("Text"))
		{
			return new TextDocument();
						
		}
		else if (documentType.equalsIgnoreCase("csv"))
				{
					return  new csvDocument();
				}
		else
			return null;
	}
	
}
