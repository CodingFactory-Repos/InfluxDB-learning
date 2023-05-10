import psutil

def get_cpu_usage(interval):
    """
    Returns the current CPU usage percentage.
    """
    return psutil.cpu_percent(interval=interval)

def register_into_log(log_file, interval):
    """
    Registers the current CPU usage percentage into a log file at the specified interval.
    """
    cpu_usage = get_cpu_usage(interval)
    timestamp = psutil.datetime.datetime.now()
    with open(log_file, "a") as f:
        f.write(f"{timestamp} ")
        f.write(f"{cpu_usage}\n")
    print(f"CPU usage: {cpu_usage}% (interval: {interval}s)")

if __name__ == '__main__':
    # Register the CPU usage at 1-second intervals
    register_into_log("log.txt", 1)

    # Register the CPU usage at 3-second intervals
    register_into_log("log.txt", 3)

    # Register the CPU usage at 6-second intervals
    register_into_log("log.txt", 6)
