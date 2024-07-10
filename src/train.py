import os
import sys
import numpy as np
from sklearn.ensemble import VotingClassifier
project_root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.append(project_root_path)
import my_library.Trainer as Trainer

preprocessed_train_data_path = input("Enter the path for the preprocessed data:") 
model_dump_path_base = input("Enter the path for the directory to save the models:")

trainer = Trainer.Trainer()
X, y = trainer.load_data(preprocessed_train_data_path)

# SVMモデルのトレーニング
svm_hyperparameters = [0.1, 1, 10, 100, 1000]
svm_models = []
for h in svm_hyperparameters:
    trainer.train_SVM(h, X, y)
    svm_models.append(trainer.model)

# ランダムフォレストモデルのトレーニング
rf_hyperparameters = [5, 10, 15, 20, 25]
rf_models = []
for h in rf_hyperparameters:
    trainer.train_RF(h, X, y)
    rf_models.append(trainer.model)

# アンサンブルモデルの作成
ensemble_estimators = [('svm_' + str(h), model) for h, model in zip(svm_hyperparameters, svm_models)] + \
                      [('rf_' + str(h), model) for h, model in zip(rf_hyperparameters, rf_models)]

ensemble_model = VotingClassifier(estimators=ensemble_estimators, voting='soft')
ensemble_model.fit(X, y)

# アンサンブルモデルの保存
ensemble_model_path = os.path.join(model_dump_path_base, "ensemble_model.pkl")
trainer.model = ensemble_model
trainer.dump_model(ensemble_model_path)