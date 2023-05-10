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


def main():
    import influxdb_client, os, time
    from influxdb_client import InfluxDBClient, Point, WritePrecision
    from influxdb_client.client.write_api import SYNCHRONOUS

    token = os.environ.get("INFLUXDB_TOKEN")
    org = "Kentucky Fried Chicken"
    url = "http://localhost:8086"

    client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

    bucket = "KFC"

    write_api = client.write_api(write_options=SYNCHRONOUS)

    for value in range(5):
        point = (
            Point("measurement1")
            .tag("tagname1", "tagvalue1")
            .field("field1", value)
        )
        write_api.write(bucket=bucket, org="Kentucky Fried Chicken", record=point)
        time.sleep(1)  # separate points by 1 second


if __name__ == '__main__':
    # # Register the CPU usage at 1-second intervals
    # register_into_log("log.txt", 1)
    #
    # # Register the CPU usage at 3-second intervals
    # register_into_log("log.txt", 3)
    #
    # # Register the CPU usage at 6-second intervals
    # register_into_log("log.txt", 6)
    main()
