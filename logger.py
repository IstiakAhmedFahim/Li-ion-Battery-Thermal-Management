import serial
import time
import csv
from datetime import datetime

# Port setup
PORT = 'COM3' 
BAUD = 9600
FILE = f"test_data_{datetime.now().strftime('%H%M')}.csv"

def run_logger():
    try:
        ser = serial.Serial(PORT, BAUD, timeout=1)
        print("Connected to Arduino...")
        
        with open(FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Time","V","I","T_Top","T_Mid","T_Bot"])
            
            start = time.time()
            
            while True:
                if ser.in_waiting:
                    line = ser.readline().decode('utf-8').strip()
                    data = line.split(',')
                    
                    if len(data) >= 5:
                        now = round(time.time() - start, 1)
                        volts = float(data[0])
                        
                        # Stop if voltage drops too low or time runs out
                        if now > 4000 or volts <= 3.0:
                            print("Test finished.")
                            break
                        
                        row = [now] + data
                        writer.writerow(row)
                        print(f"Saved: {row}")
                        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if 'ser' in locals() and ser.is_open:
            ser.close()

# run_logger()