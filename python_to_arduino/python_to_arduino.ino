void setup() {
  Serial.begin(115200);
//  Serial.setTimeout(1000);  // Increase the timeout to allow for the complete string to be received
}

void loop() {
  while (Serial.available()==0) {
    }
    String myWords = Serial.readStringUntil('\r'); // Read word until '\r'
    String addWords = ", I am Arduino.";
    Serial.println(myWords+addWords);  // Send the combined string back to Python
  }
