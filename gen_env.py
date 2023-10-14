import os
import sys
import platform

if __name__ == "__main__":
    source = sys.argv[1]
    if source == "":
        raise Exception()
    source = source.upper()

    CREDENTIAL_BUCKET = source + "_CREDENTIAL_BUCKET"
    # CREDENTIAL_BLOB = source + "_CREDENTIAL_BLOB"
    # GCS_BUCKET = source + "_GCS_BUCKET"
    # GCS_BLOB = source + "_GCS_BLOB"
    # GBQ_DATASET = source + "_GBQ_DATASET"
    # GBQ_TABLE = source + "_GBQ_TABLE"
    # SLACK_API_TOKEN = "SLACK_API_TOKEN"
    # SLACK_NOTIFICATION_CHANNEL = "SLACK_NOTIFICATION_CHANNEL"

    credential_bucket = os.environ[CREDENTIAL_BUCKET]
    # credential_blob = os.environ[CREDENTIAL_BLOB]
    # gcs_bucket = os.environ[GCS_BUCKET]
    # gcs_blob = os.environ[GCS_BLOB]
    # gbq_dataset = os.environ[GBQ_DATASET]
    # gbq_table = os.environ[GBQ_TABLE]
    # slack_api_token = os.environ[SLACK_API_TOKEN]
    # slack_notification_channel = os.environ[SLACK_NOTIFICATION_CHANNEL]

    pf = platform.system()
    if pf == "Linux":
        source = sys.argv[1]

    FILE_PATH = "./" + source + "/.env.yaml"
    with open(FILE_PATH, "w+") as f:
        f.write(CREDENTIAL_BUCKET + ": " + credential_bucket + "\n")
        # f.write(CREDENTIAL_BLOB + ": " + credential_blob + "\n")
        # f.write(GCS_BUCKET + ": " + gcs_bucket + "\n")
        # f.write(GCS_BLOB + ": " + gcs_blob + "\n")
        # f.write(GBQ_DATASET + ": " + gbq_dataset + "\n")
        # f.write(GBQ_TABLE + ": " + gbq_table + "\n")
        # f.write(SLACK_API_TOKEN + ": " + slack_api_token + "\n")
        # f.write(SLACK_NOTIFICATION_CHANNEL + ": " + slack_notification_channel + "\n")
