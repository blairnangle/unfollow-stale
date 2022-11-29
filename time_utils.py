import time


def time_to_epoch(timestamp: str) -> int:
    return int(time.mktime(time.strptime(timestamp.split(".")[0], '%Y-%m-%dT%H:%M:%S')))


def current_epoch_minus_days(days) -> int:
    return int(time.time()) - days * 60 * 60 * 24
