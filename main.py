#!/usr/bin/env python

def display_menu():
    print '************************************'
    print '|      welcom use the tools        |'
    print '|choose:1~5 function,q or Q is Exit|'
    print '|1.input member                    |'
    print '|2.print list                      |'
    print '|3.find member                     |'
    print '|4.delete member                   |'
    print '|5.modify member                   |'
    print '************************************'



def input_func():
    name = raw_input("input name:")
    number = raw_input("input number:")
    classmates = [name, number]

    print 'your input is:'
    print classmates[0]
    print classmates[1]

    return  classmates

if __name__=='__main__':
    display_menu()
    while 1 :
        choose = raw_input("please input your choose:")
        if choose == 'Q' or choose == 'q':
            print 'your choose: exit'
            exit()
        elif choose == '1':
            print 'choose:1.input member'
            input_func()
        elif choose == '2':
            print 'choose:2.print list'
        elif choose == '3':
            print 'choose:3.find member'
        elif choose == '4':
            print 'choose:4.delete mamber'
        elif choose == '5':
            print 'choose:5.modify member'
        else :
            print 'your input error,please input again'


