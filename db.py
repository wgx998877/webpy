class _Engine(object):
    def __init__(self , connect):
        self._connect = connect
    def connect (self):
        return self._connect()
engine = None
class _Dbctx(threading.local):
    def __init__(self):
        self.connect = None
        self.transactions = 0
    def is_init(self):
        self.connection = _LasyConnection()
        self.transactions = 0
    def cleanup(self):
        self.connection.cleanup()
        self.connection = None
    def cursor(self):
        return self.connection.cursor()
_db_ctx = _Dbctx()

class _ConnectionCtx(object):
    def __enter__(self):
        global _db_ctx
        self.should_cleanup = False
        if not _db_ctx.is_init():
            _db_ctx.init()
            self.should_cleanup = True
        return self
    def __exit__ (self,exctype,excvalue,traceback):
        global _db_ctx
        if self.should_cleanup:
            _db_ctx.cleanup()
    def connection():
        return _ConnectionCtx()

with connection():
    do_some_db_operation() 
