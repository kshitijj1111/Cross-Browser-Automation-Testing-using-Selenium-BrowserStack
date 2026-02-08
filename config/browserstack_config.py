import os
from selenium import webdriver

BROWSERSTACK_USERNAME = os.getenv("kshitijjadhav_OcG2Wr")
BROWSERSTACK_ACCESS_KEY = os.getenv("yne5PGsTyWsPN9MKy3y1")

if not BROWSERSTACK_USERNAME or not BROWSERSTACK_ACCESS_KEY:
    raise Exception("BrowserStack credentials not set in environment variables")

capabilities = {
    "browserName": "Chrome",
    "browserVersion": "latest",
    "os": "Windows",
    "osVersion": "11",
    "name": "Login Test",
    "build": "Cross Browser Automation Demo"
}

driver = webdriver.Remote(
    command_executor=f"https://{BROWSERSTACK_USERNAME}:{BROWSERSTACK_ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub",
    desired_capabilities=capabilities
)