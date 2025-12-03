# Lithium-Ion Battery Thermal Management Thesis

This repository contains my Bachelor's thesis from Rajshahi University of Engineering & Technology (RUET), submitted in October 2023. The project focuses on thermal management of lithium-ion batteries using fin-enhanced composite phase change materials (PCMs).

## Abstract
 The escalating demand for lithium-ion batteries in applications such as electric vehicles and renewable energy systems has highlighted the critical need for effective thermal management strategies to improve safety and performance. This thesis comprehensively explores the use of fin-enhanced phase change materials (PCMs) for thermal regulation of lithium-ion batteries, focusing on temperature control and heat dissipation. Experimental investigations evaluate the practical viability of this approach, including PCM fabrication, module integration, and thermal performance testing via cycling at 1C-3C rates. Various fin configurations—rectangular, cylindrical, and disc-shaped—are integrated with 18650 lithium-ion batteries in a container module. Six PCM compositions are evaluated to enhance thermal conductivity and battery thermal management system (BTMS) suitability: pure PCM and hybrid nano-PCMs incorporating Al₂O₃, ZnO, and graphene at optimized loadings (0.5-3%). Systematic comparisons reveal that graphene(3%) + Al₂O₃ (1%) offers the most promising performance, achieving a 5.3× thermal conductivityenhancement (to 1.16 W/m·K) and reducing peak temperatures to 42.13°C at 3C discharge—a24.87°C (37%) decrease from the 67°C unmanaged baseline and 7.00°C better than pure PCM—providing a 7.87°C safety margin below the 50°C threshold. Overall, incorporating fins and PCM significantly slows battery temperature rise, limits axial gradients to <2°C across upper, middle, and lower sections, and extends battery lifespan.

## Files
- **Thesis_Thermal_Management_LiIon_Batteries.pdf**: Full thesis document (73 pages).
- **data_acquisition.ino**: Arduino code for logging temperature and current data from the experimental setup.
- **btms_design_calculator.py**: Python script for calculating discharge parameters and geometric optimizations.
- **results_visualizer.py**: Python script to plot PCM comparisons from thesis results.
- **data_logger.py**: Python script to log data from Arduino via serial.
- **thermal_model.py**: Python script for energy balance calculations.

## How to Use
- Run the Python scripts with libraries like numpy, matplotlib, and serial (install via pip if needed).
- For Arduino, open in Arduino IDE and upload to your board.

Feel free to contact me for questions!
