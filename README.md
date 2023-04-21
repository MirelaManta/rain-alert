# Rain Alert System

This project uses the __OpenWeatherMap API__ and the __Twilio API__ to send an SMS message alerting the user if it will rain in the next 12 hours. The program checks the weather forecast for a specified location based on its latitude and longitude and sends a message to the user's phone number if it will rain.
## Installation

To run this program, you will need to install the following dependencies:
* __Python 3__
* __requests__
* __twilio__

You will also need to set up accounts with the OpenWeatherMap API and the Twilio API and obtain API keys.
## Usage
To use this program, you will need to set the following environment variables:
* OWM_API_KEY: your OpenWeatherMap API key
* AUTH_TOKEN: your Twilio authentication token

You can then run the program using the following command:
```
python main.py
```
