package Package;

public class Main {
    public static void main(String[] args) {
        System.out.println("Welcome to the Yoga Dance Studio System");

        Student student = new Student(1, "Wei-Hui", "wei@example.com", "0912345678", 2023001, "Premium");
        Teacher teacher = new Teacher(2, "Ms. Wu", "wu@yogastudio.com", "0987654321", 9001, "Yoga", 3000.0f);
        Admin admin = new Admin(3, "AdminUser", "admin@yogastudio.com", "0000000000", 1);

        Course course = new Course(101, "Hot Yoga", 60, "Intermediate");
        Schedule schedule = new Schedule(1001, 101, "2025-04-05 18:00", "Studio A");

        Enrollment enrollment = new Enrollment(2001, student.enrollCourse(), course.getCourseInfo(), "Pending");
        enrollment.confirmEnrollment();

        Payment payment = new Payment(3001, Payment.processPayment(), 1500.0f, "2025-04-03", "Credit Card");
        payment.processPayment();

        Feedback feedback = new Feedback(4001, student.giveFeedback(), teacher.checkFeedback(), 5, "The teacher explained it very clearly!");
        feedback.submitFeedback();

        admin.generateReports();

        System.out.println("=== System simulation completed ===");
    }
}
