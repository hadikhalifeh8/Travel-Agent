from datetime import datetime

def format_datetime(value):
    try:
        dt = datetime.strptime(value, "%Y-%m-%d %H:%M")
        return dt.strftime("%b-%d, %Y | %I:%M %p")
    except:
        return "N/A"
