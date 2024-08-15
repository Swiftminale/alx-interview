#!/usr/bin/python3
import sys

def print_metrics(total_file_size, status_code_counts):
    print("File size: {}".format(total_file_size))
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print("{}: {}".format(code, status_code_counts[code]))

if __name__ == "__main__":
    codes_count = {'200': 0, '301': 0, '400': 0, '401': 0,
                   '403': 0, '404': 0, '405': 0, '500': 0}
    file_size_total = 0
    count = 0

    try:
        for line in sys.stdin:
            try:
                parts = line.split()
                if len(parts) < 9:
                    continue

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

    except KeyboardInterrupt:
        print_metrics(file_size_total, codes_count)
        raise

    print_metrics(file_size_total, codes_count)

