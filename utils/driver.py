import json
from appium import webdriver
from appium.options.ios import XCUITestOptions 

def get_driver(platform, device_type='real'):
    if platform == 'ios':
        if device_type == 'real':
            config_path = './config/ios_config_real_device.json'
        else:
            config_path = './config/ios_config.json'
    elif platform == 'android':
        if device_type == 'real':
            config_path = './config/android_config_real_device.json'
        else:
            config_path = './config/android_config.json'
    else:
        raise ValueError("Invalid platform. Only 'ios' and 'android' are supported.")

    with open(config_path, 'r') as f:
        config = json.load(f)

    capabilities = config
    options = XCUITestOptions().load_capabilities(config)
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)
    return driver
