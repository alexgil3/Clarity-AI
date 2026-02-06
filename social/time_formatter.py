def format_time(timestamp, now):
    diff = now - timestamp
    seconds = int(diff.total_seconds())

    if seconds < 60:
        unit = "second" if seconds == 1 else "seconds"
        return f"{seconds} {unit} ago"

    minutes = seconds // 60
    if minutes < 60:
        unit = "minute" if minutes == 1 else "minutes"
        return f"{minutes} {unit} ago"

    hours = minutes // 60
    if hours < 24:
        unit = "hour" if hours == 1 else "hours"
        return f"{hours} {unit} ago"

    days = hours // 24
    unit = "day" if days == 1 else "days"
    return f"{days} {unit} ago"
