# computer-programming-emotion-machine-learning


## 概要
このプロジェクトは、機械学習を利用して、テキストデータを処理し、感情分析を行うシステムです。以下のモジュールがあります：
- 与えた文章データの感情を判定する(メイン)([predict_polarity.py](src/predict_polarity.py))
- 教師データや訓練データおよび感情を判定したい対称データの前処理を行う([preprocess_data.py](src/preprocess_data.py))
- 前処理されたデータから機械学習によりモデルを作成する([train.py](src/train.py))
- 機械学習により作成された複数のモデルから前処理された検証データを用いて最良のモデルを判定する([validate.py](src/validate.py))
- 訓練データと辞書を受け取り、各文についてベクトル化したものとその感情の評価値を返す機能などを持つクラス([my_library/Data_preprocessor.py](src/my_library/Data_preprocessor.py))
- 感情の特徴量(ベクトル)と評価値と指定したパラメータに応じて、機械学習を行いモデルを作成し、モデルを保存する機能などを持つクラス([my_library/Trainer.py](src/my_library/Trainer.py))
- 学習したモデルを検証データで検証し、最良のモデルを保存する機能などを持つクラス([my_library/Validator.py](src/my_library/Validator.py))
- janomeライブラリを利用して文を感情のベクトル化をして返す関数([my_library/count_statistics.py](src/my_library/count_statistics.py))
- 辞書を読み込む関数([my_library/load_dictionary.py](src/my_library/load_dictionary.py))
- 教師データなどのデータを読み込む関数([my_library/load_input_data.py](src/my_library/load_input_data.py))


## ディレクトリ構成
```
my_project/
── README.md
├── requirements.txt
├── data/
│   ├── data.txt
│   ├── dictionary1.txt
│   ├── dictionary2.txt
│   ├── train.txt
│   ├── validation.txt
│   ├── examples/
│   │   ├── data_preprocessed.pkl
│   │   └── train_preprocessed.pkl
│   └── results/
│       └── data01.txt
├── logs/ 
├── models/ 
├── src/
│   ├── predict_polarity.py
│   ├── preprocess_data.py
│   ├── train.py
│   ├── valaidate.py
│   └── my_library/
│       ├── Data_preprocessor.py
│       ├── Trainer.py
│       ├── Validator.py
│       ├── count_statistics.py
│       ├── load_dictionary.py
│       └── load_input_data.py
└── tests/
    └── test_~~~~.py
```

## 実行前の準備

### 前提
python3、pip3が使えることを確認してください。

### データファイルの準備
`data/`ディレクトリに以下のファイルを配置してください：
- `dictionary1.txt`
- `dictionary2.txt`
- `data.txt`

### 仮想環境の準備と起動
プロジェクトを独立した環境で実行できるようにするために仮想環境を作成します。これは、homebrewなどでpythonを外部管理している場合や(外部ライブラリのシステム全体へのインストールが禁止されている場合がある)、他のプロジェクトでライブラリをインストールしてたりする場合に(このプロジェクトの環境と衝突しうる)、次の手順で行うpythonのパッケージのインストールのでエラーが生じうるためです。
以下のコマンドを実行して仮想環境を作成します。
```sh
$ cd [project root]
$ python3 -m venv computer-programming-emotion-machine-learning
```
つづいて、作成した仮想環境をactivateします。

Linux, Mac
```sh
$ source computer-programming-emotion-machine-learning/bin/activate
```
Windows
```sh
$ .\computer-programming-emotion-machine-learning\Scripts\activate
```
これで以下のように表示が変わり、仮想環境が起動しました。
```sh
(computer-programming-emotion-machine-learning)$ 
```

### 依存関係の解決
以下のコマンドを実行して、必要なPythonパッケージを仮想環境にインストールします：
```sh
(~~~)$ pip install -r requirements.txt
```

## プロジェクトの実行方法

### srcディレクトリに移動
```sh
(~~~)$ cd src
```

### preprocess_data.pyの実行
以下のコマンドを実行して、データの前処理を行います：

###### ***補足***
preprocess_data.pyの実行にはかなりの時間がかかるため、それぞれの実行結果として得られるファイルを/data/example/ディレクトリに入れてあります。  
この手順をスキップする場合、以下のコマンドによりファイルを複製してください。
```sh
$ cp ../data/example/data_preprocessed.pkl ../data/data_preprocessed.pkl
$ cp ../data/example/train_preprocessed.pkl ../data/train_preprocessed.pkl
$ cp ../data/example/validation_preprocessed.pkl ../data/validation_preprocessed.pkl
```

#### 教師データの前処理
```sh
(~~~)$ python3 preprocess_data.py
# プロジェクトルートパスが表示される
/Users/~~~~~~/computer-programming-emotion-machine-learning
# 教師データのsrcディレクトリからの相対パスを入力する
Enter the path for the data file: ../data/train.txt
# 辞書データのsrcディレクトリからの相対パスを入力する
Enter the path for the dictionary file: ../data/dictionary1.txt
# 前処理したデータを保存するsrcディレクトリからの相対パスを入力する
Enter the path to save the preprocessed data: ../data/train_preprocessed.pkl
# 教師データはラベル付きの文章なのでYと入力
Enter if the data is labeled (Y/N):Y
# /data/train_processed.pklが生成される
```

#### 検証データの前処理
```sh
(~~~)$ python3 preprocess_data.py
# プロジェクトルートパスが表示される
/Users/~~~~~~/computer-programming-emotion-machine-learning
# 教師データのsrcディレクトリからの相対パスを入力する
Enter the path for the data file: ../data/validation.txt
# 辞書データのsrcディレクトリからの相対パスを入力する
Enter the path for the dictionary file: ../data/dictionary1.txt
# 前処理したデータを保存するsrcディレクトリからの相対パスを入力する
Enter the path to save the preprocessed data: ../data/validation_preprocessed.pkl
# 検証データはラベル付きの文章なのでYと入力
Enter if the data is labeled (Y/N):Y
# /data/validation_processed.pklが生成される
```

#### 感情を判定する対象の文章データの前処理
```sh
# preprocess_data.pyを実行
(~~~)$ python3 preprocess_data.py
# プロジェクトルートパスが表示される
/Users/~~~~~~/computer-programming-emotion-machine-learning
# 教師データのsrcディレクトリからの相対パスを入力する
Enter the path for the data file: ../data/data.txt
# 辞書データのsrcディレクトリからの相対パスを入力する
Enter the path for the dictionary file: ../data/dictionary1.txt
# 前処理したデータを保存するsrcディレクトリからの相対パスを入力する
Enter the path to save the preprocessed data: ../data/data_preprocessed.pkl
# 検証データはラベルなしの文章なのでNと入力
Enter if the data is labeled (Y/N):N
# /data/data_processed.pklが作成される
```

### train.pyの実行
```sh
# train.pyを実行
(~~~)$ python3 train.py
# 前処理した教師データを保存した場所のsrcディレクトリからの相対パスを入力
Enter the path for the preprocessed data:../data/train_preprocessed.pkl
# 機械学習により作成したモデルを保存する場所のsrcディレクトリからの相対パスを入力
Enter the path for the directory to save the models:../models/
# /models/にSVM_0.1.pkl, SVM_1.pkl, SVM_10.pkl, SVM_100.pkl, SVM_1000.pklなどが作成される
```

### validate.pyの実行
```sh
# validate.pyの実行
(~~~)$ python3 validate.py
# Evaluating SVM_0.1.pkl:
# Accuracy: 0.6440625
# Precision: 0.41887417218543044
# Recall: 0.2430355427473583
# Evaluating SVM_10.pkl:
# Accuracy: 0.6471875
# Precision: 0.4087136929460581
# Recall: 0.18924111431316043
# Evaluating SVM_100.pkl:
# Accuracy: 0.64875
# Precision: 0.4133611691022965
# Recall: 0.19020172910662825
# Evaluating SVM_1000.pkl:
# Accuracy: 0.6465625
# Precision: 0.4089068825910931
# Recall: 0.19404418828049952
# Evaluating SVM_1.pkl:
# Accuracy: 0.64
# Precision: 0.41148325358851673
# Recall: 0.2478386167146974
# The best model is saved as 'best_model.pkl' with accuracy: 0.64875
# /models/best_model.pklが作成される
```

### predict_polarity.pyの実行
```sh
(~~~)$ python3 predict_polarity.py >> ../data/results/data01.txt
# /data/results/data01.txtが作成される
# data01.txtの数字は適宜変えて良い
# 各文について、1がポジティブ、-1がネガティブである
```

## テスト
プロジェクトにはユニットテストが含まれています。以下のコマンドを実行してテストを実行できます：
```sh
python -m unittest discover -s tests
```

## ライセンス

## 貢献

## 作者

## 注意
```
この`README.md`は、プロジェクトの基本的な情報を提供し、セットアップや使用方法を明確にするためのものです。また、このプロジェクトは未完成です。必要に応じて、プロジェクトの詳細に合わせて修正してください。
現時点ではユニットテストは作成されていませんので、テストのコマンドを実行してもテストされません。
```
