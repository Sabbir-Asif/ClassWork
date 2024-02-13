import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;


public class Main {

    public static void main(String[] args) {

        String fileName = "input.txt";
        ArrayList<Person> peopleList = new ArrayList<>();

        try (BufferedReader br = new BufferedReader(new FileReader(fileName))) {
            int numOfTeachers = Integer.parseInt(br.readLine());
            for (int i = 0; i < numOfTeachers; i++) {
                String[] teacherDetails = br.readLine().split(",");
                String name = teacherDetails[0].trim();
                String designation = teacherDetails[1].trim();
                int id = 100 + i;
                Teacher teacher = new Teacher(name, id, designation);
                peopleList.add(teacher);
            }

            int numOfStaff = Integer.parseInt(br.readLine());
            for (int i = 0; i < numOfStaff; i++) {
                String[] staffDetails = br.readLine().split(",");
                String name = staffDetails[0].trim();
                int hours = Integer.parseInt(staffDetails[1].trim());
                int id = 200 + i;
                Staff staff = new Staff(name, id, 50.0, hours);
                peopleList.add(staff);
            }

            Scanner scanner = new Scanner(System.in);
            System.out.println("Enter person name:");
            String personName = scanner.next();

            Person selectedPerson = findPerson(peopleList, personName);
            if (selectedPerson != null) {
                System.out.println("Name: " + selectedPerson.getName());
                System.out.println("Salary: " + selectedPerson.calculateSalary());
            } else {
                System.out.println("Person not found.");
            }

            scanner.close();

        } catch (IOException e) {
            e.printStackTrace();
        }

    }

    private static Person findPerson(ArrayList<Person> peopleList, String name) {
        for (Person person : peopleList) {
            if (person.getName().equalsIgnoreCase(name)) {
                return person;
            }
        }
        return null;
    }
}