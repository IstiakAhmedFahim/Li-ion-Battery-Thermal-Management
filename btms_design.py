# Quick script to check C-rates and ring geometry
import math

class BTMS_Calc:
    def __init__(self):
        # 18650 cell specs
        self.cap = 3.0 # Ah
        self.dia = 18.33 # mm

    def get_discharge_info(self, c_rate):
        current = self.cap * c_rate
        # Time = Capacity / Current
        time_sec = (self.cap / current) * 3600
        return current, time_sec

    def get_ring_gap(self, d_star=0.2):
        # Optimization from thesis: d* = 0.2 is best
        return d_star * self.dia

calc = BTMS_Calc()

print("--- Discharge Specs ---")
for rate in [1, 2, 3]:
    i, t = calc.get_discharge_info(rate)
    print(f"{rate}C: {i:.1f}A for {t:.0f}s")

print("\n--- Geometry ---")
# Calculating gap for the PCM container
gap = calc.get_ring_gap()
print(f"Optimum PCM gap: {gap:.2f} mm")