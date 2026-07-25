import requests
import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

# Dragon Ball API URL
url = "https://dragonball-api.com/api/characters"

username = "postgres"
password = quote_plus("admin123")
host = "localhost"
port = "5432"
database = "DE_Bootcamp"

# Create connection
engine = create_engine(f"postgresql://{username}:{password}@{host}:{port}/{database}"
        )

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    df = pd.DataFrame(data["items"])

    df = df.drop(columns=["image", "deletedAt"], errors="ignore")

    pd.set_option("display.max_columns", None)
    pd.set_option("display.max_rows", None)

    # print(df)

    df.to_csv("dragonball_clean.csv", index=False)

    print("\nCSV file created successfully!")

    df.to_sql(
        "DBcharacters",
        engine,
        if_exists="replace",
        index=False
    )

    print("Data loaded successfully into PostgreSQL!")

else:
    print("Error:", response.status_code)

  