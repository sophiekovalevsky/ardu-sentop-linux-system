#include <Adafruit_GFX.h>
#include <Adafruit_PCD8544.h>


Adafruit_PCD8544 LCD = Adafruit_PCD8544(3, 4, 5, 6, 7);

int sizeData  = 28;
char data[28];

void setup() {
  Serial.begin(9600);
  LCD.begin();
  initScreen();
  LCD.setContrast(50);
}

void loop() {
  if (Serial.available()) {
    // Wait few seconds to receive data
    Serial.readBytes(data, sizeData);
    // Clear buffer data
    Serial.flush();

    // Start creating main canvas to display data
    screenMonitor();


    delay(10);
  }
}



void initScreen() {
  LCD.clearDisplay();
  //LCD.drawBitmap(0, 0, idun, 84, 48, BLACK);
  LCD.display();
  delay(1000);
  LCD.clearDisplay();
}

void screenMonitor() {
  LCD.clearDisplay();
  LCD.setTextSize(1);
  LCD.setCursor(0,0);
  LCD.println("CPU 0:   %\nCPU 1:   %\nCPU 2:   %\nCPU 3:   %\nRAM :    /");
  LCD.display();
}