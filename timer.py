import time
from win11toast import toast
"""This project was a pain in the ass since some notification modules didn't have opening in url.
Some didn't even have buttons. Not even this module was perfect. This kind of stuff is made for C# or JS or C++.
It got so bad to the point where I even started adding code in JS from to run with but realized that was very stupid.
This is because Microsoft's XML Toast has no support for python which make sense since python isn't a low level language.
"""
""" 1.Get a to-do list and a timer.

    2.Set your timer for 25 minutes, and focus on a single task until the timer rings.

    3.When your session ends, mark off one pomodoro and record what you completed.

    4.Then enjoy a five-minute break.

    5.After four pomodoros, take a longer, more restorative 15-30 minute break."""
buttons1 = [
    {'activationType': 'protocol', 'arguments': 'https://www.facebook.com/marketplace/',
     'content': 'Open Marketplace'},
    {'activationType': 'protocol', 'arguments': 'none',
     'content': 'Rest'},
    {'activationType': 'protocol', 'arguments': 'none', 'content': 'Continue Working'}
]
Initial_Time = 1500  # 25 minutes seconds
Break_Time = 300  # 5 minutes seconds
Big_Break = 1800  # 30 minutes in seconds
while True:
    for i in range(4):
        toast("Your timer has started!", "Close out this notification to start it!", button="Dismiss", audio='ms-winsoundevent:Notification.Looping.Alarm')
        time.sleep(Initial_Time)

        toast('Pomodoro Timer is Over!', 'Go rest or work for 5 more mins?', buttons=buttons1, audio='ms-winsoundevent:Notification.Looping.Alarm')
        time.sleep(Break_Time)

    toast('Pomodoro Timer is Over!', 'Go rest or work for 30 more mins?', buttons=buttons1, audio='ms-winsoundevent:Notification.Looping.Alarm')
    time.sleep(Big_Break)
