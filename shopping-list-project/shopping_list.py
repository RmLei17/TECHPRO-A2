# Shopping List Program

# Step 1: Let the user input up to 5 items
shopping_list = []
print("Enter up to 5 items to buy:")

for i in range(5):
    item = input("> ").strip()
    shopping_list.append(item)

# Step 2: Show the shopping list
print("\nYour shopping list:")
print(", ".join(shopping_list))
print(f"\nYou entered {len(shopping_list)} items.\n")

# Step 3: Search feature
search_item = input("Search for an item: ").strip().lower()

if search_item in [item.lower() for item in shopping_list]:
    print(f"✅ {search_item} is in your shopping list!")
else:
    print(f"❌ {search_item} is NOT in your shopping list.")
