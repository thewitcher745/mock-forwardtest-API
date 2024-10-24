# Candlestick Data API

This project is a Flask-based API that serves candlestick data from HDF5 files. The data is read from files stored in a `cached_data` directory and returned in JSON format.

## Requirements

- Python 3.x
- Flask
- Pandas

## Installation

1. Clone the repository:
    ```sh
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Ensure your HDF5 files are placed in the `cached_data` directory.

2. Run the Flask application:
    ```sh
    python main.py
    ```

3. Access the API endpoint:
    ```
    GET /<filename>
    ```

    Replace `<filename>` with the name of your HDF5 file. The endpoint will return the candlestick data in JSON format.

## Example

To get the candlestick data from a file named `data.h5`, you would make a GET request to `/data.h5`.