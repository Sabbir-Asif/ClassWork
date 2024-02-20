import java.util.Objects;

public abstract class Shape {
    public int x;
    public int y;
    public String color;
    public Font font;

    public Shape() {
        this.font = new Font("defaultFont", 12);
    }

    public Shape(Shape target) {
        if (target != null) {
            this.x = target.x;
            this.y = target.y;
            this.color = target.color;
            this.font = new Font(target.font);
        }
    }

    public abstract Shape clone();

    @Override
    public boolean equals(Object object2) {
        if (!(object2 instanceof Shape)) return false;
        Shape shape2 = (Shape) object2;
        return shape2.x == x && shape2.y == y && Objects.equals(shape2.color, color)
                && Objects.equals(shape2.font, font);
    }
}
