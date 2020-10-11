#include <Romi32U4.h>
#include <PololuRPiSlave.h>
#include <Odometer.h>

Romi32U4Motors motors;
Romi32U4Encoders encoders;
Romi32U4ButtonA buttonA;
Romi32U4ButtonA btnA;

const float tickDist = .152505;
const float track = 142.5;

void setup() {
  Serial.begin(6000);

  // put your setup code here, to run once:
  ledYellow(false);
  ledGreen(true);
  ledRed(false);
}

float _debug_linear_ms = 0.25;
float _debug_angle_rs = 0.0;
void _DEBUG_PID_CONTROL() {
  static float _linear_ms_change = 0.1;
  set_twist_target(_debug_linear_ms, _debug_angle_rs);
}

void loop() {
  _DEBUG_PID_CONTROL();
  // put your main code here, to run repeatedly:
  motors.setSpeeds(50,50);
  
  if (btnA.isPressed()){
    // Turn left
    motors.setSpeeds(-50, 50);
  }
  delay(10);
}
