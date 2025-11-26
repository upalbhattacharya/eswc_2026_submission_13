# Run Arguments

The various parameters used for experimenting with different
LLMs, domain contexts, n-shot prompting approaches and
temperature settings can be found in `json` files here. The 
provided directory structure below explains how the data is categorized.

```
.
├── embeddings : Parameters for generating OpenAI embeddings
│   ├── Ontology Name
│   │   ├── concepts_no_processing.json : Parameters for generating embeddings for concepts of ontology
│   │   └── individuals_no_processing.json : Parameters for generating embeddings for individuals of ontology
└── onto_pop : Parameters for Ontology Population Experiments
    ├── 0_shot
    │   ├── deepseekr1-distill-llama3-8B
    │   │   ├── astronomy-ontology
    │   │   │   ├── 2e2ddb82-9f11-4fab-9ba1-27798805d357.json
    │   │   │   ├── 6a1b73e3-f852-4d0c-b4e7-eb7041085603.json
    │   │   │   ├── 95e3f7ea-6c5f-486c-b222-b51024dd5110.json
    │   │   │   └── d7a9319b-db24-4add-afdd-c99463a320cc.json
    │   │   ├── case-uco-owl-trafficking
    │   │   │   ├── 1520db7d-bf26-4e9a-9b85-09677db2fee6.json
    │   │   │   ├── 1b8ca5f2-185e-4dc0-b071-ee0fec83f888.json
    │   │   │   ├── 7fd5b64c-80fd-43de-a208-71406958378b.json
    │   │   │   └── f17c4add-6dee-43d9-afdc-b74ff9c10a3e.json
    │   │   └── wines-ontology
    │   │       ├── 488936b8-0f78-4c91-8284-47063b5d8221.json
    │   │       ├── 4ed0757d-31df-4c98-877e-7ef33b9bd75b.json
    │   │       ├── a18775ea-3895-4b32-aa7b-68a72766a335.json
    │   │       └── e30f3fa8-9301-418e-b152-0113a761d13a.json
```
