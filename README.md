# Weather App

A simple weather application built with Python and Flask that uses the OpenWeatherMap API to fetch and display current weather information for a city.

## Features

- Search weather by city name
- Displays current temperature
- Displays weather description
- Displays humidity
- Displays wind speed
- Uses OpenWeatherMap API
- Uses Flask for the web application
- Uses environment variables to securely store the API key
- Simple and user-friendly interface

## Technologies Used

- Python
- Flask
- HTML
- CSS
- Requests
- OpenWeatherMap API
- python-dotenv

## How It Works

The user enters the name of a city into the weather search form.

The Flask application sends a request to the OpenWeatherMap API using the city name and API key.

The API returns weather information in JSON format.

The application extracts the required information and displays:

- City name
- Temperature
- Weather description
- Humidity
- Wind speed

## API Integration

This project uses the OpenWeatherMap API to retrieve real-time weather data.

The API key is stored securely in a `.env` file instead of being written directly inside the Python source code.

Example `.env` file:

```env
API_KEY=your_api_key_here

## Project Structure

Weather-App/
│
├── app.py
├── .env
├── .gitignore
├── requirements.txt
│
└── templates/
    └── index.html