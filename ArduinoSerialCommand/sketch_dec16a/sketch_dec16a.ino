#define SERIALCOMMAND_HARDWAREONLY 1


#include <Servo.h>

// Demo Code for SerialCommand Library
// Steven Cogswell
// May 2011

// If you want to use HardwareSerial only, and not have to include SoftwareSerial support, you 
// can define SERIALCOMMAND_HARDWAREONLY in SerialCommand.h, which will cause it to build without
// SoftwareSerial support.   This makes the library act as it used to before SoftwareSerial 
// support was added, and you don't need this next include: 
//#include <SoftwareSerial.h>  

#include "SerialCommand.h"


#define arduinoLED 13   // Arduino LED on board


SerialCommand SCmd;   // The demo SerialCommand object

Servo monservo;  // crée l’objet pour contrôler le servomoteur
Servo monservo1;  // crée l’objet pour contrôler le servomoteur


void setup()
{  
  pinMode(arduinoLED,OUTPUT);      // Configure the onboard LED for output
  digitalWrite(arduinoLED,LOW);    // default to LED off
  monservo.attach(9);  // utilise la broche 9 pour le contrôle du servomoteur
  monservo.write(70);
  monservo1.attach(10);  // utilise la broche 9 pour le contrôle du servomoteur
  monservo1.write(70);

  Serial.begin(9600); 

  // Setup callbacks for SerialCommand commands 
  SCmd.addCommand("ON",LED_on);       // Turns LED on
  SCmd.addCommand("OFF",LED_off);        // Turns LED off
  SCmd.addCommand("HELLO",SayHello);     // Echos the string argument back
  SCmd.addCommand("T",process_command);  // Converts two arguments to integers and echos them back 
  SCmd.addCommand("L",process_command1);  // Converts two arguments to integers and echos them back 
  SCmd.addDefaultHandler(unrecognized);  // Handler for command that isn't matched  (says "What?") 
  Serial.println("Ready"); 

}

void loop()
{  
  SCmd.readSerial();     // We don't do much, just process serial commands
}


void LED_on()
{
  Serial.println("LED on"); 
  digitalWrite(arduinoLED,HIGH);  
}

void LED_off()
{
  Serial.println("LED off"); 
  digitalWrite(arduinoLED,LOW);
}

void SayHello()
{
  char *arg;  
  arg = SCmd.next();    // Get the next argument from the SerialCommand object buffer
  if (arg != NULL)      // As long as it existed, take it
  {
    Serial.print("Hello "); 
    Serial.println(arg); 
  } 
  else {
    Serial.println("Hello, whoever you are"); 
  }
}


void process_command()    
{
  int aNumber;  
  char *arg; 

  arg = SCmd.next(); 
  if (arg != NULL) 
  {
    aNumber=atoi(arg);    // Converts a char string to an integer
    if (aNumber > 10 && aNumber < 110){
      monservo.write(aNumber);
    }
  //  Serial.print("First argument was: "); 
  //  Serial.println(aNumber); 
  } 
  else {
    Serial.println("Mising arguments"); 
  }

}

void process_command1()    
{
  int aNumber;  
  char *arg; 
  arg = SCmd.next(); 
  if (arg != NULL) 
  {
    aNumber=atoi(arg);    // Converts a char string to an integer
    if (aNumber >= 0 && aNumber <= 180){
      monservo1.write(aNumber);
    }
    
    
  } 
  else {
    Serial.println("Mising arguments"); 
  }


}


// This gets set as the default handler, and gets called when no other command matches. 
void unrecognized()
{
  Serial.println("What?"); 
}
 
 
 
 

