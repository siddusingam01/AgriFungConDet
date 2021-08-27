# AgriFungConDet
Agricultural Fugal Detection System Project Files
## About the Project:
Every year, enormous measure of harvest misfortune occurs in our nation. As indicated by records 16% of the yield misfortune in a nation is because of fungal assault. A fungal
assault requires huge measure of speculation and examination so as to recoup from it. Utilizations of fungicides will have its symptoms. These synthetic concoctions possibly gathered in land in since a long time ago run, and may likewise be cleaned out into drinking water bodies. This issue can be come through with the assistance of some innovation any and past explores did. These examines give the good states of certain each sort of growths. We additionally have sensors which are fit for detecting the diverse soil parameters. Blend of them two with the assistance of specific advances accessible in nowadays like LoRa, Cloud Data Storage will help in consistent review of the fungus in agricultural land. When the favourbale conditions are watched for a specific yield in a specific soil, the farmer can be cautioned so as to follow certain measures in order to hinder fungal development in the underlying stages itself. 

### Built With :
The following are the major components and technical aspects put into use in this Project :
- Temperature and Moisture Sensors 
- LoRa Low power long range commmunication protocol.
- io.Adafuit Cloud
- Selenium Programming in Python 
- Logestic Regression ML algorithm

## Getting Started :
### List of Components :
1. Soil Temperature Sensor DS18B20
2. Soil Moisture Sensor REES52 along with ADC (Analog to Digital Converter)
3. NodeMcu ESP8266 Wifi Board
4. LoRa RFMCW97 Transreciever module.

### Installations :
* Download the relavent Web Driver according to the Browser which you are using. The webdriver for Chrome is given. 
* Install Selenium in your Python IDLE with the following statement in the Python Prompt
           ``` pip install selenium```
* Create your account int [Adafruit.io](https://io.adafruit.com/) cloud.

## Usage :
- Connect the Soil Moisture Sensor to the one of the NodeMCU in the following way
![image](https://user-images.githubusercontent.com/69643168/125249502-ee306e80-e312-11eb-8037-a09ad04bf99a.png)

- Connect the Soil Temperature Sensor to the same NodeMCU to which the moisture sensor is connected, the following diagram assists you to do that

![image](https://user-images.githubusercontent.com/69643168/131065990-b982cdbe-7c41-471b-90c5-9b37cae85639.png)

- Take one of the LoRa Transreciever module and connect it to the same NodeMCU to which the moisture and temperature sensor are connected.

