const int ledPin = 9; 

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char state = Serial.read();
    
    if (state == '1') {
      digitalWrite(ledPin, HIGH); // Kuantum durumu: 1
    } else if (state == '0') {
      digitalWrite(ledPin, LOW);  // Kuantum durumu: 0
    }
  }
}