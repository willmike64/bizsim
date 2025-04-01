
import datetime

LOGFILE = "app_flow_log.txt"

def log_event(event: str):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOGFILE, "a") as f:
        f.write(f"[{timestamp}] {event}\n")
