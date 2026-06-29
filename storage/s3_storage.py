import os
from io import BytesIO

import boto3
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION")
)

BUCKET_NAME = os.getenv("S3_BUCKET_NAME")


def load_csv(filename):
    """
    Load a CSV file from the S3 bucket and return a Pandas DataFrame.
    """

    key = f"raw/{filename}"

    response = s3.get_object(
        Bucket=BUCKET_NAME,
        Key=key
    )

    csv_data = response["Body"].read()

    df = pd.read_csv(BytesIO(csv_data))

    return df
