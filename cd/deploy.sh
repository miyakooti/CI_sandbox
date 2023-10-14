# functionフォルダにいることが前提

# init

# cd functions
python gen_env.py salesforce


# if [ -d upload ];then\
#     rm -rf upload;\
# fi
# mkdir upload
# rsync -ahv --progress ./salesforce/ ./upload/ --exclude '__pycache__'
# cp ./config.py ./upload/
# cp ./etl.py ./upload/
# cp ./slack_notification.py ./upload/
# cd upload &&\
# gcloud functions deploy salesforce --gen2 --runtime=python310 --source=. --entry-point=salesforce --region=asia-northeast1 --trigger-topic=raw-datalake --env-vars-file .env.yaml --memory 8192;\
# rm -rf ./upload/
