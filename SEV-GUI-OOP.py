import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title("ZEV Data Tool")
        self.geometry("1200x800")
        self.configure(background="grey")

        # configure the grid of the root window
        self.columnconfigure((0, 1, 2, 3, 4, 5), weight=1, uniform='a')
        self.rowconfigure((0, 1, 2, 3), weight=1, uniform='a')

        # frames
        self.file_selection = FileSelection(self)
        self.signal_selection = SignalSelection(self)
        self.graph_display = GraphDisplay(self)
        self.filter_selection = FilterSelection(self)
        self.group_selection = SignalGroupSelection(self)
        self.log_display = LogDisplay(self)


class FileSelection(ttk.Frame):
    def __init__(self, container, label_text='File Selection', vehicle_list=['Lucid Air', 'EV Hummer', 'F150 Lightning'], test_list=['001', '002', '003'], source_list=['Dyno', 'CAN'], sample_list=['N01', 'N02', 'N03', 'N04'], button_text='Load Data'):
        super().__init__(container)
        self.selected_vehicle = tk.StringVar()
        self.selected_test = tk.StringVar()

        self.grid(row=0, rowspan=3, column=0, columnspan=2,
                  padx=5, pady=5, ipadx=5, ipady=5, sticky="nsew")

        # widgets
        ttk.Label(self, text=label_text).pack()

        #  Vehicle OptionMenu -- IN: list of strings; OUT: vehicle name as string
        self.selected_vehicle.set(vehicle_list[0])
        self.vehicle_option_menu = ttk.OptionMenu(
            self, self.selected_vehicle, *vehicle_list)
        self.vehicle_option_menu.pack()

        #  Test OptionMenu -- IN: list of strings; OUT: test name as string
        self.test_option_menu = ttk.OptionMenu(
            self, self.selected_test, *test_list)

        ttk.Button(self, text=button_text).pack()


class SignalSelection(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        ttk.Label(self, text="Signal Selection").pack()
        self.grid(row=0, rowspan=3, column=2, columnspan=1,
                  padx=5, pady=5, ipadx=5, ipady=5, sticky="nsew")

    def create_widgets(self):
        pass


class GraphDisplay(ttk.Frame):
    def __init__(self, container, text="Graph Display"):
        super().__init__(container)
        ttk.Label(self, text="Graph Display").pack()
        self.grid(row=0, rowspan=3, column=3, columnspan=3,
                  padx=5, pady=5, ipadx=5, ipady=5, sticky="nsew")

    def create_widgets(self):
        pass


class FilterSelection(ttk.Frame):
    def __init__(self, container, text="Filter Selection"):
        super().__init__(container)
        ttk.Label(self, text="Filter Selection").pack()
        self.grid(row=3, rowspan=1, column=0, columnspan=2,
                  padx=5, pady=5, ipadx=5, ipady=5, sticky="nsew")

    def create_widgets(self):
        pass


class SignalGroupSelection(ttk.Frame):
    def __init__(self, container, text="Signal Group Selection"):
        super().__init__(container)
        ttk.Label(self, text="Signal Group Selection").pack()
        self.grid(row=3, rowspan=1, column=2, columnspan=2,
                  padx=5, pady=5, ipadx=5, ipady=5, sticky="nsew")

    def create_widgets(self):
        pass


class LogDisplay(ttk.Frame):
    def __init__(self, container, text="Log Display"):
        super().__init__(container)
        ttk.Label(self, text="Log Display").pack()
        self.grid(row=3, rowspan=1, column=4, columnspan=2,
                  padx=5, pady=5, ipadx=5, ipady=5, sticky="nsew")

    def create_widgets(self):
        pass


if __name__ == "__main__":
    app = App()
    app.mainloop()
