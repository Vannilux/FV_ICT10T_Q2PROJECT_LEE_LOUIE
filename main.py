from pyscript import document

list1 = ["Edrian Correa","Cheree Mendoza","Alexa Cunanan","Carlos Borromeo","Jericho Magsalin","Eran Diaz","Louie Lee"]

def member_check(e):
    first_name = document.getElementById("input1").value.strip().title()
    last_name = document.getElementById("input2").value.strip().title()
    full_name = first_name + " " + last_name

    message = {
        True: "congratulations! You have been accepted into the SOCSCI Club!",
        False: "sorry, you have not been accepted into the SOCSCI Club."
    }[full_name in list1]

    document.getElementById("result").innerText = full_name + ", " + message

def add_member(e):
    first_name = document.getElementById("input1").value.strip().title()
    last_name = document.getElementById("input2").value.strip().title()
    full_name = first_name + " " + last_name #combine fname and lname to create full name

    Grade7 = {"Li Hansen", "Samuel Lee", "Maria Cruz"}
    Grade8 = {"Tian Gotsap", "Earl Jung", "Jack Ere", "Yosef Kim"}
    Grade9 = {"Akira Masato", "Kim Il-Park"}
    Grade10 = {"Krum Despina", "Sofia Martinez", "John Sakazuki", "Nakamura Hiroshi"}

    student_list = Grade7|Grade8|Grade9|Grade10|{full_name} # combines list of all students in the club
    document.getElementById("result").textContent = f"Total members: {len(student_list)}"

    student_list = "<br>".join(sorted(student_list)) # lists and sorts the names of the students in the club by alphabetical order

    document.getElementById("result").innerHTML += f"<br>{student_list}" #add the sorted list of students to the result div

from pyscript import document,display
# Elements
# Dictionary with information about elements
# Element Name: Symbol, Element, Atomic Number, Atomic Mass
elements = {
    "Hydrogen": ("H", 1, 1.008),
    "Helium": ("He", 2, 4.0026),
    "Carbon": ("C", 6, 12.011),
    "Nitrogen": ("N", 7, 14.007),
    "Oxygen": ("O", 8, 15.999),
    "Fluorine": ("F", 9, 18.998),
    "Neon": ("Ne", 10, 20.180),
    "Phosphorus": ("P", 15, 30.974),
    "Sulfur": ("S", 16, 32.06),
    "Chlorine": ("Cl", 17, 35.45),
    "Argon": ("Ar", 18, 39.948),
    "Selenium": ("Se", 34, 78.971),
    "Bromine": ("Br", 35, 79.904),
    "Krypton": ("Kr", 36, 83.798),
    "Iodine": ("I", 53, 126.90),
    "Xenon": ("Xe", 54, 131.29),
    "Radon": ("Rn", 86, 222.0),
    "Gavinium": ("Gm", 15, 2011.02),  # small easter egg, not a real element
}
#          Key     : Value
# Create a function to search for an element
def search_element(e):
    # Get the input from HTML
    Element1 = document.getElementById("element1").value
    # Retrieve information from the dictionary
    result = elements.get(Element1, ("Element not found", "-", "-"))
    # Display of result
    document.getElementById("symbol").innerText = Element1
    document.getElementById("element").innerText = result[0]
    document.getElementById("ANUM").innerText = result[1]
    document.getElementById("AMASS").innerText = result[2]

   
        