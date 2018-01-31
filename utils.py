from datetime import datetime

def in_future(pass_time, min_time_in_future=0):

    """

    Determines if a time, given as a string, is in the future.
    If optional min_time_in_future is given, will only return True
    if the time is at least min_time_in_future seconds into the future

    # Example: pass_time is 20 seconds in the future. Return True
    # Example: pass_time is 20 seconds in the future. min_time_in_future is 10. Return True
    # Example: pass_time is 20 seconds in the future. min_time_in_future is 40. Return False
    # Example: passtime is negative. return False
    # Example: passtime is now. return False

    """

    now = datetime.today()
    pass_time = datetime.fromtimestamp(pass_time)
    delta = (pass_time - now ).total_seconds()  # Number of seconds passtime is in the future. Negative is pass_time is in the past

    delta = delta - min_time_in_future
    return delta > 0
