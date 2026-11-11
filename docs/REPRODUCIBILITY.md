# Reproduction guide and limitations

## Required external artifacts

1. ACT-2 paired scatter/target training images (`train{i}x` / `train{i}y`) and group split metadata.
2. Turbine normalization JSON and the historical consolidated ACT-2 SCADA CSV.
3. Per-fold/per-seed checkpoints and `Unet_ACT2_deploy_best.pth`.
4. ACT-2 2026 and ACT-1 deployment SCADA exports with the schemas expected by each notebook.
5. For the external comparison, the upstream `UnetS4000DEAndADEepoch3.pth` checkpoint and sample CSV, obtained under upstream terms.

Paths currently point to the author's Kaggle datasets. Those paths identify dependencies; they do not establish public access. Update the configuration cells for your environment. Do not commit confidential SCADA records or credentials.

## Execution

- Run the training notebook for the ACT-2 development workflow after supplying image pairs and metadata.
- Run the ACT-2 inference notebook with saved checkpoints and its required 2026 inputs.
- Run the ACT-1 notebook with the unchanged ACT-2 deployment checkpoint and ACT-1 inputs.
- Run the baseline-comparison notebook after providing both checkpoints and the external sample data.

Each notebook has its own ordered cells and shared in-memory variables. They are research workflows rather than an installable Python package.

## Interpretation and audit points

- The inference notebook reconstructs CV summaries from a hard-coded `run_specs` list; these summaries are historical values, not fresh training results.
- Some notebook commentary and exploratory scenario definitions may precede the final manuscript. In particular, inspect any TP-informed input cleaning separately from the manuscript's GP-only deployment claims. Do not assume every saved experimental cell is the final paper protocol.
- Dataset-derived normalization and input-axis calibration must be distinguished from updates to model weights.
- Pixel reconstruction proxy accuracy is not capability-curve accuracy. Keep image metrics, normalized curve metrics, kW errors, and conditional regression results distinct.
- Checkpoint comparisons retain native curve readers and must report paired successful cases and reader failures.
- Historical fixed-axis component audits do not replace primary deployment results.

No end-to-end execution, numerical verification, or dependency-version lock was possible from the supplied artifacts alone. Add the original environment export, dataset hashes, split metadata, checkpoint hashes, and raw metric exports for a fully auditable release.

## Supplied run records

The new asset archive includes environment and run manifests under `results/`, and derived CSV/LaTeX exports under `tables/`. These records describe specific saved runs and have not been validated as one common environment. They do not include raw SCADA inputs or trained weights. See `RESULTS_NOTES.md` for protocol and result differences.
