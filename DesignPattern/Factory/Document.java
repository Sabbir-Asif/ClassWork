package Factory;

abstract class   Document {
	abstract  void open();
	abstract  void close();
	abstract  void save();
	abstract   void revert();
}
