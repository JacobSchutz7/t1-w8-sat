# T1-W8_SAT

# Virtual Environment
- Creates an isolated envrionment for your projects ensuring each project has its own dependencies. 

# Testing
- A method for confirming whether the application works as intended. 
- Helps catch bugs early and ensures your code runs smoothly. 

## Types of Testing
- Manual vs Automated
	- Manual: when a person manually performs tasks to test output or behaviour. 
	- Automated: programmed tests, also called scripts, to automatically perform tasks without human involvement. 
- Unit Testing: tests that target specific components, functions, or methods. 
- Integration Testing: tests that measure compatibility of multiple files, packages, and modules. 
- Chaos Testing: tests that try to break a program to see how it behaves when errors are raised. 
- Stress Testing: testing a high volume of data or inputs to see how stable the program is under those conditions. 
- End to End/Acceptance Testing: tests aimed at ensuring the final version, or near the final versions, works as intended. 

## pytest
- Powerful and user-friendly testing framework
- pytest follows the principle of 'assert'-ing things that are true in order for a test to pass. 

### Exceptions
- Used to check what happens when things go wrong. 
- Define how your program handles errors or unintended inputs. 

### Parameterised Tests
- Create different test cases for all the inputs provided. 
- Make sure to initalise packages to use them in other folders. 

### Fixtures
- Arrange and prepare data before running tests.
- Reusable code! 
- Fixture Scopes: function, class, module, package, session (when to destroy the fixture, free the memory when you no longer need it)

# File Handling 
- Read and write data from and to files respectively. 
- Open, read or write, close the file. Very important to close the file. 
- 'with' statement: automatically closes a file when you're done with it.

## Different File Types
- CSV files
- JSON files

