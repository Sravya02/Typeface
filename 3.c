include <xc.h>
include <lcd.h> 
LiquidCrystal lcd(12, 11, 5, 4, 3, 2); 
void setup() 
{ 
    lcd.begin(16, 2); 
    lcd.print("Ambulance is approaching!");
} 
void loop() 
{
    lcd.setCursor(0,1); 
    lcd.print("Time:"); 
    for (int seconds = 60; seconds > 0; --seconds)
    {
        lcd.setCursor(6,1);
        lcd.print(seconds-1);
        delay(1000);
    }
}    