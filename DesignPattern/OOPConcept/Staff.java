class Staff extends Person {
    private double salaryPerHour;
    private int hours;

    public Staff(String name, int id, double salaryPerHour, int hours) {
        super(id, name);
        this.salaryPerHour = salaryPerHour;
        this.hours = hours;
    }

    @Override
    public double calculateSalary() {
        return salaryPerHour * hours;
    }
}
