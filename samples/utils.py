from datetime import datetime
#Convert date and time to string
def generate_timestamp():
    unformarted_time= datetime.now()
    formarted_time= unformarted_time.strftime("%Y%m%d%H%M%S")

    return formarted_time