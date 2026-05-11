# Dictionary Operations

# 1. Dictionary:
# Key-value pairs, ordered, changeable, no duplicate keys

# ===================== Examples =====================

capitals = {"USA": "Washington D.C.", "France": "Paris", "Japan": "Tokyo"}  # dictionary

# ===================== DICTIONARY OPERATIONS =====================


print(capitals["USA"])  # outputs: Washington D.C. (access value by key)
print(capitals.get("France"))  # outputs: Paris (access value by key using get method)
print(capitals.get("Germany", "Key not found"))  # outputs: Key not found (returns default value if key is not found)
print(capitals.keys())  # outputs: dict_keys(['USA', 'France', 'Japan']) (returns all keys)
print(capitals.values())  # outputs: dict_values(['Washington D.C.', 'Paris', 'Tokyo']) (returns all values)
print(capitals.items())  # outputs: dict_items([('USA', 'Washington D.C.'), ('France', 'Paris'), ('Japan', 'Tokyo')]) (returns all key-value pairs)

capitals["Germany"] = "Berlin"  # adds a new key-value pair
capitals["USA"] = "Washington"  # outputs: Washington (updates value of existing key)
del capitals["Japan"]  # outputs: {'USA': 'Washington', 'France': 'Paris'} (removes a key-value pair by key)
capitals.pop("France")  # outputs: Paris (removes a key-value pair by key and returns the value)
capitals.clear()  # outputs: {} (removes all key-value pairs)


# ===================== DICTIONARY LOOPING =====================

for key, value in capitals.items():
    print(f"{key}: {value}")  # outputs: USA: Washington (iterates through key-value pairs)


