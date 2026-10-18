import datetime

def record_session_activity():
    """
    A practical automation script that creates a local text log file
    and writes timestamped updates to verify disk I/O operations.
    """
    log_filename = "activity_log.txt"
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"Initializing file writer for: {log_filename}")
    
    # Writing to a local file safely using a context manager
    with open(log_filename, "w") as file:
        file.write("=== BUILD FORGE WORKSPACE LOG ===\n")
        file.write(f"Session Initialized At : {current_time}\n")
        file.write("Status                  : Environment verification successful.\n")
        file.write("Workspace Readiness     : Confirmed.\n")
        
    print(f"[Success] Local file '{log_filename}' generated dynamically.")

if name == "main":
    record_session_activity()
