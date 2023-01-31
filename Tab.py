from appium import webdriver

print("Initiating Chrome driver")
desired_cap = {
            "deviceName": "Galaxy Tab 7",
             "udid": "192.168.1.17:5555",
            # "udid": "R9TR40KV9TJ",
            "platformName": "Android",
            "platformVersion": "11",
            "browserName": "Chrome"

        }

driver = webdriver.Remote(
            command_executor="http://127.0.0.1:4723/wd/hub",
            desired_capabilities=desired_cap
        )

driver.get("https://qa-admin.trado.co.il")
text = driver.get.title
print(text)