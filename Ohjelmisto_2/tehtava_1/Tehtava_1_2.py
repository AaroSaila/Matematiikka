import numpy

a = 1.6  # m
b = 2.3  # m
c = numpy.hypot(a, b)  # m

print(f"""
Hypotenuusan pituus on noin {c:.1f} m, kun kateetit ovat:
a = {a} m
b = {b} m
""")
