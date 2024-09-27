'''
2)Write a program to check whether the given character is vowel or consonant.
Input format:
The input consist of a character
Output format:
The output consists of a below-given string
“Vowel” / “Consonant” / “Not an alphabet”
Sample Input:
e

Sample Output:
Vowel
'''

Answer:
x=str(input())
if(x=='a' or x=='e' or x=='i' or x=='o' or x=='u'):
    print('vowel')
else:
    print('consonant')

Output:
e
vowel
