# Advanced Class Relationships
## Previous Activities
[classAttrib](./quarter1/classAttributesMethods.md)

[classRel](./quarter1/classRelationships.md)
## Existing System Description:
1. What classes currently exist in your system?
  Class 1: OPM; Class 2: SpoTickets
2. What problem or limitation exists in your current design?
    ● repeated attributes;
    ● repeated methods;
    ● temporary actions incorrectly modeled.
Explain:
## Inheritance Relationship
  Parent: OPM
  Child: Album shop
Explanation: An album shop will sell different kinds if OPM in its store.
## Inheritance UML
![Inheritance](<img width="1080" height="1350" alt="imagesinheritanceDiagram" src="https://github.com/user-attachments/assets/0cf78cd1-1578-4d3f-be4a-7df48aff311a" />
)
## Composition/Aggregation
        Album shop
            ◆
            |
          Album
Relationship: Strong HAS-A Relationship
Explanation: If Customers don't exist, an Album shop would just shut down
## Advanced UML Diagram
![Advanced UML](<img width="1080" height="1350" alt="advancedClassDiagram" src="https://github.com/user-attachments/assets/0c59ec7e-3f2b-4c7f-8157-2311ba220809" />
)
## Python Implementation
[Source Code](./quarter1/advancedRelationships.py)
## Test Run
![Test](<img width="1917" height="810" alt="Screenshot 2026-09-28 185802" src="https://github.com/user-attachments/assets/167410b6-4244-40fd-97e0-3f74a7fafede" />
)
## Object Diagram
![Objects](<img width="1080" height="1350" alt="advancedObjectDiagram" src="https://github.com/user-attachments/assets/7e00cde0-305f-4b8b-8701-b11585dfd5f4" />
)

## Reflection
Answers:
1. Why did you choose your inheritance relationship? Explain why your child class is a type of your parent class.
   I chose PhysicalAlbum as a child class of OPM because it shares common attributes such as title, artist, and base price, satisfying the IS-A relationship. 

2. How did inheritance reduce duplicate code? Identify attributes or methods that were reused.
   Inheritance allowed PhysicalAlbum to inherit common attributes and methods from OPM. This eliminated redundancy and kept the center in the parent class.

3. Why is your HAS-A relationship Composition or Aggregation? Explain the lifecycle relationship between the two objects.
   It is an Aggregation because OPM cannot exist without the Album shop. In a way, there will be no sold songs without the shop itself.

4. What is the difference between Association from Part III and the advanced relationship you
implemented?
   On Part III, we focused more on expanding the class, creating a child class. Then, on Part IV, we focused on advancing those classes.

5. How does your design follow the DRY principle?
   The design follows DRY principles by centralizing data and logic within OPM. This avoids duplicate attribute definitions across child classes.
