#define IN1 7;
#define IN2 6; 
#define ENA 9; //H-Bridge
//defining pins

//calculate amount of time necessary for syringes to empty/fill up and put that into the necessary delays

void setup() {
  pinMode (IN1, OUTPUT);
  pinMode (IN2, OUTPUT);
  pinMode (ENA, OUTPUT);
  
  void sinkFloat();
  void floatFloat();
  void sinkFloat();
  void floatFloat();
  analogWrite(ENA, 0);
  //float goes up last time
}

void sinkFloat() {
  delay(2*60*1000); //delay 2 mins to put into water. Can be changed later.
  analogWrite(ENA, 255); //check if this should be positive 255 or -255(we need the water to go INTO the syringes
  //maybe just use the digitalWrite high and low down below?
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  //delay(how much ever time needed for the syringes to be full)
  //water uploaded; float will now sink
}

void floatFloat() {
  delay(2*60*1000); //now at seafloor
  analogWrite(ENA, 255);
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH); 
  //syringes release water
  //delay(How much time it takes for syringes to empty);
}
