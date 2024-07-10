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
"""
# SVMモデルの学習と保存
for h in hyperparameters:
    model_dump_path = os.path.join(model_dump_path_base, f"SVM_{h}.pkl")
    trainer.train_SVM(h, X, y)
    trainer.dump_model(model_dump_path)
    print(f"SVM model with hyperparameter {h} saved to {model_dump_path}")"""

# RandomForestモデルの学習と保存
n_estimators_list = [50, 100, 200, 500]
max_depth_list = [5, 10, 20, 50, None]

for n_estimators in n_estimators_list:
    for max_depth in max_depth_list:
        model_dump_path = os.path.join(model_dump_path_base, f"RF_n{n_estimators}_d{max_depth}.pkl")
        trainer.train_RF(n_estimators, max_depth, X, y)
        trainer.dump_model(model_dump_path)
        print(f"RandomForest model with n_estimators={n_estimators} and max_depth={max_depth} saved to {model_dump_path}")