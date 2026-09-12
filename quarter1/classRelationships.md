# Class Relationships: Association and Multiplicity
## Previous Work
[Part I - Classes and Objects](./quarter1/classObjectUML.md)
[Part II - Class Attributes and Methods](./quarter1/classAttributesMethods.md)
## Existing Class
Class: OPM: Original Pinoy Music
Description: This class shows different examples of OPM. It includes the music genre, date released, and total number of listeners.
## New Related Class
Class: Concert Availability: SpoTickets
Description: This sub-class shows the availability of concerts in the Philippines. 
## Association
Relationship: OPM HAS Concert Availability
Explanation: Many artists or bands hold concerts in the Philippines every year; people can look up which will be performing, and check if tickets are abailable.
## Multiplicity
Multiplicity: 1 : Many
Explanation: A concert availability tracker is a whole system, therefore, many functions or objects can happen in it.
## UML Class Relationship Diagram
![Class Relationship Diagram](./<img width="1366" height="768" alt="imagesclassRelationshipDiagram" src="https://github.com/user-attachments/assets/81b832ff-22de-4632-af80-26697befd4fd" />)
## Python Implementation
[View Python Source](classRelationships.py)
## Test Run
![Relationship Test Run](images/relationshipTestRun.png)
## Object Relationship Diagram
![Object Relationship Diagram](images/objectRelationshipDiagram.png)
## Analysis
### What is the association between your two classes?
### What multiplicity did you choose and why?
### How did you implement the relationship in Python?
### Why did you store an object reference instead of copying its data?
### If your relationship uses many, why is a list appropriate?
