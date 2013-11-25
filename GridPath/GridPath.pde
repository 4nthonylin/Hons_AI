/* //<>//
  Shortest Path between two points in a Grid using A* and Greedy search
  Author: Anthony Lin
  Last Modified: November 22, 2013
*/

import java.util.*;

PriorityQueue<Node> oQueue;
PriorityQueue<Node> cQueue;
ArrayList<Node> children;
ArrayList<Node> path = new ArrayList<Node>();
boolean pathFound;
int t_g;
int t_f;
int search = 0;
Node current;
Node temp;

boolean started = false;

Grid grid;

int vidScale = 10;
int cols, rows;

void setup() {
  size(1280, 720);
  cols = 1280/vidScale;
  rows = 720/vidScale;
  grid = new Grid(cols, rows);
  rectMode(CENTER);
}

void draw() {
  background(0);
  for (int i = 0; i < cols; i++) {
    for (int j = 0; j < rows; j++) {
      switch(grid.world[i][j]) {
      case 0:
        fill(255);
        break;
      case 1:
        fill(0);
        break;
      case 2:
        fill(255, 0, 0);
        break;
      case 3:
        fill(0, 255, 0);
        break;
      case 4:
        fill(0, 0, 255);
        break;
      case 5:
        fill(0, 0, 180);
        break;
      }
      strokeWeight(1);
      stroke(50);
      rect(i*vidScale, j*vidScale, vidScale, vidScale);
    }
  }
  switch(search) {
  case 0:
    break;
  case 1:
    if (!started) aStart(new Node(grid.sX, grid.sY), new Node(grid.eX, grid.eY));
    aSearch(new Node(grid.sX, grid.sY), new Node(grid.eX, grid.eY));
    grid.world[grid.eX][grid.eY] = 3;
    grid.world[grid.sX][grid.sY] = 2;
    //delay(1);
    break;
  case 2:
    if (!started) aStart(new Node(grid.sX, grid.sY), new Node(grid.eX, grid.eY));
    gSearch(new Node(grid.sX, grid.sY), new Node(grid.eX, grid.eY));
    grid.world[grid.eX][grid.eY] = 3;
    grid.world[grid.sX][grid.sY] = 2;
    //delay(1);
    break;
  }
  if (pathFound) {
    strokeWeight(3);
    stroke(255, 255, 0);
    for (int x = 0; x < path.size()-1; x++) {
      line(vidScale*path.get(x).x, vidScale*path.get(x).y, vidScale*path.get(x+1).x, vidScale*path.get(x+1).y);
    }
  }
}

void aStart(Node start, Node finish) {
  oQueue = new PriorityQueue<Node>();
  cQueue = new PriorityQueue<Node>();
  children = new ArrayList<Node>();
  current = new Node();
  temp = new Node();

  start.g = 0;
  start.f = start.g + dDistance(start, finish);
  oQueue.add(start);
  started = true;
}

void aSearch(Node start, Node finish) {
  if (!oQueue.isEmpty () && !pathFound) {
    children = new ArrayList<Node>();
    current = oQueue.poll();
    cQueue.add(current);
    grid.world[current.x][current.y] = 4;
    if (current.x == finish.x && current.y == finish.y) {
      pathFound = true;
      while (current.parent != null) {
        path.add(current);
        current   = current.parent;
      }
      path.add(start);
    }
    children = grid.neighbors(current.x, current.y);
    for (int x = 0; x < children.size(); x++) {
      grid.world[children.get(x).x][children.get(x).y] = 5;
      t_g = current.g + children.get(x).cost;
      t_f = t_g + dDistance(children.get(x), finish);
      if (!cQueue.contains(children.get(x))) {
        temp = children.get(x).dCopy();
        temp.parent = current;
        temp.g = t_g;
        temp.f = t_f;
        if (cQueue.contains(children.get(x)) && t_f >= children.get(x).f) continue;
        if (!oQueue.contains(children.get(x))) oQueue.add(temp);
      }
    }
  }
}

void gSearch(Node start, Node finish) {
  if (!oQueue.isEmpty () && !pathFound) {
    children = new ArrayList<Node>();
    current = oQueue.poll();
    cQueue.add(current);
    grid.world[current.x][current.y] = 4;
    if (current.x == finish.x && current.y == finish.y) {
      pathFound = true;
      while (current.parent != null) {
        path.add(current);
        current   = current.parent;
      }
      path.add(start);
    }
    children = grid.neighbors(current.x, current.y);
    for (int x = 0; x < children.size(); x++) {
      grid.world[children.get(x).x][children.get(x).y] = 5;
      t_f = dDistance(children.get(x), finish);
      if (!cQueue.contains(children.get(x))) {
        temp = children.get(x).dCopy();
        temp.parent = current;
        temp.g = t_g;
        temp.f = t_f;
        if (cQueue.contains(children.get(x)) && t_f >= children.get(x).f) continue;
        if (!oQueue.contains(children.get(x))) oQueue.add(temp);
      }
    }
  }
}

int dDistance(Node a, Node b) {
  return (int)(sqrt(pow(a.x*vidScale-b.x*vidScale, 2) + pow(a.y*vidScale-b.y*vidScale, 2)));
}

void keyPressed() {
  if (key == 's') {
    grid.world[grid.sX][grid.sY] = 0;
    grid.setStart(mouseX/vidScale, mouseY/vidScale);
  }
  if (key == 'e') {
    grid.world[grid.eX][grid.eY] = 0;
    grid.setEnd(mouseX/vidScale, mouseY/vidScale);
  }
  if (key == 'a') {
    search = 1;
    
    if (!started) aStart(new Node(grid.sX, grid.sY), new Node(grid.eX, grid.eY));
    aSearch(new Node(grid.sX, grid.sY), new Node(grid.eX, grid.eY));
    grid.world[grid.eX][grid.eY] = 3;
    grid.world[grid.sX][grid.sY] = 2;
    
  }
  if (key == 'g') {
    search = 2;
    
    if (!started) aStart(new Node(grid.sX, grid.sY), new Node(grid.eX, grid.eY));
    gSearch(new Node(grid.sX, grid.sY), new Node(grid.eX, grid.eY));
    grid.world[grid.eX][grid.eY] = 3;
    grid.world[grid.sX][grid.sY] = 2;
    
  }
  if (key == 'r') {
    search = 0;
    started = false;
    pathFound = false;
    path = new ArrayList<Node>();
    for (int x = 0; x < cols; x++) {
      for (int y = 0; y < rows; y++) grid.world[x][y] = 0;
    }
  }
  if (key == 'p') {
    search = 0;
  }
}

void mouseDragged() {
  try{
  int mcols = mouseX/vidScale;
  int mrows = mouseY/vidScale;
  grid.world[mcols][mrows] = 1;
  }
  catch(Exception e){}
}

void mousePressed() {
  try{
  int mcols = mouseX/vidScale;
  int mrows = mouseY/vidScale;
  if (grid.world[mcols][mrows] == 0) grid.world[mcols][mrows] = 1; 
  else grid.world[mcols][mrows] = 0;
  }
  catch(Exception e){}
}
