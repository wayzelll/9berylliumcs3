# Class Relationships: Association and Multiplicity
## Previous Work
[Part I - Classes and Objects](./quarter1/classObjectUML.md)
[Part II - Class Attributes and Methods](./quarter1/classAttributesMethods.md)
## Existing Class
Class: OPM: Original Pinoy Music

Description: This class shows different examples of OPM. It includes the music genre, release date, and total number of listeners.
## New Related Class
Class: Concert Availability: SpoTickets

Description: This subclass shows the availability of concerts in the Philippines. 
## Association
Relationship: OPM HAS Concert Availability

Explanation: Many artists or bands hold concerts in the Philippines every year; people can look up who will be performing and check if tickets are available.
## Multiplicity
 1: Many
 
Explanation: A concert availability tracker is a whole system; therefore, many functions or objects can happen in it.

## UML Class Relationship Diagram
<img width="1366" height="768" alt="imagesclassRelationshipDiagram" src="https://github.com/user-attachments/assets/a648ce78-15f7-47fc-859a-e060d3276212" />


## Python Implementation
[View Python Source](classRelationships.py)

## Test Run
![Relationship Test Run](images/relationshipTestRun.png)
## Object Relationship Diagram
![Object Relationship Diagram](images/objectRelationshipDiagram.png)
## Analysis
### What is the association between your two classes?
Many artists or bands hold concerts in the Philippines every year; people can look up who will be performing and check if tickets are available.
### What multiplicity did you choose and why?
A concert availability tracker is a whole system; therefore, many functions or objects can happen in it.
### How did you implement the relationship in Python?
I related the two classes. I worked with the second class by using the code on the 1st as basis. 
### Why did you store an object reference instead of copying its data?
The data in the 1st class can be used in the 2nd class so I just stored the 2nd inside the 1st.
### If your relationship uses many, why is a list appropriate?
