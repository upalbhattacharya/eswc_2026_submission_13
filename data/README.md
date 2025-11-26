# Data Directory

The relevant data (ontology files and datasets) for all concerned experiments
can be found here. The directory structure is given below:

```bash
├── ontology\_name
│   ├── OWL/RDF file : contains the ontology
│   ├── data : contains data for each n-shot experiment
│   │   ├── 0_shot
│   │   │   ├──dataset.json : polars.DataFrame with input data
│   │   ├── 1_shot
│   │   │   ├──dataset.json : polars.DataFrame with input data
│   │   │   └──exmples.json
│   │   ├── 2_shot
│   │   ├── 3_shot
│   │   ├── 4_shot
│   │   ├── 5_shot
│   │   ├── 6_shot
│   │   ├── 7_shot
│   │   ├── 8_shot
│   │   ├── 9_shot
│   │   └── 10_shot
│   └── embeddings
    ```bash 
