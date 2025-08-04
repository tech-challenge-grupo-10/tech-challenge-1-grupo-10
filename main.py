import polars as pl
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline

def prepare_model_with_dataset():
    # Load the dataset
    df = pl.read_csv("./data/data.csv")
    df = df.drop(df.columns[-1])

    df = df.rename({"concave points_mean":"concave_points_mean"})

    labelEncoder = LabelEncoder()
    adequated_diagnosis = pl.Series("diagnosis_int",labelEncoder.fit_transform(df.select('diagnosis')))
    df.insert_column(2, adequated_diagnosis)

    y = df["id", "diagnosis", "diagnosis_int"]
    X = df["radius_mean","texture_mean","perimeter_mean","area_mean","smoothness_mean","compactness_mean","concavity_mean","concave_points_mean","symmetry_mean","fractal_dimension_mean"]
    X_train, eval_data, y_train, _ = train_test_split(X, y.get_column("diagnosis_int"), test_size=0.2, random_state=42)

    return eval_data, train_model(X_train, y_train)

def train_model(X_train, y_train):
    rlog_model = make_pipeline(MinMaxScaler(), LogisticRegression(), memory=None)
    rlog_model.fit(X_train, y_train)

    return rlog_model

def main():
    eval_data, model = prepare_model_with_dataset()
    y_pred_rlog = model.predict(eval_data)
    print(y_pred_rlog)
    

if __name__ == "__main__":
    main()
