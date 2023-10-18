import os
import sys

import pyperclip

from .extension_mapping import EXTENSION_TO_MARKDOWN

def print_tree_structure(root_dir, file_extensions=(".py",), prefix=''):
    """
    Returns the directory structure for files with the given extensions, visualized using | and -.
    """
    result_str = ""

    if not os.path.isdir(root_dir):
        return result_str

    items = sorted(os.listdir(root_dir))
    paths = [os.path.join(root_dir, item) for item in items]
    selected_files = [path for path in paths if any(path.endswith(ext) for ext in file_extensions)]
    directories = [path for path in paths if os.path.isdir(path)]

    for sel_file in selected_files:
        result_str += prefix + '|-- ' + os.path.basename(sel_file) + '\n'

    for i, directory in enumerate(directories):
        new_prefix = prefix + '|   ' if i != len(directories) - 1 or selected_files else prefix + '    '
        for dirpath, _, filenames in os.walk(directory):
            if any(fn.endswith(ext) for ext in file_extensions for fn in filenames):
                result_str += prefix + '|-- ' + os.path.basename(directory) + '\n'
                result_str += print_tree_structure(directory, file_extensions, new_prefix)
                break

    return result_str

def copy_code_to_markdown(root_dir, file_extensions=(".py",)):
    """
    Copies code from each file with the given extensions and returns it in markdown format.
    """
    markdown_output = ""

    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if any(filename.endswith(ext) for ext in file_extensions):
                with open(os.path.join(dirpath, filename), 'r') as file:
                    content = file.read()
                    md_ext = EXTENSION_TO_MARKDOWN['.'+filename.rsplit('.', 1)[-1]]
                    full_filename = str(os.path.relpath(os.path.join(dirpath, filename), root_dir))
                    markdown_output += f"\nFile: ./{full_filename}\n"
                    markdown_output += f"\n```{md_ext}\n"
                    markdown_output += content
                    markdown_output += "\n```\n"

    return markdown_output

def main():
    file_extensions = [".py"]
    root_directory = sys.argv[1]

    if "-f" in sys.argv:
        file_extensions = sys.argv[sys.argv.index("-f")+1:]

    tree_structure = print_tree_structure(root_directory, file_extensions)
    markdown_content = copy_code_to_markdown(root_directory, file_extensions)
    msg = ""
    msg += "Tree Directory Structure:\n\n"
    msg += tree_structure
    msg += "\nCode in Markdown Format:\n"
    msg += markdown_content

    pyperclip.copy(msg)

if __name__ == "__main__":
    main()
