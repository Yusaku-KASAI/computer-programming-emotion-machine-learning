import sklearn.svm as SVM
import sklearn.ensemble as Ensemble
import pickle
import numpy as np
import os

class Trainer:
    def __init__(self):
        """
        Trainerクラスのコンストラクタ。
        """
        self.model = None  # モデルを格納するインスタンス変数を初期化

    def load_data(self, file_path):
        """
        データセットのファイルパスからデータを読み込み、特徴量とラベルを分けて返す。
        Args:
            file_path (str): データセットのファイルパス

        Returns:
            X (numpy.ndarray): 前処理済みの訓練データ
            y (numpy.ndarray): ラベルデータ
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist.")
        
        with open(file_path, 'rb') as f:
            X, y = pickle.load(f)
        return X, y

    def dump_model(self, file_path):
        """
        学習したモデルを指定されたファイルパスに保存する。
        Args:
            file_path (str): モデルを保存するファイルパス
        """
        with open(file_path, 'wb') as f:
            pickle.dump(self.model, f)

    def load_model(self, file_path):
        """
        指定されたファイルパスからモデルを読み込む。
        Args:
            file_path (str): モデルを読み込むファイルパス
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist.")
        
        with open(file_path, 'rb') as f:
            self.model = pickle.load(f)

    def train_SVM(self, hyperparameter, X, y):
        """
        SVMによる学習をおこなう。正則化パラメータの値を指定する
        Args:
            hyperparameter (float): 正則化パラメータの値
            X (numpy.ndarray): 前処理済みの訓練データ
            y (numpy.ndarray): ラベルデータ
        """
        self.model = SVM.SVC(C=hyperparameter)
        self.model.fit(X, y)

    def train_RF(self, hyperparameter, X, y):
        """
        RandomForestによる学習をおこなう。各決定木の最大深さを指定する
        Args:
            hyperparameter (float): 最大深さの値
            X (numpy.ndarray): 前処理済みの訓練データ
            y (numpy.ndarray): ラベルデータ
        """
        self.model = Ensemble.RandomForestClassifier(max_depth=hyperparameter)
        self.model.fit(X, y)
