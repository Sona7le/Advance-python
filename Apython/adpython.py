entered_persons = set()
rejected_persons = set()

num_persons = 5

print("Event Tracker: Enter 5 persons\n")

for i in range(num_persons):
    name = input(f"Enter name of person {i+1}: ").strip()
    
    if name in entered_persons:
        print(f"Entry rejected! {name} has already entered.")
        rejected_persons.add(name)
    else:
        print(f"Entry accepted! Welcome {name}.")
        entered_persons.add(name)

print("\n--- Event Entry Summary ---")
print(f"Persons entered successfully ({len(entered_persons)}): {', '.join(entered_persons)}")
print(f"Persons rejected ({len(rejected_persons)}): {', '.join(rejected_persons)}")
print(f"Total persons who entered: {len(entered_persons)}")
print(f"Total persons rejected / duplicate entries: {len(rejected_persons)}")
print(f"Total persons not entered: {num_persons - len(entered_persons)}")
