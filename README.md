# FastAPI Weather App with Environment Variables

This FastAPI project demonstrates how to securely use an external API (OpenWeatherMap) for fetching weather data by protecting sensitive information like API keys using environment variables.

## Prerequisites

- Python 3.7 or higher
- FastAPI
- Uvicorn
- Requests library
- python-dotenv for environment variable management

## Project Setup
### 1. Clone the Repository

Clone this repository or create the project files manually.
### 2. Install Dependencies

Install the necessary Python libraries by running the following command:

```bash
pip install fastapi uvicorn requests python-dotenv
```

### 3. Set Up Your OpenWeatherMap API Key

Sign up for an API key at OpenWeatherMap.
### 4. Create a .env File

In the root of the project directory, create a .env file to store your API key securely. Add the following content to the .env file:

```bash
WEATHER_API_KEY=your_openweathermap_api_key_here
```
Note: Replace your_openweathermap_api_key_here with your actual API key from OpenWeatherMap.

### 5. Update the Application Code

In the main.py file, the API key will be loaded from the .env file using the python-dotenv library. You don’t need to modify the key in the source code.

```python
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch API key from environment variable
API_KEY = os.getenv("WEATHER_API_KEY")
```

### 6. Add .env to .gitignore

To prevent the .env file from being committed to version control, add the following entry to the .gitignore file:

```bash

# .gitignore
.env
```

This will ensure that sensitive information (like your API key) is not exposed publicly.
## Running the Application
### 1. Run the FastAPI Application

Start the FastAPI application with Uvicorn:

```bash
uvicorn main:app --reload
```
This will run the application on http://127.0.0.1:8000.

### 2. Test the API

You can test the weather API by sending a GET request to the /weather/{city} endpoint. For example, to get the weather for London:

```bash
curl -X GET "http://127.0.0.1:8000/weather/London"
```

Example Response:

```json
{
  "city": "London",
  "temperature": 15.5,
  "weather": "clear sky",
  "humidity": 60,
  "wind_speed": 3.6
}
```

## API Documentation

FastAPI automatically generates interactive API documentation, which you can access at the following URLs:

    Swagger UI: http://127.0.0.1:8000/docs
    ReDoc: http://127.0.0.1:8000/redoc

## Security Best Practices

Environment Variables: Sensitive information such as API keys should never be hardcoded in the source code. Use environment variables and load them securely using libraries like python-dotenv.

**Add .env to .gitignore**: Always ensure that the .envfile is added to.gitignore` to prevent it from being pushed to version control.

## License

This project is licensed under the MIT License.