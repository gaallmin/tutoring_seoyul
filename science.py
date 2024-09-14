# 2.시스템과 상호작용 -지구시스템과 에너지 및 물질 순환
# 4. 호간경과 에너지 - 에너지 전환과 효율적 이용

'''
에너지 수송을 효율적으로 설계
<특징>
1. 다양한 에너지 자원 선택 (user)
2. 에너지 변환 시뮬레이션 (에너지 -> 전기)
3. 효율성 계산, 환경적 영향 계산
'''


import tkinter as tk
from tkinter import ttk

class EnergySimulatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Energy Conversion Simulator")

        # 옵션선택 (드롭다운_)
        self.label = tk.Label(root, text="Select Energy Source:")
        self.label.pack(pady=10)
        
        self.energy_source = tk.StringVar()
        self.energy_source_dropdown = ttk.Combobox(root, textvariable=self.energy_source)
        self.energy_source_dropdown['values'] = ["Solar", "Wind", "Thermal"] # thermal : 지열 
        self.energy_source_dropdown.current(0)
        self.energy_source_dropdown.pack(pady=10)

        # 에너지 input 입력
        self.input_label = tk.Label(root, text="Enter Energy Input (Joules):")
        self.input_label.pack(pady=5)
        self.energy_input = tk.Entry(root)
        self.energy_input.pack(pady=5)

        # 에너지 output 입력
        self.output_label = tk.Label(root, text="Enter Energy Output (Joules):")
        self.output_label.pack(pady=5)
        self.energy_output = tk.Entry(root)
        self.energy_output.pack(pady=5)

        # 계산 버튼
        self.calculate_button = tk.Button(root, text="Calculate Efficiency", command=self.calculate_efficiency)
        self.calculate_button.pack(pady=10)

        # 결과 버튼
        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)
        
    def calculate_efficiency(self):
        try:
            energy_input = float(self.energy_input.get())
            energy_output = float(self.energy_output.get())
            
            print(f"Energy Input: {energy_input}, Energy Output: {energy_output}")  # Debug print statement
            
            if energy_input <= 0:
                raise ValueError("Energy input must be positive.")
            
            # 효율성 계산
            efficiency = (energy_output / energy_input) * 100
            self.result_label.config(text=f"Efficiency: {efficiency:.2f}%")
        
        except ValueError as e:
            self.result_label.config(text=f"Error: {str(e)}")

            

if __name__ == "__main__":
    root = tk.Tk()
    app = EnergySimulatorApp(root)
    root.geometry("400x300")
    root.mainloop()
