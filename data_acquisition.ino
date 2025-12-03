#include <Wire.h>
#include <Adafruit_INA219.h>

// Thermistor setup (10k NTC, Beta 3977)
#define BETA 3977 
#define R0 10000 
#define T0 298.15 
#define PIN_UPPER A0
#define PIN_MIDDLE A1
#define PIN_LOWER A2
#define R_SERIES 10000

Adafruit_INA219 ina219;

void setup() {
  Serial.begin(9600);
  while (!Serial) { ; }

  if (!ina219.begin()) {
    Serial.println("INA219 not connected");
    while (1) { delay(10); }
  }

  // I'm using an external 0.01 ohm shunt for high current (up to 9A)
  // The library assumes 0.1 ohm, so I need to set it to max range
  // and fix the values in the loop manually.
  ina219.setCalibration_32V_2A(); 

  Serial.println("Time(s),Temp_Top,Temp_Mid,Temp_Bot,Voltage(V),Current(mA)");
}

void loop() {
  static unsigned long start = millis();
  float t_sec = (millis() - start) / 1000.0;

  // Get temps from the 3 sensors
  float t1 = getTemp(PIN_UPPER);
  float t2 = getTemp(PIN_MIDDLE);
  float t3 = getTemp(PIN_LOWER);

  float voltage = ina219.getBusVoltage_V();
  
  // Correction for the 0.01 ohm shunt
  // The library expects 0.1 ohm, so raw reading is 10x too small.
  float raw_mA = ina219.getCurrent_mA();
  float actual_mA = raw_mA * 10.0; 

  Serial.print(t_sec);
  Serial.print(",");
  Serial.print(t1);
  Serial.print(",");
  Serial.print(t2);
  Serial.print(",");
  Serial.print(t3);
  Serial.print(",");
  Serial.print(voltage);
  Serial.print(",");
  Serial.println(actual_mA);

  delay(1000); 
}

float getTemp(int pin) {
  int val = analogRead(pin);
  if (val == 0 || val >= 1023) return -273.15; // error check
  
  float v_out = val * (5.0 / 1023.0);
  float r_therm = R_SERIES * (5.0 / v_out - 1.0);
  
  // Beta formula
  float invT = (1.0 / T0) + (1.0 / BETA) * log(r_therm / R0);
  return (1.0 / invT) - 273.15; 
}