# Internet Speed Test Tool

## Overview
This is a **Python-based Internet Speed Test Tool** that measures your internet connection speed. The program allows users to test their download and upload speeds either **once** or **multiple times** for a more accurate average result.

## Features
- **Measure Internet Speed:** Tests **download** and **upload** speeds.
- **Single & Average Mode:** Choose to test speed once or calculate an average over multiple runs.
- **User-Friendly Interface:** Guided instructions for smooth user experience.
- **Real-Time Processing:** Displays progress and results in a readable format.
- **Error Handling:** Detects network issues and prompts the user accordingly.

## Prerequisites
- Python 3.7+
- Install the required package:
  ```sh
  pip install speedtest-cli
  ```

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/internet-speed-test.git
   cd internet-speed-test
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
1. Run the script:
   ```sh
   python speedtest.py
   ```
2. Follow the on-screen instructions:
   - Press **'O'** to test speed once.
   - Press **'A'** to calculate the average speed over multiple runs.

## Example Output
```
Hello there! Welcome to the Internet Speed Test Tool.

To calculate ONCE, press 'O'
To calculate AVERAGE speed, press 'A'

Connecting to server...
Calculating download speed...
Calculating upload speed...

SPEED TEST RESULT:
==================
Download speed: 50.34 Mbps
Upload speed: 10.21 Mbps

Thanks for using this tool!
```

## License
This project is licensed under the **MIT License**.

## Author
Developed by Wisdom Emmanuel. Contributions are welcome!

