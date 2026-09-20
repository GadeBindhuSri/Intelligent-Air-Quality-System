#include <WiFi.h>
#include <HTTPClient.h>

const char* WIFI_SSID = "YOUR_WIFI_NAME";
const char* WIFI_PASSWORD = "YOUR_WIFI_PASSWORD";
const char* API_URL = "http://YOUR_COMPUTER_IP:8000/api/readings";

void setup() {
  Serial.begin(115200);
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  while (WiFi.status() != WL_CONNECTED) { delay(500); Serial.print("."); }
  Serial.println("\nWiFi connected");
}

void loop() {
  // Replace these demo values with readings from your installed sensors.
  float pm25 = 25.0;
  float pm10 = 45.0;
  float temperature = 29.0;
  float humidity = 60.0;
  float co2 = 600.0;

  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(API_URL);
    http.addHeader("Content-Type", "application/json");
    String json = "{\"pm25\":"+String(pm25,1)+",\"pm10\":"+String(pm10,1)+",\"temperature\":"+String(temperature,1)+",\"humidity\":"+String(humidity,1)+",\"co2\":"+String(co2,0)+"}";
    int code = http.POST(json);
    Serial.printf("POST status: %d\n", code);
    http.end();
  }
  delay(10000);
}
