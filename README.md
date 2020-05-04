Proyecto Final
==============================

### Contexto del problema

En una microfinanciera, los colaboradores de la fuerza de ventas realizan reuniones de seguimiento con sus clientes para asegurarse de que el monto total de la cuota del grupo sea cubierta. 

El principal problema que presentan los colaboradores es que las visitas no tienen ningún orden asignado, traduciéndose en un mayor costo tanto de distancias recorridas como económico para la empresa, en términos del bono operativo que se les asigna para los recorridos.

### Objetivo

Encontar la ruta de los colaboradores que minimice la distancia recorrida. En las reuniones de seguimiento, el colaborador debe visitar a todos sus clientes y solo los puede visitar una sola vez. Así, el problema es similar al que se tiene con el de $Travel salesman person$. 

### Algoritmos

Para resolver el problema antes planteado, se revisarán los siguientes algoritmos: 

+ Particle Swarm (PS)

+ Simulated Annealing (SA)


### Equipo de trabajo

El equipo está integrado por seis personas que fungirán diversos roles a lo largo del proyecto. El equipo a su vez se subdividió en dos: PS y SA. 

| Alumno | Equipo |
|--------|--------|
| Marco  | PS |
| Laura | PS |
| Diego | PS |
| Miguel | SA |
| Paola | SA |
| Ana   | SA |

El equipo PS revisará el código desarrollado por el equipo SA y viceversa. 

### Metodología de trabajo

El proyecto se desarrolla bajo una metodología ágil siguiendo el marco de trabajo de scrum. Las tareas e issues generadas durante el desarrollo del proyecto están organizadas en un [project board](https://github.com/lauragmz/proyecto-final-mno2020/projects/1)


### Organización del repositorio
El repositorio está organizado siguiendo la plantilla de [cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science/)

------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


--------

