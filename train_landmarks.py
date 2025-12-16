import numpy as np
import os, csv, json
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, BatchNormalization
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.callbacks import EarlyStopping

DATA_DIR = "dataset_landmarks"

X, y = [], []
labels = sorted(os.listdir(DATA_DIR))
label_map = {i: label.replace(".csv", "") for i, label in enumerate(labels)}

for idx, file in enumerate(labels):
    path = os.path.join(DATA_DIR, file)
    with open(path, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            X.append([float(v) for v in row])
            y.append(idx)

X = np.array(X, dtype=np.float32)
y = to_categorical(y, num_classes=len(labels))

X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = Sequential([
    BatchNormalization(input_shape=(X.shape[1],)),
    Dense(256, activation="relu"),
    Dropout(0.3),
    Dense(128, activation="relu"),
    Dropout(0.2),
    Dense(len(labels), activation="softmax")
])

model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

early_stop = EarlyStopping(
    monitor="val_loss",
    patience=10,
    restore_best_weights=True
)

model.fit(
    X_train, y_train,
    validation_data=(X_val, y_val),
    epochs=100,
    batch_size=32,
    callbacks=[early_stop]
)

model.save("sign_language_model.h5")

with open("label_map.json", "w") as f:
    json.dump(label_map, f, indent=2)

print("✅ Model trained & saved successfully")
print("📁 Labels:", label_map)
