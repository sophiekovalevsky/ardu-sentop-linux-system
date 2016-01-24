/* ArduLinux
* Kiara Navarro
* sophiekovalevsky@fedoraproject.org
* http://sophiekovalevsky.github.io/
*/

#include <Adafruit_GFX.h>
#include <Adafruit_PCD8544.h>

Adafruit_PCD8544 LCD = Adafruit_PCD8544(3, 4, 5, 6, 7);

#define sizeData 35

char sentData[sizeData];

void setup() {
  Serial.begin(9600);
  LCD.begin();
  initScreen();
  LCD.setContrast(50);
}

void loop() {
  LCD.clearDisplay();
  LCD.setTextSize(1);
  LCD.setCursor(0,0);
  if (Serial.available()) {
    // Wait few seconds to receive data
    delay(10);
    Serial.readBytes(sentData, sizeData);
    // Clear buffer data
    Serial.flush();

    // Start creating main canvas to display data
    screenMonitor();

    // Print cpu data
    printCPUPercent(30,0,sentData[0],sentData[1],sentData[2],sentData[3],sentData[4]);
    printCPUPercent(30,8,sentData[5],sentData[6],sentData[7],sentData[8],sentData[9]);
    printCPUPercent(30,16,sentData[10],sentData[11],sentData[12],sentData[13],sentData[14]);
    printCPUPercent(30,24,sentData[15],sentData[16],sentData[17],sentData[18],sentData[19]);

    // Print memory data
    printMem(24,32,sentData[20],sentData[21],sentData[22],sentData[23],sentData[24]);
    //printMem(53,32,sentData[25],sentData[26],sentData[27],sentData[28],sentData[29]);
    printMem(33,32,sentData[30],sentData[31],sentData[32],sentData[33],sentData[34]);
    
    LCD.display();
    Serial.end();    
    Serial.begin(9600);
    Serial.flush();
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
  LCD.println("CPU 0:    %\nCPU 1:    %\nCPU 2:    %\nCPU 3:    %\nRAM:     /");
  LCD.display();
}

void printCPUPercent(int x, int y, char cpu1, char cpu2, char cpu3, char cpu4, char cpu5) {
  char dataBuffer[] = {cpu1, cpu2, cpu3, cpu4, cpu5, '\0'};
  LCD.setTextSize(1);
  LCD.setCursor(x,y);
  int bufferInt = atoi(dataBuffer);
  if (bufferInt < 10000) {
    if (bufferInt < 1000) {
      if (bufferInt < 100) {
        if (bufferInt < 10) {
          dataBuffer[0] = ' ';
          dataBuffer[1] = ' ';
          dataBuffer[2] = ' ';
          dataBuffer[3] = ' ';
        }
        else {
          dataBuffer[0] = ' ';
          dataBuffer[1] = ' ';
          dataBuffer[2] = ' ';
        }
      }
      else {
        dataBuffer[0] = ' ';
        dataBuffer[1] = ' ';
      }
    }
    else {
      dataBuffer[0] = ' ';
    }
  }
  LCD.println(dataBuffer);
}



void printMem(int x, int y, char mem1, char mem2, char mem3, char mem4, char mem5) {
  char dataBuffer[] = {mem1, mem2, mem3, mem4, mem5, '\0'};
  LCD.setTextSize(1);
  LCD.setCursor(x,y);
  int bufferInt = atoi(dataBuffer);
  if (bufferInt < 10000) {
    if (bufferInt < 1000) {
      if (bufferInt < 100) {
        if (bufferInt < 10) {
          dataBuffer[0] = ' ';
          dataBuffer[1] = ' ';
          dataBuffer[2] = ' ';
          dataBuffer[3] = ' ';
        }
        else {
          dataBuffer[0] = ' ';
          dataBuffer[1] = ' ';
          dataBuffer[2] = ' ';
        }
      }
      else {
        dataBuffer[0] = ' ';
        dataBuffer[1] = ' ';
      }
    }
    else {
      dataBuffer[0] = ' ';
    }
  }
  LCD.println(dataBuffer);
}
