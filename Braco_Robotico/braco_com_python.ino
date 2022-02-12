#include <Servo.h> 

Servo servo;

void setup() {
  Serial.begin(9600); 
  servo.attach(6);
}

void loop() {
  while (!Serial.available()){
    int x = Serial.readString().toInt();
    servo.write(x);
    Serial.println(x);    
  }
}

