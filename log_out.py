def log_out(text):
    with open('./log/localhost_access.log', 'a') as f:
        f.write(text + "\n")
    return "ok"