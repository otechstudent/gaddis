# Shipping Charges
RPP1 = 1.5
RPP2 = 3.0
RPP3 = 4.0
RPP4 = 4.75

weight = float(input('Enter the weight of your package (in pounds): '))

if weight > 10:
    rate_per_pound = RPP4
elif weight > 6 and weight <= 10:
    rate_per_pound = RPP3
elif weight > 2 and weight <= 6:
    rate_per_pound = RPP2
else:
    rate_per_pound = RPP1

shipping_charge = weight * rate_per_pound
print("The shipping charge for ", weight,
      " pounds is $", shipping_charge, '.', sep='')
