


int ledPin = 3;    // LED connected to digital pin 9

void setup()  { 
  // nothing happens in setup 
  Serial.begin(9600);
  
} 

void setBright(int brightness)
{
  if(brightness > 255)
  {
    digitalWrite(ledPin, LOW);
    pinMode(ledPin, INPUT);
    Serial.println("256");
    Serial.println("OK");
  }
  else
  {
    analogWrite(ledPin, brightness);
    Serial.println(brightness);
    Serial.println("OK");
  }
}

void loop()  { 
  

  while(!Serial.available());
  setBright(Serial.parseInt());
    
  
}


