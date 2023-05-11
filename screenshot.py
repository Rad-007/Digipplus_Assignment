

import pyautogui,time
import winsound

time.sleep(2)

pyautogui.click(940,740)


for i in range(3):
    try:
        im=pyautogui.screenshot(region=(375,0,1145,700))
        im.save('V22_'+str(i)+'.png')

        time.sleep(0.8)

        pyautogui.click(1210,715)

        time.sleep(0.5)

    except IOError:
        im=pyautogui.screenshot(region=(375,0,1145,700))
        im.save('V22_'+str(i)+'.png')

        time.sleep(0.8)

        pyautogui.click(1210,715)

        time.sleep(0.5)

frequency=4000
duration=3000
winsound.Beep(frequency=frequency,duration=duration)

