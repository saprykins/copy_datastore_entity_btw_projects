from google.cloud import datastore
import pandas as pd

# project one
client = datastore.Client(project = "ari-dp-hun-dev")
# 'Original_Kind' is the Kind to duplicate
query = client.query(kind="data_transcoding")
entity_list = list(query.fetch())
df_transco = pd.DataFrame(query.fetch())

# project two
client = datastore.Client(project = "ari-dp-prt-uat")

# "New_Kind" with the name of the Kind desired 
kind = 'data_transcoding'
task_key = client.key(kind)

l=0
while l < len(df_transco):
    for clm in df_transco.columns:
        task = datastore.Entity(key=task_key)
        task['description'] = df_transco['description'][l]
        task['std_code'] = df_transco['std_code'][l]
        task['start_date'] = df_transco['start_date'][l]
        task['country'] = df_transco['country'][l]
        task['code'] = df_transco['code'][l]
        task['std_description'] = df_transco['std_description'][l]
        task['application'] = df_transco['application'][l]
        task['object'] = df_transco['object'][l]
        task['end_date'] = df_transco['end_date'][l]
    client.put(task)
    l=l+1
