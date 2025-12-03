# Checking the specific cooling power based on energy balance
def check_efficiency(mass_kg, enthalpy, total_energy_j):
    latent_heat = mass_kg * enthalpy
    
    # Approx 8% of energy becomes heat (internal resistance)
    heat_gen = total_energy_j * 0.08
    
    # We saw about 78% efficiency with the Graphene+Al2O3 PCM
    heat_removed = heat_gen * 0.78 
    
    # Specific cooling power (W/kg)
    # Discharge time was 1800s for 2C
    scp = heat_removed / (mass_kg * 1800) 
    
    return heat_gen, scp

# Data from my 2C tests
gen, power = check_efficiency(0.060, 200000, 39420)
print(f"Heat Gen: {gen:.1f} J")
print(f"Cooling Power: {power:.1f} W/kg")