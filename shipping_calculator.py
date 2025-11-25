lstCompanies = ['Universal Package Sorters (UPS)', 'Federation Excelsior (FedEx)', 'Dependable, Honorable Logisticians (DHL)']
lstFlatFee = [5.74, 3.59, 15.47]
lstRatePerPound = [1.59, 2.05, 1.07]
lstOversizePackageDimensions = [165, 195, 215]
lstOverchargeFee = [0.2, 0.22, 0.1]

def calcBestCompany(fullPackageDimensions, packageWeightInput):
  min_price = float(9999)
  best_company_name = ""

  # Loop through all available companies
  for i in range(len(lstCompanies)): 
    company_name = lstCompanies[i]
    flatFee = lstFlatFee[i]
    ratePerPound = lstRatePerPound[i]
    overchargeFee = lstOverchargeFee[i]
    
    # Calculate base cost
    totalAmount = flatFee + (packageWeightInput * ratePerPound)
    
    # Check for oversize charge
    if (fullPackageDimensions >= lstOversizePackageDimensions[i]):
      extraCharge = packageWeightInput * ratePerPound * overchargeFee
      totalAmount = totalAmount + extraCharge
        
    # Round the final calculated price
    current_shipment_price = round(totalAmount, 2)
    
    # Compare current price to the minimum price found so far
    if current_shipment_price < min_price:
      min_price = current_shipment_price
      best_company_name = company_name

  return best_company_name, min_price

def shipPackage():
  packageLengthInput = 0
  packageWidthInput = 0
  packageHeightInput = 0
  packageWeightInput = 0.0
  
  # Flag to check if input was successful
  input_successful = False

  try:
    print("\nPlease enter the package dimensions:")
    
    # All inputs attempted in a single try block
    packageLengthInput = int(input("Enter Length (inches): "))
    packageWidthInput = int(input("Enter Width (inches): "))
    packageHeightInput = int(input("Enter Height (inches): "))
    packageWeightInput = float(input("Enter Package Weight (pounds): "))
    
    # Ensure numbers are logical
    if (packageLengthInput > 0 and packageWeightInput > 0 and packageHeightInput > 0 and packageWeightInput > 0):
      input_successful = True
        
  # User enters a non number
  except ValueError:
    print("\nInvalid input! All inputs must be numeric (whole numbers for dimensions).")

  # If the user enters all valid values
  if input_successful:
    fullPackageDimensions = packageWidthInput + packageLengthInput + packageHeightInput
    
    print("\nWhich company would you like to ship through?")
    
    # Display options
    for i in range(len(lstCompanies)):
      company_name = lstCompanies[i]
      print(f"{i + 1}: {company_name}")
    print("4: Calculate Best Option Automatically")
    
    # Company selection
    userCompanyOption = 0
    
    while userCompanyOption != -1: 
      try:
        # Get input from the user
        userCompanyOption = int(input("\nEnter your company selection: "))
        
        # Check if the selection is a valid company number (1, 2, or 3)
        if 1 <= userCompanyOption <= len(lstCompanies):
          
          # Adjust user input (1, 2, 3) to list index (0, 1, 2)
          company_index = userCompanyOption - 1
          
          # Store associated values based on selected company
          flatFee = lstFlatFee[company_index]
          ratePerPound = lstRatePerPound[company_index]
          overchargeFee = lstOverchargeFee[company_index]
          
          # Calculate Total Amount and round
          totalAmount = flatFee + (packageWeightInput * ratePerPound)
          totalAmount = round(totalAmount, 2)
          
          # Extra charge if oversize
          if (fullPackageDimensions >= lstOversizePackageDimensions[company_index]):
            extraCharge = packageWeightInput * ratePerPound * overchargeFee
            totalAmount = round(totalAmount + extraCharge, 2)
              
          print(f"Package shipped! Total price: ${totalAmount}")
          
          # Exit the while loop after successful selection
          userCompanyOption = -1
            
        # Handle Automatic Calculation option
        elif userCompanyOption == 4:
          best_company, min_cost = calcBestCompany(fullPackageDimensions, packageWeightInput)
          print(f"Package shipped! The best option is {best_company} with a total cost of ${min_cost:.2f}.")
          
          # Exit the while loop after successful selection
          userCompanyOption = -1
          
        # User did not enter valid number (1-4)  
        else:
          print(f"Invalid choice. Please select a number between 1 and 4.")
          
      # Catch non-numeric input for the selection
      except ValueError:
        print("\nInvalid input! Please enter a valid choice number.")
          
      # Invalid company number
      except IndexError:
        # Initial validation failed to catch an out of bounds number
        print(f"Invalid choice. Please select a number between 1 and 4.")
            
  else:
    # Code block runs if the initial dimension input failed
    print("\nInput failed. Cannot proceed with calculations.")

  return

def displayCompanies():
  # Loop through each company
  for i in range(len(lstCompanies)):
    
    # Store associated values        
    company_name = lstCompanies[i]
    flat_fee = lstFlatFee[i]
    rate_per_pound = lstRatePerPound[i]
    oversize_package_dimensions = lstOversizePackageDimensions[i]
    overcharge_fee = lstOverchargeFee[i]
    
    # Output companies to user
    print(
      f"Company: {company_name} | Flat Fee: ${flat_fee} | Rate/lb: ${rate_per_pound} | Oversize Package Size (inches): ${oversize_package_dimensions} | Overcharge Fee: {(overcharge_fee * 100):.2f}%"
    )

def main():
  userInput = 0
  print("Welcome to Jake's Shipping Calculator!")
  while (userInput != -1):
    try:
      print("\nOptions:\n")
      print("1. Display Companies")
      print("2. Ship Package")
      userInput = int(input("\nEnter your choice (-1 to exit): "))
      if (userInput == 1):
        displayCompanies()
      if (userInput == 2):
        shipPackage()
    except ValueError:
        print("\nInvalid input! Please enter a valid choice number.")
  
  print("\nExiting program.")
  return
  
main()