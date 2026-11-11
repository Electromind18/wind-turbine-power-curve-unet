"""Check notebook JSON and Python syntax without executing research code."""
from pathlib import Path
import ast
import json

root = Path(__file__).resolve().parents[1]
for path in sorted((root / "notebooks").glob("*.ipynb")):
    notebook = json.loads(path.read_text())
    assert notebook["nbformat"] == 4
    assert isinstance(notebook["cells"], list)
    for index, cell in enumerate(notebook["cells"], start=1):
        assert cell["cell_type"] in {"code", "markdown", "raw"}
        if cell["cell_type"] == "code":
            ast.parse("".join(cell["source"]), filename=f"{path.name}:cell{index}")
            assert not cell["outputs"], f"Unexpected outputs: {path.name} cell {index}"
    print(f"PASS {path.name}")
