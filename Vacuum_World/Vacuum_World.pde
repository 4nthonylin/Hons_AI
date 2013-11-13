/* Vacuum World
Author: Anthony Lin  
Last Edited: October 15th, 2013
*/

int[] vacuum = new int[] {
  0, 1
};
int[] dirt = new int[] {
  1, 0
};
int counter = 0;
boolean start = false;

long lastUpdate = 0;
int updateDelay = 1000;

void setup() {
  size(640, 480);
}

int invert(int number) {
  if (number == 0) number = 1;
  else number = 0;
  return number;
}

void moveLeft() {
  vacuum[0] = 1;
  vacuum[1] = 0;
}
void moveRight() {
  vacuum[0] = 0;
  vacuum[1] = 1;
}
void suck() {
  for (int x = 0; x < 2; x++) {
    if (vacuum[x] == 1) dirt[x] = 0;
  }
}
void draw() {
  clear();
  if (start) background(200);
  else background(100);
  stroke(0);
  line(0, 240, 640, 240);
  line(320, 0, 320, 480);
  for (int x = 0; x < 2; x++) {
    if (vacuum[x] == 1) {
      fill(255, 50, 20);
      rect(60 + (x*320), 20, 200, 200);
    }
    if (dirt[x] == 1) {
      fill(127, 127, 0);
      ellipse(160 + (x*320), 360, 200, 200);
    }
  }
  fill(0);
  rect(615, 5, 16, 10);
  fill(255);
  text(counter, 620, 15);
  if (start && millis() - lastUpdate > updateDelay) {
    if (dirt[0] == 1 || dirt[1] == 1) {
      if (vacuum[0] == 1) {
        if (dirt[0] == 1) suck();
        else moveRight();
      }
      else if (vacuum[1] == 1) {
        if (dirt[1] == 1) suck();
        else moveLeft();
      }
      counter++;
    }
    else start = false;
    lastUpdate = millis();
  }
}

void mousePressed() {
  if (mouseX < 320 && mouseY < 240) {
    vacuum[0] = 1;
    vacuum[1] = 0;
  }
  if (mouseX > 320 && mouseY < 240) {
    vacuum[0] = 0;
    vacuum[1] = 1;
  }
  if (mouseX < 320 && mouseY > 240) dirt[0] = invert(dirt[0]);
  if (mouseX > 320 && mouseY > 240) dirt[1] = invert(dirt[1]);
}

void keyPressed() {
  if (keyCode == ESC) start = false;
  else{
    start = true;
    lastUpdate = millis();
    counter = 0;
  }
}
