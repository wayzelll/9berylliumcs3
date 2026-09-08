# Class Attributes and Methods
## Previous Design
Link to my previous activity:
[classObjectUML.md](./classObjectUML.md)
## Design Revision
No major changes were needed from my original design.
## Visibility Decisions
| Attribute | Data Type | Visibility | Reason |
|---|---|---|---|
| Genre | string | Public | Users may or need to search the music genre they're looking for |
| Artist | string | Public | Users may or need to search for the music artist they're looking for
| Date | integer | Private | The date of debut of the artist is not relevant and does not need to be shown to users |
| Listeners | integer | Private | The number of listeners of the artist is not relevant and does not need to be shown to users |
## Updated UML Class Diagram
<img width="1080" height="1920" alt="OPM favorites! (1)" src="https://github.com/user-attachments/assets/a8d237aa-3ea0-409a-800b-8e0fe45dceaf" />
## Python Implementation
[View Python Source] [(./quarter1/classImplementation.py)](https://github.com/wayzelll/9berylliumcs3/blob/main/quarter1/classImplementation.py)
## Test Run
<img width="1917" height="816" alt="Screenshot 2026-09-08 205427" src="https://github.com/user-attachments/assets/6532cea4-5f0f-427b-9294-b5f50130de11" />
)
## Object Diagram
![Object Diagram](./images/objectDiagram.png)

## Analysis
### Why did you make your chosen attribute private?
The release date and the number of listeners to the artist or genre are not relevant
### Which method changes the state of your object?
The Delete() method, because it doesn't just change it---it deletes the value in the class.
### How did your two objects demonstrate that instances are independent?
The attributes have their own data type and visibility, which makes them unique and independent.
### What is the difference between your class diagram and your object diagram?
The class diagram shows the overall structure, while the object diagram focuses on its own.
