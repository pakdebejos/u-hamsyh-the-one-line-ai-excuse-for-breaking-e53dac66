"""Tribal Knowledge, Deployed: an entry for the make.fun bounty "The One-Line AI Excuse for Breaking Production".

The program writes the entry text - one line, 123 characters -
to entry.txt (123 characters, inside the 1-180 gate) in the output directory (MAKEFUN_OUTPUT_DIR locally, /output
in the grader). The text is a fixed constant with no trailing newline, so
both of the grader's runs write byte-identical output.
"""
import os

LINE = "I did not break production, I simply deployed your undocumented tribal knowledge to a server that had never met you before."

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)  # no trailing newline: both grader runs byte-identical

if __name__ == "__main__":
    main()
