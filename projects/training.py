import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier


def makePrediction(csv, userInputs):
    df = pd.read_csv(csv)
    new_df = df

    x_cols = df.iloc[:, :-1]

    unique_values = df.iloc[:, -1].unique()
    # print(unique_values)

    numerical_columns = x_cols.select_dtypes(include=['int64', 'float64'])

    for column in numerical_columns.columns:
        # Fill missing values with the mean of the column
        x_cols.loc[:, column].fillna(x_cols[column].mean(), inplace=True)

    categorical_columns = x_cols.select_dtypes(include=['object'])

    for column in categorical_columns.columns:
        # Fill missing values with the most frequent value (mode)
        x_cols.loc[:, column].fillna(
            x_cols[column].mode().iloc[0], inplace=True)
        # Encode categorical variables using one-hot encoding
        x_cols = pd.get_dummies(x_cols, columns=[column])

    x_cols = x_cols.replace({True: 1, False: 0})

    last_column = df.columns[-1]
    label_encoder = LabelEncoder()

    if df[last_column].dtype == 'object':
        df[last_column] = label_encoder.fit_transform(df[last_column])

    X = x_cols.iloc[:, :].values
    y = df.iloc[:, -1].values

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=0)

    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    classifier = DecisionTreeClassifier(criterion='entropy', random_state=0)
    classifier.fit(X_train, y_train)

    new_list = []

    for item in userInputs:
        if item.isdigit():  # Check if the item is a number
            # Convert to integer and add to the new list
            new_list.append(int(item))
        else:
            try:
                new_list.append(float(item))
            except ValueError:
                new_list.append(item)

    print(new_list)
    ans = classifier.predict(sc.transform([new_list]))

    # print(unique_values)

    last_column = new_df.columns[-1]
    print(new_df[last_column].dtype)

    if type(unique_values[0]) == str:
        return unique_values[ans[0]]
    else:
        return ans[0]
