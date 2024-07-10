def load(file_path = "../data/dictionary1.txt"):
  with open(file_path, 'r', encoding="utf-8") as f:
    all_lines = f.read()
  all_lines_list = all_lines.strip().split("\n")
<<<<<<< HEAD
  res = []
  for all_lines in all_lines_list:
    res.append(all_lines.split("\t"))
  return res
=======
  res = [line.split("\t") for line in all_lines_list]
  return res
>>>>>>> f74d397e47c0446d8d17125e768b110b7313d947
