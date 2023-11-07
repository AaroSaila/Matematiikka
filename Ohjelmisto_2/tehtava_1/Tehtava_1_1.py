import numpy

a1 = 2.493  # rad
b1 = 0.911  # rad

a2 = 137.7  # deg
b2 = 62.3   # deg

A = numpy.array([30, 45, 60, 90, 120, 135, 150, 180, 270, 360])

print(f"""
1. Muunna asteiksi:
    a) 2.493 rad = {numpy.degrees(a1):0.3f} deg     b) 0.911 rad = {numpy.degrees(b1):0.3f} deg
    
2. Muunna radiaaneiksi:
    a) 137.7 deg = {numpy.radians(a2):0.1f} rad      b) 62.3 deg = {numpy.radians(b2):0.1f} rad
""")

for i in A:
    result = numpy.radians(i)
    print(f"{i} astetta on noin {result:0.3f} radiaania.")
