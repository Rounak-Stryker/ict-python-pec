#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Rounak Chatterjee
#
# Created:     24-04-2022
# Copyright:   (c) Rounak Chatterjee 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import math
for angle in range(0, 350, 15):
    print(angle,"------",round(math.sin(math.radians(angle)),4)," ",round(math.cos(math.radians(angle)),4))