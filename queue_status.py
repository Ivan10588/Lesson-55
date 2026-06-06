import json

def update_queue_log(file_path, remaining):
    with open(file_path, 'w') as f:
        json.dump({'remaining': remaining}, f)
    print(f"Log updated, remaining: {remaining}")

def main():
    total = 100
    processed = 85
    remaining = total - processed
    log_file = "queue_status.json"
    update_queue_log(log_file, remaining)

if __name__ == "__main__":
    main()
