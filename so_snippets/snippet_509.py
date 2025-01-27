# Extracted from https://stackoverflow.com/questions/33225947/can-a-website-detect-when-you-are-using-selenium-with-chromedriver
var options = new ChromeOptions();

options.AddExcludedArguments(new List<string>() { "enable-automation" });

var driver = new ChromeDriver(ChromeDriverService.CreateDefaultService(), options);

