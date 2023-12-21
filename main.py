# Plyer module is used to access the features of the hardware. This module does not comes built-in with Python.
# To install this module : type 'pip install plyer' in the terminal side
# time module works with the time and is pre-installed by python default version.


from plyer import notification
import time

count = 0                                                                                 # count works with the how many times does the loop call itself

while count <=2 :                                                                         # so here, i set count less than 2 and it execute 3 times (0,1 and then 2)
    notification.notify(title='*** Drinking Water ***',                                   # set the heading

                        message='''Drinking water is essential for life,\nhealth, and well-being. It helps maintain the\nbody’s temperature, and prevents from dehydration''',    # set the description

                        timeout=2)                                                        # displaying notification time

    time.sleep(5)                                                                         # waiting time in seconds
    count = count +1                                                                      # increase the count in the loop