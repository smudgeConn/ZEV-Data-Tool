import tkinter as tk
from tkinter import ttk
import sample_vehicle_objects as svo


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
    def __init__(self, container, label_text='File Selection', vehicle_list=['Lucid', 'Tesla'], test_list=['001', '002'], data_source_list=['Dyno', 'CAN'], sample_list=['N01', 'N02'], button_text='Load Data'):
        super().__init__(container)

        # variables
        self.label_text = label_text
        self.button_text = button_text
        self.vehicle_list = vehicle_list
        self.vehicle_var = tk.StringVar()
        self.test_list = test_list
        self.test_var = tk.StringVar()
        self.data_source_list = data_source_list
        self.data_source_var = tk.StringVar()
        self.sample_list = sample_list
        self.sample_var = tk.StringVar()

        # place the frame in the root window
        self.grid(row=0, rowspan=3, column=0, columnspan=2,
                  padx=5, pady=5, ipadx=5, ipady=5, sticky="nsew")

        # widgets
        ttk.Label(self, text=label_text).pack()

        # vehicle menu
        self.vehicle_menu = ttk.Combobox(
            self, textvariable=self.vehicle_var)
        self.vehicle_menu['values'] = self.vehicle_list
        self.vehicle_menu.pack()
        self.vehicle_menu.bind("<<ComboboxSelected>>", self.update_tests)
        self.vehicle_menu.set("Select a Vehicle")

        # test menu
        self.test_menu = ttk.Combobox(self, textvariable=self.test_var)
        self.test_menu['values'] = self.test_list
        self.test_menu.pack()
        self.test_menu.bind("<<ComboboxSelected>>", self.update_data_sources)
        self.test_menu.set("Select a Test")

        # data source menu
        self.data_source_menu = ttk.Combobox(
            self, textvariable=self.data_source_var)
        self.data_source_menu['values'] = self.data_source_list
        self.data_source_menu.pack()
        self.data_source_menu.bind(
            "<<ComboboxSelected>>", self.update_samples)
        self.data_source_menu.set("Select a Data Source")

        # sample menu
        self.sample_menu = ttk.Combobox(self, textvariable=self.sample_var)
        self.sample_menu['values'] = self.sample_list
        self.sample_menu.pack()
        self.sample_menu.set("Select a Sample")

        # load data button
        self.load_data_button = tk.Button(
            self, text=button_text, command=self.load_data).pack()

    def update_tests(self, selection):
        self.test_list = ['new test', 'new test2']

    def update_data_sources(self, selection):
        self.data_source_list = ['new data source', 'new data source2']

    def update_samples(self, selection):
        self.sample_list = ['new sample', 'new sample2']

    def load_data(self):
        pass


class SignalSelection(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        ttk.Label(self, text="Signal Selection").pack()
        self.grid(row=0, rowspan=3, column=2, columnspan=1,
                  padx=5, pady=5, ipadx=5, ipady=5, sticky="nsew")


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
