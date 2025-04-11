# Global variable
x = "Texas"

class University:
    # Class variable
    purpose = "Learning"
    
    def __init__(self, name, location, president):
        # Instance variables
        self.name = name
        self.location = location
        self.president = president
    
    def is_good(self):
        # Method using instance variables
        return self.location == "Norman"

# Demonstrate scope rules
def scope_demo():
    # Local variable
    x = "Oklahoma"
    
    class A:
        # Class variable
        x = "Oklahoma"
        
        def __init__(self):
            # Instance variable
            self.x = "Kansas"
    
    # Create instances
    a1 = A()
    a2 = A()
    
    # Demonstrate scope hierarchy
    print("Global x:", x)  # Local x shadows global x
    print("A.x (class variable):", A.x)
    print("a1.x (instance variable):", a1.x)
    print("a2.x (instance variable):", a2.x)
    
    # Demonstrate variable deletion
    del a1.x
    print("\nAfter deleting a1.x:")
    print("a1.x (now using class variable):", a1.x)
    print("a2.x (unchanged):", a2.x)

# Demonstrate University class
def university_demo():
    ou = University("University of Oklahoma", "Norman", "Joseph Harroz")
    
    print("\nUniversity Demo:")
    print("Name:", ou.name)
    print("Location:", ou.location)
    print("President:", ou.president)
    print("Purpose:", University.purpose)  # Accessing class variable
    print("Is OU good?:", ou.is_good())

if __name__ == "__main__":
    scope_demo()
    university_demo() 