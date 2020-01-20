import time  # importing time functions

print()  # spacing
print("Hi! This program calculates the likelihood of you having ridden the same plane more than once.")
time.sleep(2)  # delay
print("Aviation estimates circa 2017 from Ascend indicate there are roughly 23,600 planes in service currently, some "
      "of which are cargo planes.")
print()  # spacing
time.sleep(3)  # delay
print("For simplicity, we are going to approximate that there are 17,600 total passenger planes currently in service.")
print()  # spacing
time.sleep(1)  # delay

# user input sections
FlightYears = input("So, how many years have you been flying?:")
FY = float(FlightYears)

print()  # spacing

FlightsPerYear = input("And roughly how many flights per year?:")
FPY = float(FlightsPerYear)

totalplanes = 17600
tp = float(totalplanes)

probability = (FY * FPY)/tp
print()  # spacing
print('The likelihood that you have ridden the same plane of your given time-frame is:',probability,'%')

# Calculating probability of having ridden the same plane in the given time period
