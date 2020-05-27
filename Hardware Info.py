import cpuinfo
from tkinter import *
from tkinter import ttk
import psutil
from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class Hardware:
    def cpu_load_start(self):
        plt.style.use("fivethirtyeight")
        time = []
        load_val = []
        time_sec = count()

        def cpu_load(i):
            time.append(next(time_sec))
            load_val.append(psutil.cpu_percent(interval=0))
            plt.cla()
            plt.plot(time, load_val, label="CPU Load in % over time (s)")
            plt.legend(loc="upper left")
            plt.tight_layout()

        monitor = FuncAnimation(plt.gcf(), cpu_load, interval=1000)
        plt.show()

    def __init__(self, root):
        root.title("Hardware info")
        root.iconbitmap("hardware_icon.ico")
        tab_parent = ttk.Notebook(root)
        general = ttk.Frame(tab_parent)
        cpu = ttk.Frame(tab_parent)
        gpu = ttk.Frame(tab_parent)
        tab_parent.add(general, text="General")
        tab_parent.add(cpu, text="CPU")
        tab_parent.add(gpu, text="GPU")
        tab_parent.pack(expand=1, fill="both")

        # CPU section
        self.cpu = cpuinfo.get_cpu_info()
        self.cpu_frame = ttk.Labelframe(cpu, width=100, height=100, text="Processor")
        ttk.Label(self.cpu_frame, text="Specification").grid(row=0, column=0, sticky="E", pady=2)
        ttk.Label(self.cpu_frame, text=self.cpu['brand'], relief="sunken").grid(row=0,
                                                                                column=1,
                                                                                sticky="W",
                                                                                pady=2)
        ttk.Label(self.cpu_frame, text="Advertised Frequency").grid(row=1, column=0, sticky="E", pady=2)
        ttk.Label(self.cpu_frame, text=self.cpu['hz_advertised'], relief="sunken").grid(row=1,
                                                                                        column=1,
                                                                                        sticky="W",
                                                                                        pady=2)
        ttk.Label(self.cpu_frame, text="Actual Frequency").grid(row=2, column=0, sticky="E", pady=2)
        ttk.Label(self.cpu_frame, text=self.cpu['hz_actual'], relief="sunken").grid(row=2,
                                                                                    column=1,
                                                                                    sticky="W",
                                                                                    pady=2)
        ttk.Label(self.cpu_frame, text="Core Count").grid(row=3, column=0, sticky="E", pady=2)
        ttk.Label(self.cpu_frame, text=f"{self.cpu['count']} Cores", relief="sunken").grid(row=3,
                                                                                           column=1,
                                                                                           sticky="W",
                                                                                           pady=2)
        ttk.Label(self.cpu_frame, text="Architecture").grid(row=4, column=0, sticky="E", pady=2)
        ttk.Label(self.cpu_frame, text=self.cpu['arch'], relief="sunken").grid(row=4,
                                                                               column=1,
                                                                               sticky="W",
                                                                               pady=2)
        ttk.Label(self.cpu_frame, text="Bit").grid(row=5, column=0, sticky="E", pady=2)
        ttk.Label(self.cpu_frame, text=f"{self.cpu['bits']} Bit", relief="sunken").grid(row=5,
                                                                                        column=1,
                                                                                        sticky="W",
                                                                                        pady=2)
        ttk.Label(self.cpu_frame, text="Family").grid(row=6, column=0, sticky="E", pady=2)
        ttk.Label(self.cpu_frame, text=self.cpu['family'], relief="sunken", width=5).grid(row=6,
                                                                                          column=1,
                                                                                          sticky="W",
                                                                                          pady=2)
        self.cpu_frame.grid(row=0, column=0)

        # CPU Cache section
        self.cpu_cache_frame = ttk.Labelframe(cpu, width=100, height=100, text="Cache")
        ttk.Label(self.cpu_cache_frame, text="L1 Cache").grid(row=0, column=0, sticky="E", pady=2)
        ttk.Label(self.cpu_cache_frame, text="Future Update", relief="sunken").grid(row=0,
                                                                                    column=1,
                                                                                    sticky="W",
                                                                                    pady=2)
        ttk.Label(self.cpu_cache_frame, text="L2 Cache").grid(row=1, column=0, sticky="E", pady=2)
        ttk.Label(self.cpu_cache_frame, text="Future Update", relief="sunken").grid(row=1,
                                                                                    column=1,
                                                                                    sticky="W",
                                                                                    pady=2)
        ttk.Label(self.cpu_cache_frame, text="L3 Cache").grid(row=2, column=0, sticky="E", pady=2)
        ttk.Label(self.cpu_cache_frame, text="Future Update", relief="sunken").grid(row=2,
                                                                                    column=1,
                                                                                    sticky="W",
                                                                                    pady=2)
        self.cpu_cache_frame.grid(row=1, column=0)
        self.cpu_temp_monitor = ttk.Button(cpu, text="CPU Load Monitor", command=lambda: self.cpu_load_start())
        self.cpu_temp_monitor.grid(row=2, column=0, sticky="W")


# Making the window object
window = Tk()
Hardware(window)
window.mainloop()
