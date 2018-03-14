#cription: --a description of your program--
# Final Project term: winter 2018
#
# Name: Kuan Lin
# SID: 089988
# Course Name: cpsc111BV
#
# Name: --your name--
# SID: --your Studentid--
# Course Name: --your course number--
#
# Date created:
# Date last modified:
import sys
def main():
    input_name = input('Enter name of input file: ')
    output_name = input('Enter name of output file: ')
    if input_name == output_name:
        print('The name of two file cannot be the same.')
        sys.exit(1)
    return True
main()

'''def isMagic():
    filename = input('input a file: ')
    file = open(filename, 'r')
    for line in file:
        read'''
