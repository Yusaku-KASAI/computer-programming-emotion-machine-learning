import os,sys
import pytest
import pickle
import pytest


project_root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root_path)
sys.path.append(os.path.join(project_root_path, "src", "my_library"))

import src.my_library.load_dictionary as load_dictionary

@pytest.fixture(scope="module")
def setup_module():
    # テスト用のテキストファイルを作成し、データを準備する
    file_path = "test_dictionary.txt"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write("word1\tpositive\n")
        f.write("word2\tnegative\n")
        f.write("word3\tneutral\n")
    
    yield file_path
    
    # テスト後にファイルを削除する
    os.remove(file_path)

def test_load(setup_module):
    file_path = setup_module
    
    # load関数を呼び出す
    loaded_data = load_dictionary(file_path)
    
    # テスト
    assert len(loaded_data) == 3
    assert loaded_data[0][0] == "word1"
    assert loaded_data[0][1] == "positive"
    assert loaded_data[1][0] == "word2"
    assert loaded_data[1][1] == "negative"
    assert loaded_data[2][0] == "word3"
    assert loaded_data[2][1] == "neutral"

def test_load_default_file():
    # デフォルトのファイルパスでload関数を呼び出す
    loaded_data = load_dictionary()
    
    # テスト（ファイルの存在と読み込みが成功することを確認）
    assert len(loaded_data) > 0
    assert isinstance(loaded_data[0], list)
