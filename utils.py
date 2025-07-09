import os
from datetime import datetime

LOG_DIR = "logs"
ORDER_LOG = os.path.join(LOG_DIR, "orders.log")
ERROR_LOG = os.path.join(LOG_DIR, "errors.log")

def init_logs():
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

def log_order(order):
    with open(ORDER_LOG, "a") as f:
        f.write(f"\n[{datetime.now()}] Order placed:\n")
        for k, v in order.items():
            f.write(f"  {k}: {v}\n")

def log_error(error):
    with open(ERROR_LOG, "a") as f:
        f.write(f"\n[{datetime.now()}] ERROR: {error}\n")
