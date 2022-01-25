#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <WiFiUdp.h>

const char *ssid = "Ookk";
const char *password = "a123456789";

WiFiUDP Udp;
unsigned int localUdpPort = 4210; // local port to listen on

IPAddress local_IP(192, 168, 25, 10); // Set your local_IP address
IPAddress gateway(192, 168, 25, 34);  // Set your Gateway IP address

IPAddress Web_IP(192, 168, 25, 119); // Set your local_IP address
unsigned int WebUdpPort = 4211;      // local port to listen on

IPAddress subnet(255, 255, 0, 0);

char incomingPacket[255];                              // buffer for incoming packets
char read_barcode[25]; // a reply string to send back

bool stringComplete = false; // whether the string is complete

void setup()
{
  Serial.begin(9600);
  Serial.println();

  Serial.printf("Connecting to %s ", ssid);
  WiFi.config(local_IP, gateway, subnet);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }
  Serial.println(" connected");

  Udp.begin(localUdpPort);
  Serial.printf("Now listening at IP %s, UDP port %d\n", WiFi.localIP().toString().c_str(), localUdpPort);
}

void loop()
{
  
  int packetSize = Udp.parsePacket();
  if (packetSize)
  {
    // receive incoming UDP packets
    // Serial.printf("Received %d bytes from %s, port %d\n", packetSize, Udp.remoteIP().toString().c_str(), Udp.remotePort());
    int len = Udp.read(incomingPacket, 255);
    if (len > 0)
    {
      incomingPacket[len] = 0;
    }
    Serial.printf("UDP packet contents: %s\n", incomingPacket);

    // send back a reply, to the IP address and port we got the packet from
  }
  

  if (stringComplete)
  {

    Udp.beginPacket(Web_IP, WebUdpPort);
    Udp.write(read_barcode);
    Udp.endPacket();

    // clear the string:
    stringComplete = false;
  }
}

unsigned char i = 0;
void serialEvent()
{
  while (Serial.available())
  {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    read_barcode[i] = inChar;
    if(++i>20)
    {
      i=20;
    }
    read_barcode[i] = 0;

    // if the incoming character is a newline, set a flag so the main loop can
    // do something about it:
    if (inChar == '\n')
    {
      stringComplete = true;
      i = 0;
    }
  }
}