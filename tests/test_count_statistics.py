import os,sys
import pytest
import pickle
import numpy as np
import pytest
from janome.tokenizer import Tokenizer

project_root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root_path)
sys.path.append(os.path.join(project_root_path, "src", "my_library"))

import src.my_library.count_statistics as count_statistics

@pytest.fixture(scope="module")
def setup_module():
    dic = [
        ("good", "p"),
        ("bad", "n"),
        ("neutral", "e")
    ]
    return dic

def test_count_and_vectorize_positive(setup_module):
    dic = setup_module
    sent = "This movie is good."
    result = count_statistics(dic, sent)
    
    assert result[0] == 1  # num_positive
    assert result[1] == 0  # num_negative
    assert result[2] == 0  # num_neutral
    assert result[3] == 1  # num_total (only positive)

def test_count_and_vectorize_negative(setup_module):
    dic = setup_module
    sent = "This movie is bad."
    result = count_statistics(dic, sent)
    
    assert result[0] == 0  # num_positive
    assert result[1] == 1  # num_negative
    assert result[2] == 0  # num_neutral
    assert result[3] == 1  # num_total (only negative)

def test_count_and_vectorize_neutral(setup_module):
    dic = setup_module
    sent = "This movie is neutral."
    result = count_statistics(dic, sent)
    
    assert result[0] == 0  # num_positive
    assert result[1] == 0  # num_negative
    assert result[2] == 1  # num_neutral
    assert result[3] == 1  # num_total (only neutral)

def test_count_and_vectorize_multiple_words(setup_module):
    dic = setup_module
    sent = "This movie is good but sometimes bad."
    result = count_statistics(dic, sent)
    
    assert result[0] == 1  # num_positive
    assert result[1] == 1  # num_negative
    assert result[2] == 0  # num_neutral
    assert result[3] == 2  # num_total (positive and negative)

def test_count_and_vectorize_no_match(setup_module):
    dic = setup_module
    sent = "This movie is amazing."
    result = count_statistics(dic, sent)
    
    assert result[0] == 0  # num_positive
    assert result[1] == 0  # num_negative
    assert result[2] == 0  # num_neutral
    assert result[3] == 0  # num_total (no match)