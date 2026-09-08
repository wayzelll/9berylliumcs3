# Class Attributes and Methods
## Previous Design
Link to my previous activity:
[classObjectUML.md](./classObjectUML.md)
## Design Revision
Describe any changes made to your original class.
## Visibility Decisions
| Attribute | Data Type | Visibility | Reason |
|---|---|---|---|
| Genre | string | Public | Users may or need to search the music genre they're looking for |
| Artist | string | Public | Users may or need to search the music artist they're looking for
| Date | integer | Private | The date of debut of the artist is not relevant and does not need to be shown to users |
| Listeners | integer | Private | The number of listeners of the artist is not relevant and does not need to be shown to users |
## Updated UML Class Diagram
![Class Diagram](images/classDiagramSG5.png)
## Python Implementation

[View Python Source](classImplementation.py)
## Test Run
![Test Run](images/classTestRun.png)
## Object Diagram
![Object Diagram](images/objectDiagram.png)
## Analysis
### Why did you make your chosen attribute private?
### Which method changes the state of your object?
### How did your two objects demonstrate that instances are independent?
### What is the difference between your class diagram and your object diagram?
