const int RELE = 8;

void setup() {
  Serial.begin(9600);
  pinMode(RELE, OUTPUT);
}

void loop() {
  int status = 0; // set status to off

  while (Serial.available()>0)
  {
    status = Serial.parseInt();

        if (status==1)
        {
          digitalWrite(RELE, HIGH);
        } else {
          digitalWrite(RELE, LOW);
        }
  }

}
