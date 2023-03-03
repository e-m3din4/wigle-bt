
                                          w@@@@@@@@@@@@@@@@@@@@@@w
                                       w@@@@@@@@@@@@@@@@@@@@@@@@@@@@w,
                                    q@@@@@@@KMM*""````````""*%MK@@@@@@@W
                                  @@@@@@M*`                      `*%@@@@@@,
                                 @@@@@M                              *@@@@@N
                               @@@@@                                   1@@@@@
                              @@@@@                j@W,                 `@@@@@
                             @@@@@                 j@@@@W,               `@@@@@
                            ]@@@@                  j@@@@@@@W              1@@@@N
                            @@@@                   j@@@@@@@@@@w            %@@@@
                            @@@@             ,     j@@@@D*K@@@@@@w         J@@@@N
                            @@@@           ,@@@W   j@@@@H  `@@@@@@M`        @@@@@
                            @@@@          `%@@@@@N j@@@@H,#@@@@@M`           @@@@
                            @@@N            `*@@@@@@@@@@@@@@@@M              @@@@
                            @@@N               *@@@@@@@@@@@@M                @@@@
                            @@@N                 "K@@@@@@K"                  @@@@
                            @@@N                 a@@@@@@@@W                  @@@@
                            @@@N              ,#@@@@@@@@@@@@N                @@@@
                            @@@N            ,@@@@@@K@@@@K@@@@@@p             @@@@
                            @@@@          -@@@@@@M j@@@@H *@@@@@@p           @@@@
                            @@@@           `*@K"   j@@@@H  ,@@@@@@@H         @@@@
                            @@@@H                  j@@@@N@@@@@@@M`          @@@@
                            W@@@@                  j@@@@@@@@@M`            @@@@@
                             @@@@N                 j@@@@@@M"              ]@@@@
                             V@@@@p                j@@@M"                J@@@@
                              %@@@@W               jM"                  z@@@@
                               1@@@@@                                 ,@@@@@
                                @@@@@Np                            ,#@@@@@
                                 @@@@@@Nw,                    ,a#@@@@@@
                                  "%@@@@@@@@@Kpwwwwaaawwwp@@@@@@@@@@M
                                      *K@@@@@@@@@@@@@@@@@@@@@@@@MM

                            # Wigle-BT - Bluetooth Device Trilateration Tool.

# Wigle-BT
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
