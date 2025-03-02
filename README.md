# Banner Grabber Tool

A simple Python script to grab service banners from a target IP and port. This tool is useful for reconnaissance and identifying services running on a specific port.

## Features
- **Banner Grabbing**: Connects to a specified IP and port to retrieve the service banner.
- **User-Friendly**: Prompts the user for the target IP and port.
- **Error Handling**: Handles connection errors and timeouts gracefully.
- **ASCII Art Banner**: Displays a stylish ASCII art banner using `pyfiglet`.

## Requirements
- Python 3.x
- `pyfiglet` library

## Installation

### Clone the Repository:
```bash
git clone https://github.com/kinza099/banner-grabber.git
cd banner-grabber
```

### Install Dependencies:
Install the `pyfiglet` library if you don't already have it:
```bash
pip install pyfiglet
```

### Run the Script:
```bash
python3 banner_grabber.py
```

## Usage
Run the script:
```bash
python3 banner_grabber.py
```
Enter the target IP address and port when prompted:
```bash
Please Enter the IP Address: 192.168.1.1
Enter the Port: 22
```
The script will display the banner from the target service:
```bash
Banner from 192.168.1.1:22:
SSH-2.0-OpenSSH_7.6p1 Ubuntu-4ubuntu0.3
```

## Screenshots
Here are some screenshots demonstrating the usage of the tool:

![image](https://github.com/user-attachments/assets/98ba5cdc-9724-4333-950d-767ad633748b)


## Use Cases
- **Service Identification**: Identify the version of services running on a target (e.g., SSH, HTTP, FTP).
- **Reconnaissance**: Gather information about a target during penetration testing.
- **Network Troubleshooting**: Check if a service is running and responding correctly.


## Author
- **Your Name**
- GitHub: [kinza099](https://github.com/kinza099)
- Email: kinzapython@gmail.com

## Acknowledgments
- Inspired by basic networking and reconnaissance tools.
- Thanks to the creators of `pyfiglet` for the ASCII art library.

## License
This project is licensed under the MIT License. See the LICENSE file for details.


