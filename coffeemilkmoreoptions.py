def main():
    print("🌍 Daily Habits Environmental Impact Calculator 🌍\n")

    # Ask for daily habits
    coffees = int(input("How many coffees do you drink per day? "))
    km_driven = float(input("How many kilometres do you drive per day? "))
    meat_meals = int(input("How many meat-based meals do you eat per day? "))
    fast_fashion = int(input("How many fast fashion items do you buy per month? (approx) "))
    shower_minutes = int(input("How many minutes do you usually shower? "))

    # Ask about milk choice
    print("\nWhat type of milk do you usually drink in your coffee?")
    print("Options: almond, oat, soy, cow")
    milk_choice = input("Enter your choice: ").lower()

    # Environmental data (average estimates per litre of milk)
    milk_data = {
        "almond": {"water": 371, "co2": 0.14},
        "oat": {"water": 48, "co2": 0.18},
        "soy": {"water": 28, "co2": 0.09},
        "cow": {"water": 628, "co2": 3.2}
    }

    # Simplified daily activity impacts
    coffee_base_water = coffees * 130  # litres of water per coffee (farm to cup)
    car_emissions = km_driven * 0.21  # kg CO2 per km (average petrol car)
    meat_emissions = meat_meals * 2.5  # kg CO2 per meal
    fast_fashion_water = fast_fashion * 2700 / 30  # litres/day
    shower_water = shower_minutes * 9  # litres per minute of shower

    # Calculate milk impact per coffee (assuming 0.2L milk per coffee)
    milk_per_coffee = 0.2

    if milk_choice in milk_data:
        milk_water = milk_data[milk_choice]["water"] * milk_per_coffee * coffees
        milk_emissions = milk_data[milk_choice]["co2"] * milk_per_coffee * coffees
    else:
        milk_choice = "unknown"
        milk_water = 0
        milk_emissions = 0
        print("\n⚠️ Invalid milk choice. Defaulting to 0 impact for milk.")

    # Add milk impact to total coffee footprint
    total_coffee_water = coffee_base_water + milk_water

    # Display estimated daily impact
    print("\n--- 🌱 Estimated Daily Environmental Impact ---")
    print(f"☕ Coffee ({coffees} cups with {milk_choice} milk):")
    print(f"   → ~{total_coffee_water:.0f} litres of water")
    print(f"   → ~{milk_emissions:.2f} kg CO₂ from milk")

    print(f"🚗 Driving: {km_driven} km → ~{car_emissions:.2f} kg CO₂")
    print(f"🥩 Meat meals: {meat_meals} → ~{meat_emissions:.2f} kg CO₂")
    print(f"👕 Fast fashion: {fast_fashion} items/month → ~{fast_fashion_water:.0f} litres water/day")
    print(f"🚿 Showers: {shower_minutes} minutes → ~{shower_water:.0f} litres of water")

    # Milk comparison table
    print("\n🥛 Milk Environmental Impact (per litre):")
    print("{:<10} {:<20} {:<15}".format("Milk Type", "Water Use (L)", "CO₂ (kg)"))
    print("-" * 40)
    for milk, data in milk_data.items():
        print("{:<10} {:<20} {:<15}".format(milk.capitalize(), data["water"], data["co2"]))

    # Detailed environmental review
    print("\n🌿 Environmental Impact Overview by Milk Type\n")

    print("🐄 Cow’s Milk:")
    print("Negatives:")
    print("- Methane from enteric fermentation (cow digestion) contributes significantly to greenhouse gases.")
    print("- Manure releases methane and nitrous oxide, both powerful greenhouse gases.")
    print("- Requires large amounts of land and water for grazing and feed production.")
    print("- Manure and fertiliser runoff can pollute waterways, causing algal blooms and ecosystem harm.")
    print("Advantages:")
    print("- Technological improvements have reduced land use by 90%, feed by 77%, and water by 65% per glass since the 1950s.")
    print("- Innovations like SeaFeed™ (seaweed-based feed) can reduce methane emissions from cattle.")
    print("- Cow’s milk remains a key source of protein, calcium, and essential nutrients.")

    print("\n🌱 Soy Milk:")
    print("Negatives:")
    print("- Large-scale soy farming can contribute to deforestation, especially in the Amazon.")
    print("- Intensive farming may reduce biodiversity and degrade soil due to pesticides and fertilisers.")
    print("Advantages:")
    print("- Requires 95% less land and water than dairy milk.")
    print("- Produces significantly lower greenhouse gas emissions.")
    print("- Soy crops can improve soil fertility through nitrogen fixation.")

    print("\n🌳 Almond Milk:")
    print("Negatives:")
    print("- Almond trees are water-intensive, with most production in drought-prone California.")
    print("Advantages:")
    print("- Very low greenhouse gas emissions.")
    print("- Almond trees absorb CO₂, helping offset some emissions.")
    print("- Requires much less land than dairy milk.")

    print("\n🌾 Oat Milk:")
    print("Negatives:")
    print("- Some conventional oat farms use pesticides like glyphosate, which can impact soil health.")
    print("Advantages:")
    print("- Produces considerably fewer greenhouse gas emissions than dairy milk.")
    print("- Requires significantly less water than dairy or almond milk.")
    print("- Often sourced from regions with lower environmental strain, such as Northern Europe.")

    # Statistics and insights
    print("\n📊 Quick Facts:")
    print("- Cow’s milk emits over 3 kg CO₂ per litre — roughly 35x higher than soy milk.")
    print("- Almond milk uses about 13x more water than soy milk.")
    print("- Switching from cow’s to oat milk for 2 coffees/day can save ~200 L of water per week.")
    print("- Cutting one meat meal per day reduces CO₂ by ~900 kg/year — equivalent to 3,600 km less driving.")

    # Total summary
    total_water = total_coffee_water + fast_fashion_water + shower_water
    total_emissions = car_emissions + meat_emissions + milk_emissions

    print("\n--- 🌏 Total Daily Summary ---")
    print(f"💧 Total water use: ~{total_water:.0f} litres/day")
    print(f"💨 Total CO₂ emissions: ~{total_emissions:.2f} kg/day")

    print("\nRemember: Small daily choices add up to big impacts! 🌱")
    print("""💪 Ways You Can Make a Difference  

Your daily choices matter — even small changes can reduce your environmental footprint and inspire others to do the same.  

☕ Coffee  
- Bring a reusable cup instead of disposable ones.  
- Choose plant-based milk or support local cafés that prioritise sustainable sourcing.  

🚗 Transport  
- Walk, cycle, or use public transport for short trips.  
- Carpool with friends or co-workers.  
- Combine errands to reduce kilometres.  

🍔 Food Choices  
- Swap one or two meat meals each week for plant-based options.  
- Buy local, seasonal produce.  
- Reduce food waste by planning meals and using leftovers.  

👗 Fashion  
- Buy second-hand or from ethical brands.  
- Avoid fast fashion and host clothing swaps.  

🚿 Water & Energy  
- Keep showers under 5 minutes.  
- Turn off taps when brushing teeth or washing dishes.  
- Use cold laundry cycles and air-dry clothes.  
""")

if __name__ == "__main__":
    main()