# Code Review

## Video segments
### (5 minutes each)
- [Code Review 1](/index.md)
- [Code Review 2](/index.md)
- [Code Review 3](/index.md)
- [Code Review 4](/index.md)

## Summary notes:
```markdown
Structure
- Does the code completely and correctly implement the design?
	The purpose of this code was to create a simple menu system to maintain two small databases for a zoo.
	One database for Animal data and another for Habitat data.  This code does address this request completely
	and correctly.

- Does the code conform to any pertinent coding standards?
	The code includes appropriate naming conventions, indentations and commenting throughout

- Is the code well-structured, consistent in style, and consistently formatted?
	The code has a consistent style and the formatting is neat, easy to read and consistent

- Are there any uncalled-for or unneeded procedures or any unreachable code?
	There are a number of similar procedures between the Animal and Habitat data handling that could
	potentially be refined or combined in some situations within this code.  There does not appear to be
	any uncalled-for procedures or any unreachable code in this project.

- Are there any leftover stubs or test routines in the code?
	There does not appear to be any left over stubs or test routines in this code.

- Can any code be replaced by calls to external reusable components or library functions?
	A large amount of the code uses external reusable components for both Animal and Habitat data handling
	The menu generation and file loading procedures coule be externalized, particularly when considering
	expanding the system with an additional data base for personel

- Are there any blocks of repeated code that could be condensed into a single procedure?
	Two portions of code are very similar and handle the creation of the two menus for Animals and Habitat
	these two aspects of code could be consensed into a single procedure potentially

- Is storage use efficient?
	Most of the storage is handled within text files, this is less efficient than it should be but the project is
	currently very small.  Considering scalablity this may need to be addressed.
	
- Are symbolics used rather than “magic number” constants or string constants?
     There are no instances of this in the code.

- Are any modules excessively complex and should be restructured or split into multiple routines?
	Most of the program is simple in nature, some areas may benefit from a restructure, particularly the
	menu generating code portion.

Documentation
- Is the code clearly and adequately documented with an easy-to-maintain commenting style?
	Documentation is well commented throughout the code and makes sense.  Some comments may
	be unnecessary
	
- Are all comments consistent with the code?
	Comments are consistent throughout the code

Variables
- Are all variables properly defined with meaningful, consistent, and clear names?
	Most of the variables have meaning for the code and are properly defined.  There was one instance where
	'temp' was used instead of 'temperature' which could be confusing.   The variables may need to be reworked
	to confine to code standards, despite being easily read and understood.

- Do all assigned variables have proper type consistency or casting?
	Variables used have proper type consistency or casting where needed

- Are there any redundant or unused variables?
	There were no unused variables and no redunant variables were found	

Arithmetic Operations
- Does the code avoid comparing floating-point numbers for equality?
	This code avoids comparing floating-point numbers for equality

- Does the code systematically prevent rounding errors?
	The code does not contain rounding errors

- Does the code avoid additions and subtractions on numbers with greatly different magnitudes?
	The code does not add or subtract numbers with greatly different magnitudes

- Are divisors tested for zero or noise?
	Divisors tested with zero are present

Loops and Branches
- Are all loops, branches, and logic constructs complete, correct, and properly nested?
	Loops and branches are correctly nested

- Are the most common cases tested first in IF- -ELSEIF chains?
	Common cases and user input are tested with IF/ELSEIF chains

- Are all cases covered in an IF- -ELSEIF or CASE block, including ELSE or DEFAULT clauses?
	File handling ensures a default file, user input switches utilize default clauses, if statements address
	user input errors
	
- Does every case statement have a default?
	Yes

- Are loop termination conditions obvious and invariably achievable?
	Loops used reference EOF and are attainable

- Are indexes or subscripts properly initialized, just prior to the loop?
	Yes

- Can any statements that are enclosed within loops be placed outside the loops?
	Loops contain minimal statements

- Does the code in the loop avoid manipulating the index variable or using it upon exit from the loop?
	Loops do not appear to maniuplate the index variable or use it upon exiting the loop

Defensive Programming
- Are indexes, pointers, and subscripts tested against array, record, or file bounds?
	File bounds are addressed and tested in this code

- Are imported data and input arguments tested for validity and completeness?
	Imported file data is not tested, user input data is tested for validity

- Are all output variables assigned?
	Most output does not utilize variables in this code

- Are the correct data operated on in each statement?
	Correct data is operated on within each statement

- Is every memory allocation deallocated?
	Memory is not deallocated fully

- Are timeouts or error traps used for external device accesses?
	There is no external device access for this program

- Are files checked for existence before attempting to access them?
	Files are checked for existence before attempting to access them

- Are all files and devices left in the correct state upon program termination?
	Files are closed prior to terminating the program
```
