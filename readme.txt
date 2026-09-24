File Integrity Checker

A lightweight Python script that checks the integrity of files in selected system directories by calculating their SHA-256 hashes and logging unexpected or inaccessible files.

Overview

This project is designed as a simple starting point for file integrity monitoring.

The script:

Scans files inside predefined system directories.

Calculates a SHA-256 hash for each file.

Compares the calculated hash against previously stored hashes.

Logs files whose hash does not match a known value.

Logs files that cannot be accessed because of permission or operating-system errors.

Prints the analysis status directly to the terminal.

Note: The current implementation initializes an empty hash dictionary on every execution. Therefore, all scanned files will currently be reported as [WARNING]. Persistent baseline hashes are not implemented yet.

Requirements

Python 3.8+

A Unix-like operating system

Sufficient permissions to read the directories being scanned

The script uses only Python standard-library modules:

hashlib

os

No external dependencies are required.

Usage

Clone the repository and run the script:

python3 main.py


Depending on the permissions of the user running the script, some files may generate permission errors.

For example:

[WARNING] /bin/example
Warning: /bin/restricted_file: [Errno 13] Permission denied

Configuration

The directories to scan can be configured through the DIRECTORIOS_SISTEMA variable:

DIRECTORIOS_SISTEMA = [
    "/bin",
]


Additional directories can be added:

DIRECTORIOS_SISTEMA = [
    "/bin",
    "/usr/bin",
    "/usr/local/bin",
]


The log files are configured through:

LOG_HASHES = "negatives_logs.txt"
LOG_ERRORES = "errors_logs.txt"

Logs
negatives_logs.txt

Contains files whose calculated SHA-256 hash does not match a stored hash.

Example:

/bin/example - HASH: 8a4c...

errors_logs.txt

Contains files that could not be analyzed because of PermissionError or OSError.

Example:

/bin/restricted_file - ERROR: [Errno 13] Permission denied


Both log files are cleared every time the program starts.

How It Works

The program follows three main steps:

Initialize

Creates an empty hash dictionary.

Clears the previous log files.

Scan

Recursively walks through the configured directories using os.walk().

Opens each file in binary mode.

Hash and compare

Calculates a SHA-256 hash using hashlib.sha256().

Compares the result with the hash stored for that file.

Reports the result to the terminal and appropriate log file.

Current Limitations

This project is intentionally simple and currently has several limitations:

Hashes are not persisted between executions.

The hash dictionary starts empty on every run.

Only /bin is scanned by default.

Large files are read entirely into memory before hashing.

Log files are overwritten when the program starts.

There is no command-line interface yet.

There is no mechanism to automatically establish or update a trusted baseline.

Future Improvements

Possible improvements include:

Persisting baseline hashes in a JSON or database file.

Adding an initialization mode to create a trusted baseline.

Streaming files in chunks instead of loading them entirely into memory.

Adding command-line arguments for directories and log locations.

Supporting multiple hash algorithms.

Adding timestamps to log entries.

Returning meaningful exit codes for automated monitoring.

Adding unit tests.

Improving error handling and reporting.

Supporting scheduled or continuous integrity monitoring.

Security Considerations

This tool should be used as a basic file-integrity monitoring utility, not as a complete security solution.

A hash mismatch indicates that the current file contents differ from a previously trusted hash. It does not by itself prove that a file has been maliciously modified.

For meaningful integrity monitoring, the baseline hashes should be generated from a trusted system state and protected from unauthorized modification.

License

Add your preferred license here, for example:

MIT License


If this project is intended for public use, it is recommended to include a LICENSE file in the repository.