class Teacher extends Person {
    private String designation;
    private double basicSalary;

    public Teacher(String name, int id, String designation) {
        super(id, name);
        this.designation = designation;
        setBasicSalary();
    }

    private void setBasicSalary() {
        switch (designation.toLowerCase()) {
            case "lecturer":
                basicSalary = 50000;
                break;
            case "assistant professor":
                basicSalary = 75000;
                break;
            case "professor":
                basicSalary = 100000;
                break;
            default:
                basicSalary = 0;
                break;
        }
    }

    @Override
    public double calculateSalary() {
        return basicSalary;
    }

    public String getDesignation() {
        return designation;
    }
}