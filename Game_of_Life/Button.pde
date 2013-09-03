class Button {
  String buttonName;
  int rectx, recty;
  int sizex, sizey;
  int textx;
  boolean buttonOver;
  color rectColor;
  color rectHighlight;
  color rectPress;

  Button(String name, int textshift, int x, int y, int size1, int size2, color color1, color color2, color color3) {
    textFont(loadFont("HelveticaNeue-Bold-48.vlw"), 12); 
    rectx = x;
    recty = y;
    sizex = size1;
    sizey = size2;
    textx = textshift;
    rectColor = color1;
    rectHighlight = color2;
    rectPress = color3;
    buttonName = name;
  }
  void update(int x, int y) {
    if (overButton(rectx, recty, sizex, sizey)) buttonOver = true;
    else buttonOver = false;
    
    if (buttonOver) fill(rectHighlight, 100);
    else fill(rectColor, 10);
    strokeWeight(1);
    stroke(0);
    rect(rectx, recty, sizex, sizey, 5, 5, 5, 5);
    if (buttonOver) fill(255); 
    else fill(rectHighlight  );
    fill(255);
    text(buttonName, rectx + textx, (sizey/2) + recty + ((sizey/2)/2));
  }

  boolean overButton(int x, int y, int width, int height) {
    if (mouseX >= x && mouseX <= x+width && mouseY >= y && mouseY <= y+height) return true;
    else return false;
  }
}

