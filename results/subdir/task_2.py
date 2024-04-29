from datetime import datetime
import pytz
def display_current_time(timezones):
    for timezone in timezones:
        try:
            tz = pytz.timezone(timezone)
            current_time = datetime.now(tz)
            print(f"Time in {timezone}: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")
        except pytz.exceptions.UnknownTimeZoneError:
            print(f"Error: Timezone '{timezone}' is not valid.")
if __name__ == "__main__":
    timezones = input("Enter timezones (comma-separated): ").split(',')
    display_current_time(timezones)