# Codecopy

Prepare to chat about your code base with ChatGPT. You can filter files based on the file extension (e.g. `.py`, `.c`, `.fs`, `.html`)

1. Print the tree directory structure
2. Copy and paste all your codes in a Markdown format.

### Installation
```bash
git clone https://github.com/sangkeun00/codecopy.git
cd codecopy
pip install .
```

### Usage
```bash
codecopy /path/to/dir # by default, it only considers .py files
```

```bash
codecopy /path/to/dir -f .js .html
```

### Tips
If your code is too long, you can split your prompt at
[https://chatgpt-prompt-splitter.vercel.app](https://chatgpt-prompt-splitter.vercel.app).
