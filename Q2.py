#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Rounak Chatterjee
#
# Created:     21-04-2022
# Copyright:   (c) Rounak Chatterjee 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

Gross_Income=float(input("Gross income: "))
No_of_family_members=int(input("No. of family members: "))
deduction_1=3000*No_of_family_members
deduction_2=10000
Taxable_Income=(Gross_Income-(deduction_2-(deduction_1)))
Tax=(Taxable_Income*20)/100
print("Tax =",Tax)