import pandas as pd
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    sample_dict = {
        "Name": [
                "Braund, Mr. Owen Harris",
                "Allen, Mr. William Henry",
                "Bonnell, Miss. Elizabeth",
            ],
            "Age": [22, 35, 58],
            "Sex": ["male", "male", "female"],
    }

    df = pd.DataFrame(sample_dict)
    print(df)
    return df.to_json()
