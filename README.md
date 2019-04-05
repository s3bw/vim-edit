<h1 align="center">
    Vim-Edit
</h1>

<h4 align="center">
    Just opening file-like objects in vim.
</h4>

## Usage

Open the file in your vim editor. Changes are saved.

```python
from vim_edit import editor

with open("README.md") as file:
    editor.open(file)
```
