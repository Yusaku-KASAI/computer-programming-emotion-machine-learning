def load(file_path = "../data/dictionary1.txt"):

  with open(file_path, 'r', encoding="utf-8") as f:
    all_lines = f.read()
  all_lines_list = all_lines.strip().split("\n")
  res = [line.split("\t") for line in all_lines_list]
  return res
