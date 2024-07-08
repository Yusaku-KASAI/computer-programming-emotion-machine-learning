import os
def load_traindata():
  # ファイルの絶対パスを取得
  base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
  file_path = os.path.join(base_path, 'data', 'train.txt')
  with open(file_path, 'r', encoding="utf-8") as f:
    all_lines = f.read()
  all_lines_list = all_lines.strip().split("\n")
  res = []
  for all_lines in all_lines_list:
    res.append(all_lines.split("\t"))
  return res


def load_raw_data():
  # ファイルの絶対パスを取得
  base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
  file_path = os.path.join(base_path, 'data', 'data.txt')
  with open(file_path, 'r', encoding="utf-8") as f:
    all_lines = f.read()
  all_lines_list = all_lines.strip().split("\n")
  return all_lines_list