# import pyautogui
# import time
# # https://github.com/AdritoPramanik/Automation_Of_Google_Meet/tree/main

# meetingID = pyautogui.prompt(text='Enter your meeting ID', title='Meeting ID', default='')
# time.sleep(1)

# # Open Microsoft Edge
# pyautogui.press('win', interval=0.5)
# time.sleep(1)
# pyautogui.typewrite('microsoft edge', interval=0.5)
# time.sleep(1)
# pyautogui.press('enter', interval=0.5)
# time.sleep(5)  # Adjust this delay based on your system's performance

# # Type Google Meet URL
# pyautogui.typewrite('https://meet.google.com/?authser=0', interval=0.3)
# time.sleep(1)
# pyautogui.press('enter', interval=0.5)
# time.sleep(5)  # Adjust this delay based on your system's performance

# # Click on Join Button
# pyautogui.click(250, 520)
# time.sleep(2)

# # Type Meeting ID
# pyautogui.typewrite(meetingID, interval=0.2)
# time.sleep(1)

# # Press Enter to Join
# pyautogui.press('enter', interval=0.2)
# time.sleep(9)

# # Click on Camera and Microphone Buttons
# pyautogui.click(400, 570)
# time.sleep(2)
# pyautogui.click(500, 570)
# time.sleep(2)

# # Alert and Confirmation
# pyautogui.alert(text='We are entering a meeting', title='Info', button='OK')
# time.sleep(1)

# # Click on Join Meeting Button
# pyautogui.click(990, 440)

# print("Asked to join")
