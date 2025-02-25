# Appium-Clock-Test
Follow the instructions below to test a simple Clock mobile app using appium 
Mobile App testing Using Appium
**INSTALLATION and Requirements:**
1)	Installing Java JDK
 
 ![image](https://github.com/user-attachments/assets/d0d4344e-2170-4dde-aff8-65542ae40b82)
 ![image](https://github.com/user-attachments/assets/e9ab7c97-d040-4b1b-b9a9-d21bf94b69f5)


2)	Installing Android Studio
 ![image](https://github.com/user-attachments/assets/e88de498-d5cb-402a-94cc-58820bdb7955)
  ![image](https://github.com/user-attachments/assets/1b29db9a-a655-48ce-aea6-4f153226d6c8)

3)	Installing Appium Server
Command :
_npm install -g appium_
 ![image](https://github.com/user-attachments/assets/38406831-87d5-4ba7-9fd4-97313147d53c)

4)	Installing Appium Python client
Command :
_pip install Appium-Python-Client selenium_
 
5) Install Latest Version of Node js  
Starting Android Emulator :
![image](https://github.com/user-attachments/assets/d52e1a3e-9335-4ff9-b2e9-54537a9b458b)
![image](https://github.com/user-attachments/assets/39839727-ab4c-4cae-a344-acba6e6990f8)
 
Verify if ADB is working,
command :
_adb devices_ 
you should see something like this
![image](https://github.com/user-attachments/assets/48357b30-075f-4b79-937a-4bd330389fd5)

**else add it to path**

**Running Appium Server**
command
_appium_
![image](https://github.com/user-attachments/assets/bb4d4ed3-c04a-4100-86eb-1e7e03165f79)

**Python Test Script**:
•	Opens the Clock app
•	 Switches to the Alarm tab
•	 Adds a new alarm (Time: 07:30 AM)
•	 Saves and verifies the alarm
-> change the path link of the clock app from clock_test.py for your device 
(clock_test.py) (given in the repo)
 
**Running the Test Script** :
command:
_python clock_test.py_

