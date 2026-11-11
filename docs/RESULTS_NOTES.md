# Result provenance and consistency

The submitted manuscript and the supplied experiment archive are distinct records. Packaging has not rerun, reconciled, or altered their numerical values. The archive may contain development runs, alternate preprocessing/readout configurations, partial months, and multiple scoring protocols.

| Record | ACT-2/2026 S1 normalized RMSE | ACT-1/2025 S1 normalized RMSE |
| --- | ---: | ---: |
| Manuscript Table 2, Panel A | 0.02864 | 0.05440 |
| Supplied full-month/scenario summaries | 0.02939 | 0.04694 |

The second row comes from `tables/02-act2-2026-testing/scenario-results/ours_full_months_2026.csv` and `tables/03-act1-zero-shot/act-1-scenario-results/ours_by_scenario_act1_2025.csv`. These are not interchangeable with the manuscript table. Neither record has been replaced by the other.

The training run manifest describes a pixel-map/polynomial reader, whereas supplied inference code includes a monotone spline reader. Environment files describe particular saved runs, not one verified environment for every notebook.

Before claiming exact paper reproduction, identify the checkpoint, split, normalization, curve reader, month inclusion rule, and metric CSV that produced each final manuscript figure/table. Original assets are retained so that this mapping can be audited. Files with similar or duplicate names remain available with their original-source mapping.
