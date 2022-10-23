import requests
import os
import shutil
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from sqlalchemy import create_engine
import time
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')

# HOST = 'postgis'
HOST = 'localhost'
DBNAME = 'sfbike'
USR = 'postgres'
PWD = 'postgres'
PORT = 5432

def extract(url, *kwargs):
    print('Downloading dataset...')
    response = requests.get(url)
    file = os.path.join(DATA_DIR, 'archive.zip')

    with open(file, 'wb') as f:
        f.write(response.content)
    print('Done')

    print('Unpacking zip file...')
    shutil.unpack_archive(file, DATA_DIR)
    print('Done')

def commit_data():
    print('Connecting with postgres...')
    # conn1 = psycopg2.connect(host='localhost', user=USR, password=PWD, port=PORT)
    conn = psycopg2.connect(host=HOST, user=USR, password=PWD)
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()
    print('Done')    

    print('Creating database...')
    cursor.execute(f'DROP DATABASE IF EXISTS {DBNAME}')
    cursor.execute(f'CREATE DATABASE {DBNAME}')    
    
    cursor.close()
    conn.close()
    print('Done')

    time.sleep(2)

    print('Connecting with database...')
    engine = create_engine(f'postgresql://{USR}:{PWD}@{HOST}:{PORT}/{DBNAME}')
    print('Done')

    time.sleep(2)

    print('Saving data to database...')

    # Extremamente lento
    # df = pd.read_csv(os.path.join(DATA_DIR, 'status.csv'))
    # df.to_sql('status', engine, index=False)    

    # Tempo de execução médio de 44 minutos
    chunksize = 10 ** 6
    with pd.read_csv(os.path.join(DATA_DIR, 'status.csv'), chunksize=chunksize) as reader:
        for chunk in reader:
            chunk['time'] = pd.to_datetime(chunk['time'])        
            chunk.to_sql('status', engine, index=False, if_exists='append')

    print('Done')

    print('Closing connection...')    
    print('Done')
    

if __name__ == "__main__":
    start_time = time.time()

    # extract('https://storage.googleapis.com/kaggle-data-sets/57/793589/compressed/status.csv.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20221008%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20221008T202509Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=6467169761901c503ce787ff45ef9e0d2f2cdbf332be14b9c0fea4a0b72f26bac08168ab58204e5690233015ca8fdc4c664d988dcf75c277767533c70b62ce793141cd8e37e79c1f028564dfd360e4a064c31e3b889652dc5475c41286a04f0b49debbc767b81b805128d751d82005c13783379de6dee4672398cca0c80efd3292d55e09b07e2f46e64a54718b6b9efae927e35643ba779a3fa69591b1b1a7ed06a1e0568f55e1b7f8e4cdfea628d574f27025afe2468a466795b5086ce79fde457e2239b1e45ac04c135a8e1d3496a032ca609670b96001861c8dab10b5383f7b833d23e83553b004289a324f48bee4570fd20b98e2f91b3a8096cdce58e900')
    commit_data()

    print(f'Tempo de execução: {time.time() - start_time}' )

