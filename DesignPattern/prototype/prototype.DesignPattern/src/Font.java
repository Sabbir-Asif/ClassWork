public class Font {
    private String fontFamily;
    private int fontSize;

    // Constructor
    public Font(String fontFamily, int fontSize) {
        this.fontFamily = fontFamily;
        this.fontSize = fontSize;
    }

    // Copy constructor
    public Font(Font source) {
        if (source != null) {
            this.fontFamily = source.fontFamily;
            this.fontSize = source.fontSize;
        }
    }

    public String getFontFamily() {
        return fontFamily;
    }

    public int getFontSize() {
        return fontSize;
    }

    public void setFontSize(int font)
    {
        this.fontSize = font;
    }
}