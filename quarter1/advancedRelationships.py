class OPM:
    def __init__(self, title: str, artist: str, price: float):
        self.title = title
        self.artist = artist
        self.price = price

    def get_details(self) -> str:
        return f"'{self.title}' by {self.artist} - ₱{self.price:.2f}"


class PhysicalAlbum(OPM):
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

    def add_to_inventory(self, track: OPM):
        self.inventory.append(track)

    def display_inventory(self):
        print(f"--- {self.shop_name} Inventory ---")
        for item in self.inventory:
            print(f"- {item.get_details()}")


if __name__ == "__main__":
    track1 = OPM("Kathang Isip", "Ben&Ben", 150.0)
    album1 = PhysicalAlbum("Eraserheads Anthology", "Eraserheads", 500.0, "Vinyl")

    print("--- Test 1: Inheritance Output ---")
    print(track1.get_details())
    print(album1.get_details())
    print()

    shop = AlbumShop("Pinoy Beats Music Store")
    
    shop.add_to_inventory(track1)
    shop.add_to_inventory(album1)

    print("--- Test 2: Aggregation Output ---")
    shop.display_inventory()
