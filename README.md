# Wigle-BT - Bluetooth Devices Trilateration Tool.
This tool allows you to get the approximate location of a Bluetooth device using the long-awaited: Wigle.net API. The tool uses trilateration to calculate the BT device location based on its signal strength and the location of nearby devices.

## Requirements
To use this tool, you need to have Python 3 installed on your system. You also need to create a free account on Wigle.net and obtain an API key.

## Installation
Clone this repository or download the ZIP file and extract it to a directory of your choice.
Create a file named config.json in the same directory as wigle-bt and add your Wigle.net API key in the following format:

{ "api_auth": "YOUR_API_KEY_HERE" }

Open a terminal or command prompt in the directory where you extracted the files and run the command:

pip3 install -r requirements.txt

...to install the required Python libraries.

## Usage
Open a terminal or command prompt in the directory where you extracted the files.

Run the command:

python3 Wigle-BT.py

Choose option 1 to get the location of a bluetooth device.

Enter the MAC address of the bluetooth device when prompted.

The tool will display the latitude and longitude of the bt device's location.

## License
This tool is licensed under the MIT license. See the LICENSE file for more information.

## Acknowledgments
This tool was created using the Wigle.net API and the trilateration algorithm developed by Thomas Pototschnig. Thanks to the developers of these tools for making this project possible.
