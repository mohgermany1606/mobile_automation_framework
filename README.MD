# Mobile Automation Framework

This is a mobile automation framework for IDNow AutoIdent for automating below scenario - 
a. Launch the application
b. Validate that the homescreen is displayed with an editbox for identid
and button labelled start ident.
c. Enteranyoneofthefollowingidentidsinthetextboxandclickstartident
button
i. TS2-LJGCD
ii. TS2-QTTUF iii. TS2-XKPSF iv. TS2-TUHYJ
v. TS2-FGAKW vi. TS2-AGJGU
vii. TS2-JRSQV viii. TS2-WEKGG ix. TS2-RWQBS
x. TS2-DWUMM
d. Validate that the terms and conditions screen is displayed
e. Click on close icon on top left corner
f. Validate the options with the reasons are displayed
g. Choose any of the option and click Quit session
h. Validate that there is an intermediate screen displayed before theapp
redirects to the home screen

# This framework is developed on MacOs platform using Visual Studio Code and Xcode 15.4

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)

## Features

- **Cross-Platform Support:** Automate tests on both iOS and Android devices.
- **Flexible Driver Setup:** Easily configure and initialize drivers for various devices and simulators/emulators.
- **Built-in Utilities:** Includes utility functions to streamline test creation and execution.

## Installation

### Prerequisites

- [Python 3.12+](https://www.python.org/downloads/)
- [Appium](https://appium.io/)
- [Xcode](https://developer.apple.com/xcode/) (for iOS testing)
- [Android Studio](https://developer.android.com/studio) (for Android testing)

### Setting Up the Project

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/mohgermany1606/mobile_automation_framework.git
    cd mobile_automation_framework
    ```

2. **Create and Activate a Virtual Environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

### Appium Server

Ensure that the Appium server is running on your machine. You can start it using:

```bash
appium
```

## Usage

### Run Test

```bash
python3 -m unittest discover -s tests -p 'test_app.py'
```
