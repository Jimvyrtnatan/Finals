def measurement_converter():
  units = {
    'mm to cm': lambda x: x / 10,
    'cm to mm': lambda x: x * 10,
    'ft to m': lambda x: x / 3.28,
    'm to ft': lambda x: x * 3.28,
    'kg to lbs': lambda x: x * 2.20462,
    'lbs to kg': lambda x: x / 2.20462,
  }

  print("Measurement Converter")
  print("----------------------")

  while True:
    print("\nAvailable Conversions:")
    for key in units:
      print(key)  # Simpler presentation of available conversions

    choice = input("\nEnter the conversion you'd like to perform (or 'q' to quit): ")
    if choice.lower() == 'q':  # Handle 'q' in any case
      break

    if choice not in units:
      print("Invalid choice. Please try again.")
    else:
      try:
        value = float(input("Enter the value to convert: "))
        result = units[choice](value)
        print(f"{choice}: {value:.2f} -> {result:.2f}")  # Format results with 2 decimal places
      except ValueError:
        print("Invalid input. Please enter a number.")

  print("\nThank you for using the Measurement Converter!")

measurement_converter()
