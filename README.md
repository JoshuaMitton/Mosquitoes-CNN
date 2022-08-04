# Mosquito Age and Species Classification

This is a collection of Keras models for  classification of mosquito age and species classification as described in our paper:

https://www.nature.com/articles/s41467-022-28980-8

## Installation

```
conda create --name mosquitoes python=3.6.13
conda activate mosquitoes
python setup.py install
````

## Data

The dataset used in this project can be dowloaded from https://www.nature.com/articles/s41467-022-28980-8.

Download the dataset into the mosquitoes/Data folder and unzip:

```
unzip .zip
```

Then process the data with the scripts provdided in mosquitoes/Data/MIMI-project. First run

```
OPUS dei 2.3.ipynb
```

then
```
Loco mosquito 5.0.ipynb
```


## Run the examples

We provide notebooks to train different models for different datasets. To train the CNN model look at the scripts in mosquitoes/Models/CNN/CNN.

To train on LV data

```
MIMI-Paper-CNN-Lab-Only.ipynb
```

To train on LV+GV data

```
MIMI-Paper-CNN-TCField.ipynb
```

To train on EV data

```
MIMI-Paper-CNN-TCValie.ipynb
```

To train on Wild data

```
MIMI-Paper-CNN-Wild-retrain-v2
```

There is also the equivalent notebooks for the MLP model in the folder mosquitoes/Models/MLP.

Further, to perform the sensitivity analysis use the notebook in mosquitoes/Models/Sensitivity_Analysis

```
MIMI-Sensitivity.ipynb
```

Finally, we initially used UMAP for some early data visualisations. The notebook for this is in mosquitoes/Models/UMAP

```
UMAP_MIMI_data_w_dates.ipynb
```


## Cite

Please cite our paper if you make use of our work:

```
@article{siria2022rapid,
  title={Rapid age-grading and species identification of natural mosquitoes for malaria surveillance},
  author={Siria, Doreen J and Sanou, Roger and Mitton, Joshua and Mwanga, Emmanuel P and Niang, Abdoulaye and Sare, Issiaka and Johnson, Paul CD and Foster, Geraldine M and Belem, Adrien MG and Wynne, Klaas and others},
  journal={Nature communications},
  volume={13},
  number={1},
  pages={1--9},
  year={2022},
  publisher={Nature Publishing Group}
}
```


