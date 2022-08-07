import argparse
from pickle import NONE
from termcolor import colored

arg_pr = argparse.ArgumentParser()

arg_pr.add_argument(
    "-m", "--model", nargs="+", required=True,
    choices=["GRU", "LSTM", "Transformer"],
    help="Add the model to use on the graphic plot."
)

arg_pr.add_argument(
    "-s", "--source", required=True,
    choices=["en", "cv"],
    help="Source languague of the model"
)

arg_pr.add_argument(
    "-t", "--target", required=True,
    choices=["en", "cv"],
    help="Target languague the model"
)

arg_pr.add_argument(
    "-sm", "--smoothing",
    type=float,
    default=NONE,
    help="Smoothing the graphics"
)

args = vars(arg_pr.parse_args())


if args["source"] == args["target"]:
    print(
        colored(
            "Error: Source languague and Target languague should not be the same.",
            "red", attrs=["bold"])
    )
    exit(1)

if args["smoothing"] < 0 or args["smoothing"] > 1:
    print(
        colored(
            "Error: Smoothing value must be between 0 and 1.",
            "red", attrs=["bold"])
    )
    exit(1)


from src.plot_config import Plot_Metrics_Graphs as plt_MG


valid_metrics_name = [
    "Training Loss", "Validation Loss", "Training Accuracy", "Validation Accuracy",
    "BLUE Score", "METEOR Score", "TER Score"
]


def validate_metrics(metrics_name: str) -> list:
    metrics_name = metrics_name.split(", ")

    for metric in metrics_name:
        if metric not in valid_metrics_name:
            return None
    
    return metrics_name


print("\nEnter the metrics name separate by ',' (comma):")
print(colored(f"Valid list: {valid_metrics_name}\n", "blue", attrs=["bold"]))
print(colored("Ex: ", attrs=["bold"]))
print(colored("  Metrics name: Training Loss, Validation Loss", attrs=["bold"]))

metrics_name = str(input(colored("\nMetrics name: ", "magenta", attrs=["bold"])))
metrics_name = validate_metrics(metrics_name)

if not metrics_name:
    print(
        colored(
            "Error: Matrics name not compatible.",
            "red", attrs=["bold"])
    )
    exit(1)


header_name = str(input(colored("\nPlot header name: ", "magenta", attrs=["bold"])))
y_label = str(input(colored("\ny_label name: ", "magenta", attrs=["bold"])))
x_label = str(input(colored("\nx_label name: ", "magenta", attrs=["bold"])))


if __name__ == "__main__":
    plt_MG.plot_metrics(
        models = args["model"], 
        metrics_name = metrics_name, 
        source = args["source"], 
        target = args["target"], 
        plot_header=header_name, 
        y_label=y_label,
        x_label=x_label,
        smoothing=args["smoothing"]
    )
