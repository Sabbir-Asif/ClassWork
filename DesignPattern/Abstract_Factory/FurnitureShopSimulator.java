public class FurnitureShopSimulator {
    private static void assembleFurniture(FurnitureFactory factory) {
        Chair chair = factory.createChair();
        Sofa sofa = factory.createSofa();
        CoffeeTable coffeeTable = factory.createCoffeeTable();

        chair.sitOn();
        sofa.lieOn();
        coffeeTable.placeCoffee();
    }

    public static void main(String[] args) {
        FurnitureFactory modernFactory = new ModernFurnitureFactory();
        FurnitureFactory victorianFactory = new VictorianFurnitureFactory();

        System.out.println("Assembling modern furniture:");
        assembleFurniture(modernFactory);

        System.out.println("\nAssembling Victorian furniture:");
        assembleFurniture(victorianFactory);
    }
}