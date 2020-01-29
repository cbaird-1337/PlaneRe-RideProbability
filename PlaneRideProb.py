import sys
import time

#function for slow printing of text
def slowprint(s):
  for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(1./35)

if __name__ == "__main__":

    import time  # importing time functions

print()  # spacing
slowprint("Hi! This program calculates the likelihood of you having ridden the same plane more than once.")
time.sleep(1)  # delay
slowprint("Aviation estimates circa 2017 from Ascend indicate there are roughly 23,600 planes in service currently, some "
        "of which are cargo planes.")
print()  # spacing
time.sleep(3)  # delay
slowprint(
      "For simplicity, we are going to approximate that there are 17,600 total passenger planes currently in service.")
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

# Calculating probability of having ridden the same plane in the given time period
probability = (FY * FPY) / tp
print()  # spacing
print('The likelihood that you have ridden the same plane for your given time-frame is:',
        "{:.2%}".format(probability));

