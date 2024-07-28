# Mobile Automation Framework

Welcome to the **Mobile Automation Framework**! This project provides a comprehensive suite for mobile application testing, enabling you to perform automated tests on both iOS and Android platforms.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Running Tests](#running-tests)
- [Contributing](#contributing)
- [License](#license)

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

Run Test:
```bash
python3 -m unittest discover -s tests -p 'test_app.py'
```
