class OPM:
    def __init__(self, title: str, artist: str, price: float):
        self.title = title
        self.artist = artist
        self.price = price

    def get_details(self) -> str:
        return f"'{self.title}' by {self.artist} - ₱{self.price:.2f}"


class PhysicalAlbum(OPMTrack):
    def __init__(self, title: str, artist: str, price: float, packaging_type: str):
        super().__init__(title, artist, price)
        self.packaging_type = packaging_type

    def get_details(self) -> str:
        base_info = super().get_details()
        return f"{base_info} [{self.packaging_type} Edition]"


class AlbumShop:
    def __init__(self, shop_name: str):
        self.shop_name = shop_name
        self.inventory = []

    def add_to_inventory(self, track: OPMTrack):
        self.inventory.append(track)

    def display_inventory(self):
        print(f"--- {self.shop_name} Inventory ---")
        for item in self.inventory:
            print(f"- {item.get_details()}")
