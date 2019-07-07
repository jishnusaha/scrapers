
import time
from functions import *

print("helli");

start = time.time()
print(start)
get_mobile_list()

get_mobileAccessories_list()


get_computer_list()


get_computerAccessories_list()


get_gaming_console_list()

end = time.time()
print(end)
print(end-start)
print('done')