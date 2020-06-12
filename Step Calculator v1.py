print("STEP CALCULATOR")


distance = float(input("Distance to cover(in cm):"))
diameter = float(input("Enter the diameter of the wheels(in cm):"))
step_angle = float(input("Enter the step angle(in degree): "))


cir = diameter*3.14
steps_in_one_rev = 360/step_angle
total_revolutions = distance/cir
total_steps = steps_in_one_rev * total_revolutions
print("The number of steps are " + str(total_steps))  


