import requests
import os
import shutil
import time
import csv
from Postgres import PostgresConnection


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')

# Realiza o download do dataset (.zip) e extrai o mesmo na pasta de dados
def extract(url, *kwargs):
    print('Downloading dataset...')    

    response = requests.get(url) # Faz o download    

    file = os.path.join(DATA_DIR, 'archive.zip')

    with open(file, 'wb') as f:
        f.write(response.content) # Grava o arquivo .zip
    print('Done')

    print('Unpacking zip file...')
    shutil.unpack_archive(file, DATA_DIR) # Extrai os arquivos de dentro do .zip
    print('Done')

    print('Removing zip file')
    os.remove(os.path.join(DATA_DIR, 'archive.zip'))
    print('Done')

def commit_data():
    print('Connecting with postgres...')
    pg = PostgresConnection()
    conn, cursor = pg.get_connection_and_cursor()    
    print('Done')    

    print('Saving data to database...')

    # Tempo médio de execução de 6 minutos
    # Abre o csv e copia para a tabela status
    with open(os.path.join(DATA_DIR, "status.csv"), 'r') as f:         
        next(f)        
        cursor.copy_from(f, os.getenv('TABLE_NAME'), sep=',', columns=('station_id', 'bikes_available', 'docks_available', 'time'))
        
    conn.commit()        

    print('Done')

    print('Closing connection...')
    cursor.close()
    conn.close()
    print('Done')
    
if __name__ == "__main__":
    start_time = time.time()

    extract('https://drive.google.com/u/1/uc?id=1XcmPmv91TIt0L3tKf0FWmiwaJbY604pU&export=download&confirm=t')
    commit_data()

    print(f'Execution time (seconds): {time.time() - start_time}' )

