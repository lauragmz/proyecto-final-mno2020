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
```
├── deploy                                                         <- archivos para el tablero
├── docker                                                         <- construcción de imagen
├── Minutas
│   ├── 20042020_Sesion0.txt
│   ├── 24042020_Sesion1.txt
│   └── TSP-plan_trabajo.xlsx
├── notebooks
│   ├── entrega
│   │   ├── Analisis_ParticleSwarm_10nodos.ipynb
│   │   ├── Analisis_ParticleSwarm_6nodos.ipynb
│   │   ├── Analisis_ParticleSwarm_Paralelo.ipynb
│   │   ├── Analisis_Simulated_Annealing _10nodos-100_iter.ipynb
│   │   ├── Analisis_Simulated_Annealing _6nodos-100_iter.ipynb
│   │   └── settings.toml
│   └── SA-one process-con-clases.ipynb
├── README.md
├── references
│   └── README.md
├── reports
│   ├── figures
│   └── MNO_ExamenFinal.pdf
├── setup.py
└── src
    ├── Control.py
    ├── data
    │   ├── __init__.py
    │   ├── load_data.py
    │   ├── make_dataset.py
    │   └── transformaciones.py
    ├── __init__.py
    ├── models
    │   ├── CA_utils.py
    │   ├── __init__.py
    │   ├── particle_swarm.py
    │   ├── simulated_annealing.py
    │   └── TSP.py
    ├── Pipeline.ipynb
    ├── Pipeline.py
    ├── settings.toml
    ├── sql
    │   ├── clean_tables.sql
    │   ├── create_db.sql
    │   ├── create_schemas.sql
    │   ├── create_tables.sql
    │   └── create_views.sql
    └── Utileria.py
 ```
--------

