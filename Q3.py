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

seconds=int(input("Enter No. of seconds: "))
minutes=seconds//60
rem_seconds=seconds%60
print("No. of minutes =",minutes,"minutes and",rem_seconds,"seconds")