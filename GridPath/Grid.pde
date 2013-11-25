public class Grid {
  public int[][] world;
  public int sX, sY, eX, eY;

  public Grid(int c, int r) {
    world = new int[c][r];
  } 

  public void setStart(int _x, int _y) {
    sX = _x;
    sY = _y;
    world[_x][_y] = 2;
  }

  public void setEnd(int _x, int _y) {
    eX = _x;
    eY = _y;
    world[_x][_y] = 3;
  }
  private boolean compare(int a, int b, int c, int d){
    return (a == b) || (a == c) || (a == d);
  }
  
  public ArrayList<Node> neighbors(int x, int y) {
    ArrayList<Node> temp = new ArrayList<Node>();
    
    if (compare(grid.world[x+1][y], 0, 2, 3)) temp.add(new Node(x+1, y, 10));
    if (compare(grid.world[x-1][y], 0, 2, 3)) temp.add(new Node(x-1, y, 10));
    if (compare(grid.world[x][y+1], 0, 2, 3)) temp.add(new Node(x, y+1, 10));
    if (compare(grid.world[x][y-1], 0, 2, 3)) temp.add(new Node(x, y-1, 10));
    if (compare(grid.world[x+1][y+1], 0, 2, 3)) temp.add(new Node(x+1, y+1, 14));
    if (compare(grid.world[x-1][y+1], 0, 2, 3)) temp.add(new Node(x-1, y+1, 14));
    if (compare(grid.world[x+1][y-1], 0, 2, 3)) temp.add(new Node(x+1, y-1, 14));
    if (compare(grid.world[x-1][y-1], 0, 2, 3)) temp.add(new Node(x-1, y-1, 14));
    return temp;
  }
}
