/*
  Hello World.ino
  2013 Copyright (c) Seeed Technology Inc.  All right reserved.

  Author:Loovee
  2013-9-18

  Grove - Serial LCD RGB Backlight demo.

  This library is free software; you can redistribute it and/or
  modify it under the terms of the GNU Lesser General Public
  License as published by the Free Software Foundation; either
  version 2.1 of the License, or (at your option) any later version.

  This library is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
  Lesser General Public License for more details.

  You should have received a copy of the GNU Lesser General Public
  License along with this library; if not, write to the Free Software
  Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
*/

#include <Wire.h>
#include "rgb_lcd.h"


rgb_lcd lcd;

const int colorR = 255;
const int colorG = 0;
const int colorB = 0;

int led = 9;           // the PWM pin the LED is attached to
int minimum = 20;
int incomingInt = 0;


void setup() 
{
  Serial.begin(9600);

  Serial.println("ready");

  // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
  lcd.setRGB(colorR, colorG, colorB);
}


void loop() 
{
  if (Serial.available() > 0) {
    set_bright(Serial.parseInt());
  }

}

void set_bright(int brightness)
{

    
  // clamp brightness to above 20, 
  // any value above 255 sets the pin High-Z, makes the lamp brightest

if (brightness < minimum)
{
  brightness = minimum;
}

  if (brightness < 256) {
    pinMode(led, OUTPUT);
    analogWrite(led, brightness);
    lcd.clear();
      lcd.setCursor(0, 1);
  lcd.print(brightness);
  } else {
    pinMode(led, INPUT);
        lcd.clear();
          lcd.setCursor(0, 1);
          lcd.print("Max");
  } 

  return;
}



/*********************************************************************************************************
  END FILE
*********************************************************************************************************/
