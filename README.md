# Models Graphs Generator (MGG)
### _Training metrics graph generator (Accuracy, Loss) according to the provided model (which can be GRU, LSTM or Transformer)_

Given a model name and the desired metric, this generator will generate a graph according to the data generated in the training process of that model. It's worth noting that you can generate graphics for more than one model.

> This project was made with the intention of being an integral part of my final final project.
> All aspects addressed in the implementation were made according to the needs of the project as a whole.
> Cape Verdean Creole is the mother language of Cape Verde, which is not an official language and is not well represented and known around the world. Therefore, it is a great honor to carry out studies and projects that contribute to its recognition and dissemination.

### Dependencies installation

Run the following command to install all the dependencies:

```sh
pip install -r requirements.txt
```

### Features / Execution

To generate the graph you need to pass the correct parameters during the execution of the main Python file, for example:

- Example 1:
    It is intended to generate a graph from an LSTM model with origin in English and destination in Cape Verdean Creole
    ```sh
    python main.py -m LSTM -s en -t cv
    ```
- Example 2:
    It is intended to generate a graph from the Transformer and GRU models with origin in Cape Verdean Creole and destination in English
    ```sh
    python main.py -m Transformer GRU -s cv -t en
    ```
- Example 1:
    It is intended to generate a graph from the GRU, LSTM and the Transformer models with origin in English and destination in Cape Verdean Creole
    ```sh
    python main.py -m GRU LSTM Transformer -s en -t cv
    ```
**Notes** that the parameters have the following meanings:
- **'-m'** or **'--model'** are the models, or the model, that you want to make the graph;
- **'-s'** or **'--source'** is the source language;
- **'-t'** or **'--target'** is the target language.


### All parts of the project into a whole
The whole project is divided into parts and each part has an essential function in it.
They are distributed as shown in the subtopics below.


#### Models implementation
This are the model used in the whole project:

- [Transformer model implementation]
- [GRU model implementation]
- [LSTM model implementation]
- [Models Training Graphs Generator]


#### Frontend test platform
This is a React App made to test all the translations made by the models, similar to the App [Google Translator]. 
Projects related to using the frontend application can be found at:

- [MT Models API implementation]
- [Cape Verdean Creole Translator Frontend test App]


#### Dataset
The dataset used to train, validate and test the model was the [CrioleSet dataset].
If the dataset is not in the project while executing any of the action commands, it will be downloaded and added to the project.

- [CrioleSet dataset]

### License

MIT


**Feel free to use and get in touch with any questions.**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [Transformer model implementation]: <https://github.com/robertocarlosmedina/attention-transformer-translator>
   [GRU model implementation]: <https://github.com/robertocarlosmedina/rnn-gru-attention-translator>
   [LSTM model implementation]: <https://github.com/robertocarlosmedina/rnn-lstm-translator>
   [MT Models API implementation]: <https://github.com/robertocarlosmedina/machine-translation-models-api>
   [CrioleSet dataset]: <https://github.com/robertocarlosmedina/crioleSet>
   [Cape Verdean Creole Translator Frontend test App]: <https://github.com/robertocarlosmedina/cv-creole-translator>
   [Models Training Graphs Generator]: <https://github.com/robertocarlosmedina/models-graphs-generator>
   [Google Translator]: <https://translate.google.com>
