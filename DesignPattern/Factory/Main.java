package Factory;

public class Main {

	public static void main(String[] args) {
		
		
		
		Document textDoc=Application.createDocument("text");
		Document csvDoc=Application.createDocument("csv");
		
		 textDoc.open();
         textDoc.save();
         textDoc.close();
         textDoc.revert();
          
         System.out.println();
         System.out.println();
         System.out.println();
         
         csvDoc.open();
         csvDoc.save();
         csvDoc.close();
         csvDoc.revert();
		
		

	}

}
