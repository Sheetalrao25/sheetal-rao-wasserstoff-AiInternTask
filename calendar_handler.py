# calendar_handler.py

from credentials import get_calendar_service  # ✅ make sure the file is credentials.py
from datetime import datetime, timedelta
import pytz

def create_google_calendar_event(event_details):
    service = get_calendar_service()

    try:
        start_time_str = event_details['start_time']
        end_time_str = event_details.get('end_time')  # Optional

        # Parse datetime
        start_time = datetime.strptime(start_time_str, "%Y-%m-%d %H:%M")
        end_time = (
            datetime.strptime(end_time_str, "%Y-%m-%d %H:%M")
            if end_time_str
            else start_time + timedelta(hours=1)  # default to 1 hour event
        )

        # Set timezone
        timezone = "Asia/Kolkata"  # Change if you're in a different timezone
        start_time = pytz.timezone(timezone).localize(start_time)
        end_time = pytz.timezone(timezone).localize(end_time)

        # Construct event
        event = {
            'summary': event_details['summary'],
            'location': event_details.get('location', ''),
            'description': event_details.get('description', ''),
            'start': {
                'dateTime': start_time.isoformat(),
                'timeZone': timezone,
            },
            'end': {
                'dateTime': end_time.isoformat(),
                'timeZone': timezone,
            },
        }

        created_event = service.events().insert(calendarId='primary', body=event).execute()
        print(f"✅ Event created: {created_event.get('htmlLink')}")

    except Exception as e:
        print("❌ Failed to create event:", str(e))
