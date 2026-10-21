# GUI Testing – HEX RGB Converter

A simple web-based HEX to RGB and RGB to HEX converter created for Task V.

## Features

- HEX to RGB conversion
- RGB to HEX conversion
- Input validation
- Color preview

## Technologies

- HTML
- CSS
- JavaScript
- Python
- Selenium

## Testing

The application was tested using manual UI testing and automated UI testing with Selenium.

The same 12 test cases were performed using both methods. The tests covered valid inputs, invalid inputs and boundary values for both HEX and RGB conversion.

All 12 test cases passed successfully in both manual and automated testing.

## Running the Application

Open `index.html` using a local development server such as VS Code Live Server.

## Running the Automated Tests

Make sure the application is running, then execute:

```bash
python tests/test_converter.py
```