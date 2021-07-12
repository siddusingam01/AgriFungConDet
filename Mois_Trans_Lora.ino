/*********
  Modified from the examples of the Arduino LoRa library
  More resources: https://randomnerdtutorials.com
*********/
/*This is to transmitt hello and a number using lora*/
#include <SPI.h>
#include <LoRa.h>

//define the pins used by the transceiver module
#define ss 5
#define rst 14
#define dio0 2

int counter = 0;
float value;
int WET=2;
int DRY=16;
int sensor=A0;
float readMois()
 {
  Serial.print("MOISTURE LEVEL : ");
   value= analogRead(sensor);
  // value= value/10;
   Serial.println(value);

        if(value<150)
        {
            digitalWrite(WET, HIGH);
        }
       else
       {
           digitalWrite(DRY,HIGH);
       }

       delay(1000);

       digitalWrite(WET,LOW);

       digitalWrite(DRY, LOW);
       value= ( 100.00 - ( (value/1023.00) * 100.00 ) );
       return value;

 }



void setup() {
  //initialize Serial Monitor
  Serial.begin(115200);
  delay(10);
  pinMode(sensor,INPUT);

  while (!Serial);
  Serial.println("LoRa Sender");

  //setup LoRa transceiver module
  LoRa.setPins(ss, rst, dio0);
  
  //replace the LoRa.begin(---E-) argument with your location's frequency 
  //433E6 for Asia
  //866E6 for Europe
  //915E6 for North America
  while (!LoRa.begin(866E6)) {
    Serial.println(".");
    delay(500);
  }
   // Change sync word (0xF3) to match the receiver
  // The sync word assures you don't get LoRa messages from other LoRa transceivers
  // ranges from 0-0xFF
  LoRa.setSyncWord(0xF3);
  Serial.println("LoRa Initializing OK!");
}

void loop() {
  Serial.print("Sending packet: ");
  Serial.println(counter);

  //Send LoRa packet to receiver
  LoRa.beginPacket();
  LoRa.print(readMois());
  LoRa.print(counter);
  LoRa.endPacket();

  counter++;

  delay(10000);
}
