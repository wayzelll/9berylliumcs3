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
| Artist | string | Public | Users may or need to search the music artist they're looking for
| Date | integer | Private | The date of debut of the artist is not relevant and does not need to be shown to users |
| Listeners | integer | Private | The number of listeners of the artist is not relevant and does not need to be shown to users |
## Updated UML Class Diagram
![Class Diagram](<img width="1080" height="1920" alt="OPM favorites! (1)" src="https://github.com/user-attachments/assets/a8d237aa-3ea0-409a-800b-8e0fe45dceaf" />)
## Python Implementation
[View Python Source](quarter1/classImplementation.py)
## Test Run
![Test Run](images/classTestRun.png)
## Object Diagram
![Object Diagram](images/objectDiagram.png)

## Analysis
### Why did you make your chosen attribute private?
### Which method changes the state of your object?
### How did your two objects demonstrate that instances are independent?
### What is the difference between your class diagram and your object diagram?
