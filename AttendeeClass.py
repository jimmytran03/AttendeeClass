class Attendee:
    current_attendees = 0

    def __init__(self, name: str):
        self.name = name
        Attendee.current_attendees += 1
        print(f"Welcome {self.name}! Current attendees: {Attendee.current_attendees}")

    @staticmethod
    def leave_meeting():
        if Attendee.current_attendees > 0:
            Attendee.current_attendees -= 1
            print(f"Someone left. Current attendees: {Attendee.current_attendees}")
        else:
            print("No attendees left to leave.")

# Example usage
attendee1 = Attendee("John")
attendee2 = Attendee("Jane")
Attendee.leave_meeting()
