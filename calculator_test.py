from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time

# Desired capabilities for Clock app
capabilities = {
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
    "appium:deviceName": "emulator-5554",
    "appium:platformVersion": "15.0",
    "appium:appPackage": "com.android.deskclock",
    "appium:appActivity": ".DeskClock",
    "appium:noReset": True
}

# Start Appium session
driver = webdriver.Remote("http://127.0.0.1:4723", capabilities)

# Wait for app to load
time.sleep(2)

# Switch to "Alarm" tab (if not already selected)
try:
    alarm_tab = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Alarm")
    alarm_tab.click()
    time.sleep(2)
except:
    print("Already in Alarm tab or not found")

# Click on "Add Alarm" button
add_alarm = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Add alarm")
add_alarm.click()
time.sleep(2)

# Set Alarm Time (07:30 AM) - Adjust if needed
driver.find_element(AppiumBy.XPATH, "//android.widget.RadialTimePickerView.RadialPickerTouchHelper[@content-desc='7']").click()
driver.find_element(AppiumBy.XPATH, "//android.widget.RadialTimePickerView.RadialPickerTouchHelper[@content-desc='30']").click()

# Confirm Alarm (Click "OK" or "Save")
ok_button = driver.find_element(AppiumBy.ID, "android:id/button1")
ok_button.click()
time.sleep(2)

print("Alarm set successfully!")

# Quit driver
driver.quit()
