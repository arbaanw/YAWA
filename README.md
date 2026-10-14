# YAWA — Yet Another Weather App 🌦️

A Python command-line weather application that fetches current weather information for a city and checks upcoming forecasts for rain. It can also send an SMS alert when rain is expected.

## Features

- **Current weather:** Displays the current temperature and feels-like temperature.
- **City geocoding:** Converts a city name into geographic coordinates.
- **Rain alerts:** Checks upcoming weather forecasts for rain.
- **SMS notifications:** Uses Twilio to send a rain alert by SMS.
- **Default city:** Saves your preferred city in a local JSON file.
- **CLI options:** Built with Typer for a convenient command-line interface.

## Tech Stack

- Python
- [Typer](https://typer.tiangolo.com/) — CLI framework
- [Requests](https://requests.readthedocs.io/) — HTTP requests
- [OpenWeatherMap](https://openweathermap.org/api) — Weather and geocoding APIs
- [Twilio](https://www.twilio.com/) — SMS notifications
- JSON — Local configuration storage

## Prerequisites

- Python 3.9+
- An OpenWeatherMap API key
- A Twilio account with SMS capabilities, if you want rain alerts

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/arbaanw/YAWA.git
cd YAWA
```

**2. Create and activate a virtual environment**

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows, activate the environment using:

```powershell
.venv\Scripts\activate
```

**3. Install dependencies**

```bash
pip install typer requests twilio
```

**4. Configure your API key**

The application imports `API_KEY` from `api_key.py`. Create that file in the project directory:

```python
API_KEY = "your_openweathermap_api_key"
```

Replace the placeholder with your OpenWeatherMap API key.

**Security:** Do not commit `api_key.py` or any real API credentials to GitHub. Add secret files to `.gitignore`.

## Usage

Run the application:

```bash
python main.py
```

On the first run, the application asks for a default city and saves it in `data.json`.

### Check the weather

```bash
python main.py weather
```

### Check the weather for a specific city

```bash
python main.py weather "Chennai"
```

### Change the default city

```bash
python main.py weather --change-city "Mumbai"
```

The default city is stored locally, so you can reuse it on subsequent runs.

## Example Output

```text
CHENNAI: 30°C (feels like 35°C)
```

*Example output only; actual temperatures depend on live weather conditions.*

## Project Structure

```text
YAWA/
├── main.py       # CLI, weather retrieval and rain alerts
├── data.json     # Saved default city
├── api_key.py    # Local API key configuration
└── README.md
```

## How It Works

1. Loads the saved city or prompts for one.
2. Retrieves the city's latitude and longitude using OpenWeatherMap's geocoding API.
3. Fetches current weather data and calculates temperatures in Celsius.
4. Checks the forecast for rain.
5. Sends an SMS alert through Twilio if the configured forecast check detects rain.
6. Prints the current temperature and feels-like temperature.

## Limitations

- Requires an internet connection and valid API credentials.
- SMS alerts require a correctly configured Twilio account and phone numbers.
- API quotas and service availability may affect functionality.
- The current implementation uses a local JSON file rather than a database.
- API errors and missing or invalid city results may require additional error handling.

## Future Improvements

- [ ] Move API credentials to environment variables.
- [ ] Add robust handling for invalid cities and API failures.
- [ ] Support configurable temperature units.
- [ ] Let users configure alert thresholds and notification preferences.
- [ ] Add scheduled forecast checks.
- [ ] Add tests for weather retrieval and city configuration.

