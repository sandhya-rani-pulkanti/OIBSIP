function convertTemp() {
    const inputTemp = parseFloat(document.getElementById("inputTemp").value);
    const inputUnit = document.getElementById("inputUnit").value;
    let result;
  
    if (isNaN(inputTemp)) {
      document.getElementById("output").innerText = "Please enter a valid number";
      return;
    }
  
    switch (inputUnit) {
      case "Celsius":
        result = `Fahrenheit: ${(inputTemp * 9/5 + 32).toFixed(2)}°F, Kelvin: ${(inputTemp + 273.15).toFixed(2)}K`;
        break;
      case "Fahrenheit":
        result = `Celsius: ${((inputTemp - 32) * 5/9).toFixed(2)}°C, Kelvin: ${((inputTemp - 32) * 5/9 + 273.15).toFixed(2)}K`;
        break;
      case "Kelvin":
        result = `Celsius: ${(inputTemp - 273.15).toFixed(2)}°C, Fahrenheit: ${((inputTemp - 273.15) * 9/5 + 32).toFixed(2)}°F`;
        break;
    }
  
    document.getElementById("output").innerText = result;
  }
  