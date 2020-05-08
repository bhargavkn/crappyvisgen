def log_message(msg):
    print("[+] {}".format(msg))


def log_task_init(msg):
    print("[+] {} ...".format(msg))


def log_task_end(msg):
    print("[+] {} ... ok".format(msg))


def log_error(msg):
    print("[*] {} ...".format(msg))
