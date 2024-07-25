#task1
''' "Itinerary 1: Alice - From New York to London
 Itinerary 2: Bob - From Tokyo to San Francisco"
 '''
def format_itineraries(itineraries):
    return "\n".join(
    [f"Itinerary {i +1}: {traveler_name} - From {origin} to {destination}" 
     for i, (traveler_name, origin, destination) in enumerate(itineraries)]
)
itineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Franciso")]
result = format_itineraries(itineraries)
print(result)