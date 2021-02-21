# Software Design & Engineering

[Home](/index.md)

## Project Summary
The program showcasing my Software Develop and Design skill sets is my Humidity and temperature monitoring system created for the Raspberry Pi using a variety of sensors programmed in Python.  The original design for this was to use a light sensor to initiate readings during daylight hours on the half hour (I used seconds instead of hours for quicker testing).   While running during day time, the program would sense the daylight levels, then if the threshold is met, would read temperature and humidity every 30 seconds (30 minutes).
I decided an improvement upon this would be to allow the user to bypass the daylight settings and instead have the monitoring system run for an allotted period of time.  I updated the program to run the same sequences and code as before, using a series of boolean checks to signify whether the user had input any duration or chosen the standard operating methods.
	During this process there were a number of minor logical situations to think through using the pseudo code prepared earlier.  I didn’t want to create duplicate code which would have been the easiest solution, but not very efficient.  Instead I chose to have the user input whether they wanted to use the standard monitoring system or utilize a duration period instead.  Then, updated the while loops to act accordingly with more advanced logic statements incorporating additional checks and booleans for which state the user had selected.
	Future iterations of this program would be improved with additional error checking and perhaps a menu system for the user to input options for monitoring.  The initial design goals were met and the program functions now with the option of entering a duration or using the original set parameters designed.

## Project Files
- [Video Demonstration](/CS350_Final_Project/video
- [Webpage Data Chart](/CS350_Final_Project/CS350_Final_Project.html)
- [JSON Data File](/CS350_Final_Project/station.json)
- Python Files: [Project](/CS350_Final_Project/CS350_Final_Project.py) [Revised Project](/CS350_Final_Project/CS350_Final_Project_Revised.py)
