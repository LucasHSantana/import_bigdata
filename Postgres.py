import psycopg2
from sqlalchemy import create_engine
from os import getenv

class PostgresConnection():
    def __init__(self, host=None, database=None, port=None, user=None, password=None):
        self._host = host if host else getenv('HOST')
        self._database = database if database else getenv('DATABASE_NAME')
        self._port = port if port else getenv('PORT')
        self._user = user if user else getenv('USERNAME')
        self._pass = password if password else getenv('PASSWORD')

        self._conn = None
        self._cursor = None
        self._engine = None

    def __str__(self):
        """
            Class to str (Ex: print(Object))
            :return: String with Host, Database and Port info
        """
        return f'Host: {self._host}, Database: {self._database}, Port: {self._port}'

    def __repr__(self):
        """
            Class representation (Calling repr(Object) return a valid Python expression to reconstruct the object again) 
            :return: valid Python expression of object
        """
        return f'PostgresConnection(host={self._host}, database={self._database}, port={self._port}, user={self._user}, password={self._pass})'

    def get_engine(self):
        """
            Get sqlalchemy engine (Postgres)
            :return: sqlalchemy engine
        """

        # If engine not exists yet
        if self._engine is None:
            # Create engine            
            self._engine = create_engine(f'postgresql://{self._user}:{self._pass}@{self._host}:{self._port}/{self._database}')

        return self._engine

    def get_connection_and_cursor(self):
        """
            Get psycopg2 connection and cursor
            :return: connection, cursor
        """

        # If connection not exists yet
        if self._conn is None:
            # Create connection            
            self._conn = psycopg2.connect(host=self._host, user=self._user, password=self._pass, database=self._database, port=self._port)
            # Get cursor
            self._cursor = self._conn.cursor()

        return self._conn, self._cursor