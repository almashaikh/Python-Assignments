from datetime import datetime, timedelta

def longest_streak(date_strings):
    dates = {
        datetime.fromisoformat(date_str).date()
        for date_str in date_strings
    }

    if not dates:
        return 0
    
    #sort the dates
    sorted_dates = sorted(dates)

    longest = 1
    current = 1

    #checking for consecutive dates
    for i in range(1, len(sorted_dates)):
        if sorted_dates[i] == sorted_dates[i-1] + timedelta(days=1):
            current += 1
        else:
            current = 1

        longest = max(longest, current)
    
    return longest

dates = [
    "2026-07-01",
    "2026-07-02",
    "2026-07-04",
    "2026-07-05",
    "2026-07-06",
]

print(longest_streak(dates))