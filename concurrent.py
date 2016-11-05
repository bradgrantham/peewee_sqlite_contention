# import threading
import multiprocessing
import time
import datetime
import subprocess
import uuid
import base64
import flask
import peewee
import hashlib
import random
from validate_email import validate_email

# require_login decorator?
# cookies - secure
# add "forgot password" button and link, prototype functionality

app = flask.Flask(__name__)

pwdb = peewee.SqliteDatabase("test.db", threadlocals=True)
pwdb.connect()

class TimedLock():
    def __init__(self, lock):
        self.lock = lock

    def __enter__(self):
        attempts, succeeded = 0, False

        while not succeeded and attempts < 5:
            succeeded = self.lock.acquire(True) # attempts > 3)
            time.sleep(.1)
            attempts += 1

        if not succeeded:
            raise LockFailedException()

        return self.lock

    def __exit__(self, type, value, traceback):
        self.lock.release()

dblock = TimedLock(multiprocessing.Lock())
# dblock = multiprocessing.Lock()


class BaseModel(peewee.Model):
    class Meta:
        database = pwdb

class DumbThingie(BaseModel):
    thingie = peewee.BlobField(default="hi")
    blargA = peewee.BlobField(null = True)
    blargB = peewee.BlobField(null = True)
    blargC = peewee.BlobField(null = True)
    blargD = peewee.BlobField(null = True)
    blargE = peewee.BlobField(null = True)
    blargF = peewee.BlobField(null = True)
    blargG = peewee.BlobField(null = True)
    blargH = peewee.BlobField(null = True)
    blargI = peewee.BlobField(null = True)
    blargJ = peewee.BlobField(null = True)

class LockFailedException(BaseException):
    pass

@app.route("/dumb/<mb>", methods=['GET'])
def dumb(mb):
    mb = int(mb)

    try:
        with dblock:
            print "creating."
            blarg = DumbThingie.create()
    except peewee.OperationalError:
        print 'OperationalError in create'
        return 'OperationalError in create'

    print "generating."
    q = '*' * 1024
    qq = q * 1024
    qqqA = qq * mb
    qqqB = qq * mb
    qqqC = qq * mb
    qqqD = qq * mb
    qqqE = qq * mb
    qqqF = qq * mb
    qqqG = qq * mb
    qqqH = qq * mb
    qqqI = qq * mb
    qqqJ = qq * mb
    blarg.blargA = qqqA
    blarg.blargB = qqqB
    blarg.blargC = qqqC
    blarg.blargD = qqqD
    blarg.blargE = qqqE
    blarg.blargF = qqqF
    blarg.blargG = qqqG
    blarg.blargH = qqqH
    blarg.blargI = qqqI
    blarg.blargJ = qqqJ

    try:
        with dblock:
            print "saving."
            blarg.save()
    except peewee.OperationalError:
        print 'OperationalError in save'
        return 'OperationalError in save'

    print "done."

    return ''


#############################################################################
# Main

random.seed()

if __name__ == "__main__":

    if not DumbThingie.table_exists():
        DumbThingie.create_table()

    app.run(debug = True, port=5050, processes=4)
