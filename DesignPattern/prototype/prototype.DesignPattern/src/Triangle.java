public class Triangle extends Shape {
    public int base;
    public int height;

    public Triangle() {
    }

    public Triangle(Triangle target) {
        super(target);
        if (target != null) {
            this.base = target.base;
            this.height = target.height;
        }
    }

    @Override
    public Shape clone() {
        return new Triangle(this);
    }

    @Override
    public boolean equals(Object object2) {
        if (!(object2 instanceof Triangle) || !super.equals(object2)) return false;
        Triangle shape2 = (Triangle) object2;
        return shape2.base == base && shape2.height == height;
    }
}
