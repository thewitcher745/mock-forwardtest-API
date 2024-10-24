from flask import Flask, jsonify
import pandas as pd
import os

app = Flask(__name__)


@app.route('/<filename>', methods=['GET'])
def get_candlestick_data(filename):
    try:
        # Ensure the file is in the cached_data directory
        directory = os.path.join(os.getcwd(), 'cached_data')
        file_path = os.path.join(directory, filename)

        if not os.path.exists(file_path):
            return jsonify({'error': 'File not found'}), 404

        # Read the HDF5 file
        data = pd.read_hdf(file_path)
        print(data.head())
        # Convert the DataFrame to JSON
        json_data = data.to_json(orient='records')

        return jsonify(json_data)

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)