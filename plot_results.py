import matplotlib.pyplot as plt
import numpy as np

# Recreating the 3C discharge comparison plot
def plot_3c_results():
    t = np.linspace(0, 1200, 100) # 3C takes ~1200s
    start_temp = 34.5 
    
    # Peak temps from my experiments (at 1200s)
    results = {
        'Pure PCM': 49.13,
        'Graphene(3%)+ZnO(2%)': 47.74,
        'Al2O3(1%)+ZnO(2%)': 45.96,
        'Al2O3(0.5%)+ZnO(2%)': 44.25,
        'Al2O3(0.75%)+ZnO(2%)': 43.41,
        'Graphene(3%)+Al2O3(1%)': 42.13 # Best result
    }
    
    plt.figure(figsize=(10, 6))
    
    for name, peak in results.items():
        # Simple curve fit to show the trend
        # T = T_start + (T_peak - T_start) * curve_factor
        curve = t**1.2 / 1200**1.2
        temps = start_temp + (peak - start_temp) * curve
        
        # Make the best one stand out
        lw = 3 if 'Al2O3(1%)' in name and 'Graphene' in name else 1.5
        ls = '-' if lw == 3 else '--'
        
        plt.plot(t, temps, label=f"{name} (Max: {peak}°C)", linewidth=lw, linestyle=ls)

    plt.axhline(y=50, color='red', linestyle=':', label='Safety Limit')
    
    plt.title('PCM Performance at 3C Discharge')
    plt.xlabel('Time (s)')
    plt.ylabel('Temp (°C)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()

if __name__ == "__main__":
    plot_3c_results()