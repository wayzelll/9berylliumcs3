class SpoTickets:
    def __init__(self, event: str, artist: str, date: int, login_date: int):
        self.event = event
        self.artist = artist
        self.date = date
        self.__login_date = login_date

    def search(self):
        print(f"Searching tickets for event: {self.event} featuring {self.artist}...")

    def display_info(self):
        print(f"Event: {self.event} | Artist: {self.artist}")

    def display_date(self):
        print(f"Performance Date: {self.date}")

    def __display_lg_date(self):
        print(f"Log-in Date: {self.__login_date}")


if __name__ == "__main__":

    ticket_system = SpoTickets(
        event="Gabi ng Lambing",
        artist="Silent Sanctuary",
        date=20261025,
        login_date=20260914
    )
    
    ticket_system.search()
    ticket_system.display_info()
    ticket_system.display_date()
