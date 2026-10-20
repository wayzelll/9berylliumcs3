class Publication: # creates class

    def __init__(self, title, author, ): # defines attributes
        self._title = title 
        self._author = author
    def display_info(self): 
        print (f"Title: {self._title}")
        print (f"Author: {self._author}")
        
class Book(Publication): # creates class

    def __init__(self, title, author,pageNo): # defines attributes
        self._title = title
        self._author = author
        self._pages = pageNo
        
    def getPages(self):
        return self._pages # returns the value

    def setPages(self, pageNo):# defines attributes
        if pageNo < 0:
            print("Number of pages must be positive.")
        else:
            self._pages = pageNo
    def display_info(self): # defines attributes
        print (f"Title: {self._title}")
        print (f"Author: {self._author}")
        print (f"Number of pages: {self._pages}")

class Magazine(Publication): # creates class

    def __init__(self, title, author, issueNo): # defines attributes
        self._title = title
        self._author = author
        self._issues = issueNo
        
    def get_issue_number (self): # defines attributes
        return self._issues # returns the value
        
    def display_info(self): # defines attributes
        print (f"Title: {self._title} ")
        print (f"Author: {self._author}")
        print (f"Issue number: {self._issues}")


#Samples
pub1 = Publication ("Journal of Experimental Psychology", "Ratcliff, R. & Van Dongen, H.")
book1 = Book ("The Hobbit", "J.R.R. Tolkien", 310)
mag1 = Magazine ("National Geographic", "Various Authors", 202)


print("Publication Information:")
pub1.display_info()

print("\nBook Information:")
book1.setPages(-310)
book1.display_info()
print(book1.getPages())

print("\nMagazine Information:")
mag1.display_info()
print(mag1.get_issue_number())


print("\nMagazine Information:")
mag1.display_info()
print(mag1.get_issue_number())
