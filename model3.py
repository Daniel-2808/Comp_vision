import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_auc_score, average_precision_score
from sklearn.metrics import confusion_matrix, classification_report

seed=42
np.random.seed(seed)
tf.random.set_seed(seed)

X,y=make_classification(
n_samples=1000,
n_features=20,
n_informative=10,
n_redundant=5,
random_state=seed)

X_train,X_temp,y_train,y_temp=train_test_split(
X,y,test_size=0.30,stratify=y,random_state=seed)

X_val,X_test,y_val,y_test=train_test_split(
X_temp,y_temp,test_size=0.50,stratify=y_temp,random_state=seed)

scaler=StandardScaler()

X_train=scaler.fit_transform(X_train)
X_val=scaler.transform(X_val)
X_test=scaler.transform(X_test)

model=tf.keras.Sequential([
tf.keras.layers.Dense(128,activation="relu",input_shape=(X_train.shape[1],)),
tf.keras.layers.Dropout(0.3),
tf.keras.layers.Dense(64,activation="relu"),
tf.keras.layers.Dense(32,activation="relu"),
tf.keras.layers.Dense(1,activation="sigmoid")
])

model.compile(
optimizer="adam",
loss="binary_crossentropy",
metrics=[
tf.keras.metrics.Precision(name="precision"),
tf.keras.metrics.Recall(name="recall"),
tf.keras.metrics.AUC(name="auc")
])

history=model.fit(
X_train,y_train,
validation_data=(X_val,y_val),
epochs=150,
batch_size=32
)

pred=model.predict(X_test).ravel()

print("ROC AUC:",roc_auc_score(y_test,pred))
print("PR AUC:",average_precision_score(y_test,pred))

y_pred=(pred>=0.5).astype(int)

cm=confusion_matrix(y_test,y_pred)
print(cm)
print(classification_report(y_test,y_pred))

# GRAFICAS LINEALES
plt.plot(history.history["loss"])
plt.plot(history.history["val_loss"])
plt.title("Loss")
plt.legend(["Train","Validation"])
plt.show()

plt.plot(history.history["precision"])
plt.plot(history.history["val_precision"])
plt.title("Precision")
plt.legend(["Train","Validation"])
plt.show()

plt.plot(history.history["recall"])
plt.plot(history.history["val_recall"])
plt.title("Recall")
plt.legend(["Train","Validation"])
plt.show()

plt.plot(history.history["auc"])
plt.plot(history.history["val_auc"])
plt.title("AUC")
plt.legend(["Train","Validation"])
plt.show()