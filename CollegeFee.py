'''

5) 
Write a program to determine the fee amount to be collected from a student. 
Refer the table below for fee details.
  Student Type  
  Student Type denoted as  
  Fee Details  
Merit Seat Day Scholar
MSDS

Tuition fee + Bus fee



Merit Seat Hosteller
MSH
Tuition fee + Hostel fee

Management Seat Day Scholar



MGSDS

150% of Tuition fee + Bus fee



Management Seat Hosteller
MGSH

150% of Tuition fee + Hostel fee




Input format:
The first input corresponds to the student type
The second input corresponds to the tuition fee
The third input corresponds to the bus fee or hostel fees
Output format:
Print the total fee amount of the corresponding student with 2 decimal places.
Refer below sample output for formatting
Sample Input:
MSH
40000
50000
Sample Output:
90000.00

''''


Answer:

stype=str(input())
tfee=float(input())
hostelorbus=float(input())
if(stype=='MSDS'):
    print(tfee+hostelorbus)
elif(stype=='MSH'):
    print(tfee+hostelorbus)
elif(stype=='MGSDS'):
    print(tfee+(0.50*tfee)+hostelorbus)
elif(stype=='MGSH'):
    print(tfee+(0.50*tfee)+hostelorbus)
else:
    print('Invalid course')

OUTPUT:
MSDS
40000
50000
90000.00
