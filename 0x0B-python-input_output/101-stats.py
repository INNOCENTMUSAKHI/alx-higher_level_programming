#!/usr/bin/env python3

import sys

def print_info(file_size, status_codes):
    print(f"File size: {file_size}")

    for code, count in sorted(status_codes.items()):
        if count > 0:
            print(f"{code}: {count}")

def main():
    status_codes = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
    }

    line_count = 0
    file_size = 0

    for line in sys.stdin:
        try:
            _, _, _, status_code, _, size, *_ = line.split()
            status_codes[status_code] += 1
            file_size += int(size)
        except (ValueError, KeyError):
            pass

        line_count += 1

        if line_count % 10 == 0:
            print_info(file_size, status_codes)

    print_info(file_size, status_codes)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
