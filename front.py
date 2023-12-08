import tkinter as tk
from tkinter import ttk
from exceldata import ExcelData

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import pyplot as plt

class Front(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.excInst = ExcelData()

        # Setup containers
        self.container = tk.Frame(self)
        self.right_container = tk.Frame(self)

        # Combo setup
        self.combo = ttk.Combobox(self.right_container, values=self.excInst.get_file_names(), state='readonly')
        self.combo.bind('<<ComboboxSelected>>', self.on_combo_change)
        self.combo.set(self.excInst.get_file_name())

        # Checkbox setup
        self.checkbox_checked = tk.IntVar()
        self.checkbox = ttk.Checkbutton(
            self.right_container,
            text="Draw lissajous?",
            command=self.on_checkbox,
            variable=self.checkbox_checked
        )

        # Graph setup
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.container)
        self.data = self.excInst.get_values(self.combo.get())
        self.plot, _ = self.ax.plot(self.data["time"], self.data["ch1_vals"], self.data["time"], self.data["ch2_vals"])

        # Cursors setup
        self.h_line_1 = self.ax.axhline(color='g', lw=2, ls='--')
        self.h_line_2 = self.ax.axhline(color='g', lw=2, ls='--')
        self.v_line_1 = self.ax.axvline(color='g', lw=2, ls='--')
        self.v_line_2 = self.ax.axvline(color='g', lw=2, ls='--')

        # Event listeners
        self.canvas.mpl_connect('motion_notify_event', self.on_mouse_move)
        self.canvas.mpl_connect('key_press_event', self.on_key_press)

        # Delta info setup
        self.h_delta_info = tk.Label(self.right_container, text="horizontal Δ=?")
        self.v_delta_info = tk.Label(self.right_container, text="vertical Δ=?")
        self.key_first_pressed = False
        self.key_second_pressed = False
        self.key_third_pressed = False
        self.key_fourth_pressed = False

        # pack everything up
        self.container.pack(side="left", fill="both", expand=True)
        self.right_container.pack(side="right")
        self.combo.pack(side="top", padx=10, pady=10)
        self.checkbox.pack(side="top")
        self.h_delta_info.pack(side="top")
        self.v_delta_info.pack(side="top")
        self.canvas.get_tk_widget().pack(side="left")

        self.draw_grid()

    def on_checkbox(self):
        if self.checkbox_checked.get():
            self.plot_lissajous()
        else:
            self.plot_graph()

    # draw grid since its often cleared
    def draw_grid(self, draw_at_zero=False):
        min_time, max_time = min(self.data["time"]), max(self.data["time"])
        self.ax.grid(True, which="both")
        self.ax.axhline(y=0, color='black', linestyle='--', linewidth=1)
        if draw_at_zero:
            self.ax.axvline(x=0, color='black', linestyle='--', linewidth=1)
        else:
            self.ax.axvline(x=int((abs(max_time)+abs(min_time)) / 2), color='black', linestyle='--', linewidth=1)
        self.canvas.draw()

    def draw_h_v_lines(self):
        self.h_line_1 = self.ax.axhline(color='g', lw=2, ls='--')
        self.h_line_2 = self.ax.axhline(color='g', lw=2, ls='--')
        self.v_line_1 = self.ax.axvline(color='g', lw=2, ls='--')
        self.v_line_2 = self.ax.axvline(color='g', lw=2, ls='--')
        self.canvas.draw()

    # Calculate delta
    def on_key_press(self, event):
        if event.key == "1":
            self.key_first_pressed = not self.key_first_pressed
        if event.key == "2":
            self.key_second_pressed = not self.key_second_pressed
        if event.key == "3":
            self.key_third_pressed = not self.key_third_pressed
        if event.key == "4":
            self.key_fourth_pressed = not self.key_fourth_pressed

        h_1 = self.h_line_1.get_ydata()[0]
        h_2 = self.h_line_2.get_ydata()[0]
        v_1 = self.v_line_1.get_xdata()[0]
        v_2 = self.v_line_2.get_xdata()[0]
        diffh = abs(h_1 - h_2)
        diffv = abs(v_1 - v_2)
        self.h_delta_info.config(text=f"ΔH={diffh}")
        self.v_delta_info.config(text=f"ΔV={diffv}")

    def on_mouse_move(self, event):
        x, y = event.xdata, event.ydata
        if self.key_first_pressed:
            self.h_line_1.set_ydata([y])
        if self.key_second_pressed:
            self.h_line_2.set_ydata([y])
        if self.key_third_pressed:
            self.v_line_1.set_xdata([x])
        if self.key_fourth_pressed:
            self.v_line_2.set_xdata([x])
        self.canvas.draw()

    def on_combo_change(self, event):
        filename = self.combo.get()
        checkbox_state = self.checkbox_checked.get()
        self.data = self.excInst.get_values(filename)
        if checkbox_state:
            self.plot_lissajous()
        else:
            self.plot_graph()

    def plot_lissajous(self):
        self.ax.clear()
        self.ax.scatter(self.data["ch1_vals"], self.data["ch2_vals"], s=.25)
        self.draw_grid(draw_at_zero=True)
        self.draw_h_v_lines()

    def plot_graph(self):
        self.ax.clear()
        self.ax.plot(self.data["time"], self.data["ch1_vals"])
        self.ax.plot(self.data["time"], self.data["ch2_vals"])
        self.draw_grid()
        self.draw_h_v_lines()


Front().mainloop()
