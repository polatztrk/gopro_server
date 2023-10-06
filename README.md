# gopro_server

This Python script captures video streams from two RTMP sources (cameras) and records them into separate AVI files. The script also displays the live video streams from both cameras side by side on the screen.

## Table of Contents

- [Introduction](#introduction)
- [Usage](#usage)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This script is designed to capture video from two RTMP camera sources and perform the following tasks:

1. Record video streams from both cameras into separate AVI files.
2. Display the live video streams from both cameras side by side on the screen.
3. Allow you to stop the recording and close the video display using the 'q' key.

## Usage

To use this script:

1. Make sure you have Python installed on your system, along with the OpenCV library (`cv2`).

2. Clone or download this repository to your computer.

3. Open a terminal and navigate to the directory where you have saved the script.

4. Run the script using the following command:

   python camtest.py

5. The script will capture video from the specified RTMP sources (cameras) and display a live feed of both cameras side by side.

6. It will also record the video streams from both cameras into separate AVI files. The filenames will include a timestamp in their names.

7. To stop the recording and close the video display, press the 'q' key in the terminal where the script is running.

## Requirements

- Python (3.x recommended)
- OpenCV (cv2) library

You can install OpenCV using pip:

  pip install opencv-python

## Contributing

Contributions to this script are welcome. If you have improvements, bug fixes, or additional features to add, please feel free to open an issue or create a pull request.



