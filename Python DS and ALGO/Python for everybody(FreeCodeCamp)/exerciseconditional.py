press_ups=input("Enter the No. Press ups: ")
press_ups_limit=input("Enter the regular press up Limit: ")
exc_press_ups=0
try:
    fpress_ups=float(press_ups)
    fpress_ups_limit=float(press_ups_limit)
except:
    print("Please enter numeric values")
    quit()

if fpress_ups>fpress_ups_limit:
    exc_press_ups=fpress_ups-fpress_ups_limit
    print("Your extra press ups: ", exc_press_ups)
else :
    print("you are exhausted, you only burn: "+ str(fpress_ups * 0.29)+" cals")

print(" your extra cals burnt today: "+ str(exc_press_ups*0.36)+" cals")
total=(exc_press_ups*0.36)+(fpress_ups_limit*0.29)
print("your total cals burnt today: extra + regular = "+str(total)+" cals")