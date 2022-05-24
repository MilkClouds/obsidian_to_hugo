import argparse, re, os, shutil
from pathlib import Path
import links_processor
def process_file(text, args):
    text = links_processor.replace_links_helper(text, args)
    return text
def process_content(args):
    hugo_content_dir = args.hugo_content_dir
    obsidian_content_dir = args.obsidian_content_dir
    for root, dirs, files in os.walk(obsidian_content_dir):
        root = Path(root)
        for file in files:
            if file.endswith(".md"):
                filePath = Path.joinpath(hugo_content_dir, Path.relative_to(root, obsidian_content_dir), file)
                with open(filePath, "r", encoding="UTF-8") as f:
                    text = f.read()
                print("Processing", Path.joinpath(obsidian_content_dir, file))
                text = process_file(text, args)
                with open(filePath, "w", encoding="UTF-8") as f:
                    f.write(text)
def copy(src, dst):
    if os.path.isdir(dst):
        dst = os.path.join(dst, os.path.basename(src))
    shutil.copyfile(src, dst)
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--hugo-dir", default = Path("../blog"))
    parser.add_argument("--hugo-content-dir", default = Path("../blog/content/post/"))
    parser.add_argument("--hugo-attachments-dir", default = Path("../blog/static/attachments/"))
    parser.add_argument("--obsidian-content-dir", default = Path("./blog/"))
    parser.add_argument("--obsidian-attachments-dir", default = Path("./Attachments/"))
    args = parser.parse_args()
    shutil.copytree(args.obsidian_content_dir, args.hugo_content_dir, dirs_exist_ok=True)
    process_content(args)
if __name__ == "__main__":
    main()