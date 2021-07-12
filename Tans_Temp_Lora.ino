/*********
  Modified from the examples of the Arduino LoRa library
  More resources: https://randomnerdtutorials.com
*********/
/*This is to transmitt hello and a number using lora*/
#include <SPI.h>
#include <LoRa.h>
#include <DallasTemperature.h>
#include <OneWire.h>
#define ONE_WIRE_BUS 4

//define the pins used by the transceiver module
#define ss 5
#define rst 14
#define dio0 2

OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

int counter = 0;
int sensor=A0;
float readtemp()
 {
  sensors.requestTemperatures();                // Send the command to get temperatures  
  Serial.println("Temperature is: ");
  Serial.println(sensors.getTempCByIndex(0));   // Why "byIndex"? You can have more than one IC on the same bus. 0 refers to the first IC on the wire
//  delay(500);
//  client.println(String(sensors.getTempCByIndex(0)));
//  Serial.println("0.00");
//  delay(3000);
  return sensors.getTempCByIndex(0);
 }

void setup() {
  //initialize Serial Monitor
  Serial.begin(115200);
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
  LoRa.print(readtemp()
  );
  LoRa.print(counter);
  LoRa.endPacket();

  counter++;

  delay(10000);
}
