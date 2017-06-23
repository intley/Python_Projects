#Program opens a video to let you know to take a break every two hours

import webbrowser
import time

breakcount = 0

print("This program started on " +time.ctime())
while(breakcount < 3):
    time.sleep(2 * 60*60)
    webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
    breakcount = breakcount + 1
