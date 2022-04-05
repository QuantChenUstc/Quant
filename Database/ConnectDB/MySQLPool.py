from msilib.schema import SelfReg
import pymysql
from timeit import default_timer
from DBUtils.PooledDB import PooledDB
from sympy import false

host = 'localhost'
port = 3306
db_day = 'data_day'
user = 'root'
password = 'root'

class MysqlConfig:

    def __init__(self, host, db, user, password, port=3306):
        self.host = host
        self.db = db
        self.user = user
        self.password = password
        self.port = port

        self.charset = 'UTF8'
        self.minCached = 10
        self.maxCached = 20
        self.maxShared = 10
        self.maxConnection = 100

        self.blocking = True
        self.maxUsage = 100
        self.setSession = None
        self.reset = True
    
class MysqlPoolConn:
    __pool = None

    def __init__(self, config):
       if not self.__pool:
           self.__class__.__pool = PooledDB(creator=pymysql,
                                            maxconnections=config.maxConnection,
                                            mincached=config.minCached,
                                            maxcached=config.maxCached,
                                            maxshared=config.maxShared,
                                            blocking=config.blocking,
                                            maxusage=config.maxUsage,
                                            setsession=config.setSession,
                                            charset=config.charset,
                                            host=config.host,
                                            port=config.port,
                                            database=config.db,
                                            user=config.user,
                                            password=config.password,
                                            )
    def get_conn(self):
        return self.__pool.connection()


dbConfig = MysqlConfig(host, db_day, user, password, port)

poolConnection = MysqlPoolConn(dbConfig)

class UsingMysql(object):
    def __init__(self, commit=True, logTime = True, logLable='总用时'):
        self._logTime = logTime
        self._commit = commit
        self._logLable = logLable
    
    def __enter__(self):
        if self._logTime is True:
            self._start = default_timer()
        
        conn = poolConnection.get_conn()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        conn.autoCommit = False

        self._conn = conn
        self._cursor = cursor
        return self
    
    def __exit__(self, *exc_info):
        if self._commit:
            self._conn.commit()
        self._cursor.close()
        self._conn.close()

        if self._logTime is True:
            diff = default_timer() - self._start
            print('-- %s: %.6f 秒' % (self._logLable, diff))
    
    def fetch_one(self, sql, params=None):
        self.cursor.execute(sql, params)
        return self.cursor.fetchone()
    
    def fetch_all(self, sql, params=None):
        self.cursor.execute(sql, params)
        return self.cursor.fetchall()

    def get_count(self, sql, params=None, count_key = 'code'):
        self.cursor.execute(sql, params)
        data = self.cursor.fetchone()
        if not data:
            return 0
        return 1
        #return data[count_key]

    @property
    def cursor(self):
        return self._cursor
        