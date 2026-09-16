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
 1: 1
 
Explanation: An artist can accommodate at most 1 concert or event at one time.

## UML Class Relationship Diagram
<img width="1366" height="768" alt="imagesclassRelationshipDiagram" src="https://github.com/user-attachments/assets/a648ce78-15f7-47fc-859a-e060d3276212" />


## Python Implementation
[View Python Source](classRelationships.py)

## Test Run
Before relationship: <img width="1917" height="912" alt="Screenshot 2026-09-16 201136" src="https://github.com/user-attachments/assets/f04b61a1-4e6c-413d-8a1a-0334d44ec4ec" />
After Relationship: <img width="1917" height="912" alt="Screenshot 2026-09-16 201326" src="https://github.com/user-attachments/assets/6dc0c2d7-b816-4f2e-9a18-1acf0f8b10dd" />

## Object Relationship Diagram
![Object Relationship Diagram](<img width="1366" height="768" alt="imagesobjectRelationshipDiagram" src="https://github.com/user-attachments/assets/8e162d28-48f3-431d-8a6e-e3f70e7366c0" />
)
## Analysis
### What is the association between your two classes?
Many artists or bands hold concerts in the Philippines every year; people can look up who will be performing and check if tickets are available.
### What multiplicity did you choose and why?
An artist can accommodate at least 1 concert or event.
### How did you implement the relationship in Python?
I related the two classes. I built the second class using the first class as a basis. 
### Why did you store an object reference instead of copying its data?
The data in the 1st class can be used in the 2nd class, so I just stored the 2nd inside the 1st.
### If your relationship uses many, why is a list appropriate?

## References
Google searches: 
1. how to insert a class inside a class in oop act. both must be working
<img width="1035" height="939" alt="image" src="https://github.com/user-attachments/assets/be9bca7a-268b-4464-a721-53da9ea38819" />
2. what does return do in python
<img width="1016" height="599" alt="image" src="https://github.com/user-attachments/assets/879aff03-dc94-4bbf-ad87-a91a24e0d79b" />



