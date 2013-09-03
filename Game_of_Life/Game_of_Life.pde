int vidScale = 8;
int cols, rows;
int[][] matrix, temp;
boolean overSettings = false;
boolean run = false;
boolean step = false;
Button play;
Button pause;
Button clear;
Button Brandom;
Button Bstep;

void setup() {
  size(1280, 750);
  matrix = new int[1280/vidScale +1][720/vidScale +1];
  temp = new int[1280/vidScale +1][720/vidScale +1];
  cols = 1280/vidScale;
  rows = 720/vidScale;
  play = new Button("PLAY", 32, 0, 720, 100, 30, #BA0000, #FF0000, 255);
  pause = new Button("PAUSE", 32, 300, 720, 100, 30, #9C9C9C, #C2C0C0, 255);
  clear = new Button("CLEAR", 32, 600, 720, 100, 30, #9C9C9C, #C2C0C0, 255);
  Brandom = new Button("RANDOM", 24, 900, 720, 100, 30, #9C9C9C, #C2C0C0, 255);
  Bstep = new Button("STEP", 25, 1200, 720, 80, 30, #34ABFA, #0D8ADE, 255);
  for (int i = 0; i < 350; i++) {
    temp[int(random(cols-1))][int(random(rows-1))] = 1;
  }
}

void check(int i, int j) {
  int sum = 0;
  try {
    sum = matrix[i-1][j+1] + matrix[i][j+1] + matrix[i+1][j+1] + matrix[i-1][j] + matrix[i+1][j] + matrix[i-1][j-1] + matrix[i][j-1] + matrix[i+1][j-1];
  }
  catch (Exception e) {
  }
  if (sum == 3) temp[i][j] = 1;
  else if (sum == 1) temp[i][j] = 0;
  else if (sum > 3) temp[i][j] = 0;
  else temp[i][j] = matrix[i][j];
} 

void draw() {
  if (mouseY > 720) overSettings = true; 
  else overSettings = false;
  for (int i = 0; i < cols; i++) {
    for (int j = 0; j < rows; j++) {
      if (run) check(i, j);
    }
  }
  for (int i = 0; i < cols; i++) {
    for (int j = 0; j < rows; j++) {
      matrix[i][j] = temp[i][j];
      int x = i*vidScale;
      int y = j*vidScale;
      fill(temp[i][j]*255);
      stroke(50);
      rect(x, y, vidScale, vidScale);
    }
  }
  if (step) {
    run = false;
    step = false;
  }
  play.update(mouseX, mouseY);
  pause.update(mouseX, mouseY);
  clear.update(mouseX, mouseY);
  Brandom.update(mouseX, mouseY);
  Bstep.update(mouseX, mouseY);
}

void mouseDragged() {
  if (!overSettings) {
    int mcols = mouseX/vidScale;
    int mrows = mouseY/vidScale;
    if (temp[mcols][mrows] == 0) {
      temp[mcols][mrows] = 1; 
      matrix[mcols][mrows] = 1;
    }
    else {
      temp[mcols][mrows] = 0;
      matrix[mcols][mrows] = 0;
    }
  }
}

void mousePressed() {
  if (!overSettings) {
    int mcols = mouseX/vidScale;
    int mrows = mouseY/vidScale;
    if (temp[mcols][mrows] == 0) {
      temp[mcols][mrows] = 1; 
      matrix[mcols][mrows] = 1;
    }
    else {
      temp[mcols][mrows] = 0;
      matrix[mcols][mrows] = 0;
    }
  } 
  else {
    if (play.buttonOver) run = true;
    if (pause.buttonOver) run = false;
    if (clear.buttonOver) {
      for (int i = 0; i < cols; i++) {
        for (int j = 0; j < rows; j++) {
          temp[i][j] = 0;
        }
      }
    }
    if (Brandom.buttonOver) {
      for (int i = 0; i < 300; i++) {
        temp[int(random(cols-1))][int(random(rows-1))] = 1;
      }
    }
    if (Bstep.buttonOver) {
      step = true;
      run = true;
    }
  }
}

