# This is an example of how you would use this library
1. Create a custom dataset object by inheriting from `torch.utils.data.Dataset`.
1. Specify if you want to perform K-Fold Cross Validation. (!!!IN PROGRESS!!!)
1. Specify if you want to reproduce the experiment. (!!!IN PROGRESS!!!)
1. You must create an experiment file in YAML specifying the format of the experiment

    For the experiment file, you must specify the following:
    1. The name of the experiment
    1. For the data loading part, you must mention:
        1. The batch size - if you have limited memory go with a smaller size
        1. The number of workers - if you can't parallelize well, leave it blank
        1. The shuffle parameter - should be True, if you haven't shuffled the dataset
    1. For the training part, you must mention:
        1. Learning Rate
        1. Number of Epochs
        1. The loss function to be used:
            * MSE -> "mse"
            * Cross Entropy -> "ce"
            * Binary Cross Entropy -> "bce"
        1. The optimizer to be used:
            * SGD -> "sgd"
            * Adam -> "adam"
            * RMSProp -> "rmsprop"
            * Adagrad -> "adagrad"

1. Create the ML model in the models folder - add it to the `models_list.py`. Mention the name in the experiment file, it is imperative that the name of the class and the name in the YAML file are exactly the same, or else the class constructor won't be found.
1. Make a trainer object
1. Train the model
1. Test the model