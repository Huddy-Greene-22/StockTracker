from typing import Dict, List
import matplotlib.pyplot as plt


class StockDisplayer:

    def display_days(self, ticker, data_dict: Dict[str, Dict]):
        names = list(data_dict.keys())
        values = list(data_dict.values())

        figure, axes = plt.subplots()

        axes.plot(names, values, label=ticker)
        axes.set(title="Stock")
        axes.tick_params(axis="x", labelrotation=90)
        axes.legend()

        plt.show()
