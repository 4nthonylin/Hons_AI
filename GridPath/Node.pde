public class Node implements Comparable {
  public int x, y;
  public int g;
  public int f;
  public boolean burned = false;
  public int cost;

  public Node parent;

  public Node() {
  }
  public Node(int _x, int _y) {
    x = _x;
    y = _y;
  }
  public Node(int _x, int _y, int _c) {
    x = _x;
    y = _y;
    cost = _c;
  }

  public Node(int _x, int _y, int _g, int _f) {
    x = _x;
    y = _y;
    g = _g;
    f = _f;
  }

  public Node dCopy() {
    return new Node(x, y);
  }

  public int compareTo(Object o) {
    return this.f - ((Node)o).f;
  }
}
