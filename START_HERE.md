# Upload your prepared repository to GitHub (Windows)

Everything is already organized. Do not upload the ZIP itself. Extract it, then upload the contents of the `wind-turbine-power-curve-unet` folder.

## Recommended: GitHub Desktop (no commands)

1. Download and extract the prepared ZIP using Windows **Extract All**.
2. Install GitHub Desktop from https://desktop.github.com/ and sign in as **Electromind18**.
3. In GitHub Desktop choose **File → New repository**.
4. Name: `wind-turbine-power-curve-unet`.
5. Description: `Site-adapted U-Net for wind turbine power curve modeling: research code, figures, and benchmark results accompanying a manuscript submitted to Scientific Reports.`
6. Choose a convenient Local path, for example Documents/GitHub. Leave initialization options unchecked and License as None. Click **Create repository**.
7. Choose **Repository → Show in Explorer** to open the newly created folder.
8. Open the extracted prepared folder in another Explorer window. Copy ALL its contents into the new repository folder. Copy `README.md`, `requirements.txt`, `notebooks`, `figures`, `tables`, `results`, `docs`, `scripts`, `.github`, and `.gitignore`. Do not put the entire outer folder inside the new repository folder. Enable **View → Show → Hidden items** if needed.
9. Return to GitHub Desktop. The files appear under Changes. Enter commit summary: `Add research code, figures, tables, and documentation`. Click **Commit to main**.
10. Click **Publish repository**. Confirm owner **Electromind18**. For a public portfolio repository, uncheck **Keep this code private**; leave it checked if you want a private draft. Click **Publish repository**.
11. Choose **Repository → View on GitHub**. Check that README renders and `notebooks/`, `figures/`, `tables/`, and `results/` appear at the top level.
12. On GitHub click the gear beside **About**. Paste the description above. Suggested topics: `wind-energy`, `power-curve`, `scada`, `unet`, `pytorch`, `renewable-energy`, `machine-learning`, `reproducible-research`.

This method uploads all files together without selecting hundreds of figures manually. No access token needs to be pasted into chat.

## Alternative: upload through the GitHub website

1. Sign in at https://github.com/new as Electromind18.
2. Enter the same repository name and description. Choose Public or Private. Leave README, .gitignore, and license initialization off, then click **Create repository**.
3. Click **uploading an existing file** on the empty-repository page.
4. Drag `README.md`, `requirements.txt`, `START_HERE.md`, and the small folders from the extracted package onto the upload area. Commit changes.
5. Use **Add file → Upload files** for additional folders. Upload figure experiment folders one at a time; the training figure group has 76 images, so keep it separate from the other figure groups. If GitHub asks for fewer files, split the selection further while preserving the destination folder. Each supplied file is below 25 MiB.
6. Check that the folders and README appear at the repository root. Upload `.github` and `.gitignore` too; GitHub Desktop is easier for these items.

Do not upload confidential SCADA source data. The package contains supplied figures and derived result exports, not the raw SCADA dataset or model weights.

## Adding more figures later

Place images in the matching experiment folder under `figures/`, and CSV/LaTeX tables under the corresponding folder in `tables/`. In GitHub Desktop, commit the changes and click **Push origin**. Keep main-paper and supplementary numbering only when the final manuscript mapping is confirmed.

## Publication status

The README says **submitted to Scientific Reports**. Update this only if the manuscript status changes. No software license has been selected automatically. Numerical differences between experiment exports and manuscript values are documented in `docs/RESULTS_NOTES.md`.

Official references:
- https://docs.github.com/en/desktop/overview/creating-your-first-repository-using-github-desktop
- https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository
