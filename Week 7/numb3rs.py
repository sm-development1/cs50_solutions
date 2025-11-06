import re

def validate(ip):
    pattern = r"^(?:[0-9]{1,2}|1[0-9]{2}|2[0-4][0-9]|25[0-5])(?:\.(?:[0-9]{1,2}|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}$"
    return re.match(pattern, ip) is not None

def main():
    print(validate(input("IPv4 Address: ")))

if __name__ == "__main__":
    main()
