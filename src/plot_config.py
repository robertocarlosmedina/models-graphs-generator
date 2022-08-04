import json
import matplotlib.pyplot as plt


colors = ["#3EC70B", "#FF0000", "#3B44F6", "#FF5B00", "#0E185F", "#243D25"]

class Plot_Metrics_Graphs:

    @staticmethod
    def get_data(model: str, graphs_name: list) -> list:
        """
            Method to get the data in one model.
        """
        # opening all the json files
        json_files = [open(f'./{model.lower()}/{graph}.json') for graph in graphs_name]

        # load all the data
        data = [json.load(file) for file in json_files]

        # close all the files
        [file.close for file in json_files]

        return data
    
    @staticmethod
    def get_all_data(models: list, graphs_name: list) -> list:
        """
            Method to get all the data inside more then one models.
        """
        for model in models:
            data = Plot_Metrics_Graphs.get_data(model, graphs_name)
            print("\n\n")
            print(data)
            print("\n\n")            
        
        print()
        return [Plot_Metrics_Graphs.get_data(model, graphs_name) for model in models]
    
    @staticmethod
    def make_matrics_single_model(graphs_name: list, all_data: list) -> dict:
        """
            Method to make a single metrics dict of a model.
        """
        metrics = {}

        for graph, data in zip(graphs_name, all_data):
            metrics[graph] = [[dt[1] for dt in data], [dt[2] for dt in data]]
        
        return metrics
    
    @staticmethod
    def make_matrics_multi_models(
                model: str, simplify_graphs_name: list, all_data: list) -> dict:
        """
            Method to make a multiple metrics dict of different models.
        """
        metrics = {}

        for graph, data in zip(simplify_graphs_name, all_data):
            metrics[model+": "+graph] = [[dt[1] for dt in data], [dt[2] for dt in data]]
        
        return metrics
    
    @staticmethod
    def make_metrics(models: list, graphs_name: list) -> dict:
        """
            Method to make the metrics dict.
        """
        all_metrics = {}

        if len(models) > 1:
            metrics = {}
            for model in models:
                all_data = Plot_Metrics_Graphs.get_data(model, graphs_name)
                metrics = Plot_Metrics_Graphs.make_matrics_multi_models(
                                model, graphs_name, all_data)
                all_metrics.update(metrics)
        
        else:
            all_data = Plot_Metrics_Graphs.get_data(models[0], graphs_name)
            metrics = Plot_Metrics_Graphs.make_matrics_single_model(graphs_name, all_data)
            all_metrics.update(metrics)
        
        return all_metrics

    @staticmethod
    def plot_metrics(models: list, metrics_name: list,  source: str, \
            target: str, plot_header: str, y_label: str, x_label="Epochs") -> None:
        """
            Method to calculate and plot different models validation accuracy.
        """
        print(models)
        direction = f"{source}-{target}"
        graphs_name = [f"{name} ({direction})" for name in metrics_name]

        all_metrics = Plot_Metrics_Graphs.make_metrics(models, graphs_name)

        for metric, color in zip(all_metrics.items(), colors[0:len(all_metrics.items())]):
            plt.plot(metric[1][0], metric[1][1], color=color, label=metric[0])
        
        plt.legend()
        plt.title(f"{plot_header} ({direction})", pad=18,
            fontname="Times New Roman", fontweight="bold", fontsize=12,
        )
        plt.xlabel(x_label, fontname="Times New Roman", fontweight='bold')
        plt.ylabel(y_label, fontname="Times New Roman", fontweight='bold')
        plt.grid(axis = "y", linewidth = 0.4)
        plt.grid(axis = "x", linewidth = 0.2)
        plt.show()      
