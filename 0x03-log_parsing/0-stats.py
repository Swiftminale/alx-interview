#!/usr/bin/python3
import sys
import re
import signal

def print_metrics(total_file_size, status_code_counts):
    print("File size: {}".format(total_file_size))
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print("{}: {}".format(code, status_code_counts[code]))

def handle_interrupt(signal, frame):
    print_metrics(file_size_total, codes_count)
    sys.exit(0)

signal.signal(signal.SIGINT, handle_interrupt)

codes_count = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
file_size_total = 0
count = 0

log_line_pattern = re.compile(r'^\S+ - \[\S+ \S+\] "GET /projects/260 HTTP/1.1" \d{3} \d+$')

for line in sys.stdin:
    try:
        if not log_line_pattern.match(line):
            continue

        parts = line.split()
        status_code = parts[-2]
        file_size = int(parts[-1])

        if status_code in codes_count:
            codes_count[status_code] += 1

        file_size_total += file_size
        count += 1

        if count == 10:
            print_metrics(file_size_total, codes_count)
            count = 0

    except (ValueError, IndexError):
        continue

print_metrics(file_size_total, codes_count)

