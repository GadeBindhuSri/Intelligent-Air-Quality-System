# Hardware integration

## Recommended build
- ESP32 DevKit
- PM2.5/PM10 particulate sensor with a UART interface (for example SDS011)
- BME280 temperature/humidity sensor
- Optional CO2 sensor
- USB cable and stable power

## Important
The supplied firmware contains a clearly marked demo sensor section. Before the final hardware demo, replace those values with the actual sensor library/readings and use the correct voltage level and pinout from each sensor's datasheet.

## Network
The ESP32 and the computer running FastAPI must be reachable on the same Wi-Fi network. Change `YOUR_COMPUTER_IP` to the computer's LAN IP.

## Test without hardware
The dashboard and API already include demo readings, so you can develop the UI before assembling the circuit.
