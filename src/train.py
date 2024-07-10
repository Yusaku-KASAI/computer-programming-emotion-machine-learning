import os
import sys
import my_library.Trainer as Trainer  # Trainerクラスのインポート
import joblib  # モデルの読み込みに使用

# データとモデルの保存先パスを入力させる
preprocessed_train_data_path = input("Enter the path for the preprocessed data:") 
model_dump_path_base = input("Enter the path for the directory to save the models:")

# Trainerクラスのインスタンスを作成
trainer = Trainer.Trainer()

# データを読み込む
X, y = trainer.load_data(preprocessed_train_data_path)


# ハイパーパラメータのリストを定義
hyperparameters = [0.1, 1, 10, 100, 1000]

# SVMモデルの学習と保存
for h in hyperparameters:
    model_dump_path = os.path.join(model_dump_path_base, f"SVM_{h}.pkl")
    trainer.train_SVM(h, X, y)
    trainer.dump_model(model_dump_path)
    print(f"SVM model with hyperparameter {h} saved to {model_dump_path}")

# RandomForestモデルの学習と保存
hyperparameters = [5, 10, 20, 50, None]
for h in hyperparameters:
    model_dump_path = os.path.join(model_dump_path_base, f"RF_{h}.pkl")
    trainer.train_RF(h, X, y)
    trainer.dump_model(model_dump_path)
    print(f"RandomForest model with hyperparameter {h} saved to {model_dump_path}")