from termcolor import colored
def wise():
    def WISE():
        def test3():
            def test2():
                def test():
                    def main():

                        menuochoice = 0            	
                        wronganswer = 0                 

                        if menuochoice != 2:            	

                            print('Enter the dungeon... or run away?\n')
                            print('1)The Four Wise Ones.')
                            print('2)Quit\n')                        

                        themodchoice = int(input('Enter your choice here:'))
                        if themodchoice ==1:
                            
                            print('nHi! My children: Module, Keyword, Symbol, and Topic are really hungry. The more they know the more they grow ... So if you answer a few simple questions they will be well nourished and one day, they will be able to help you a lot more than you could have ever imagined.\n But...\n First we must feast!')
                            print('')
                            
                                   
                            print('Which of the following is not a python module?\n')

                            print('1)inspect')
                            print('2)select')
                            print('3)elif')
                            print('4)string')  

                            thechoice = int(input('\nEnter your choice here: '))

                            if thechoice != 3:

                                        print(colored('\nWrong!','red'))
                                        print('\nTry the next one.')
                                        wronganswer += 1										
                            else:
                                        print(colored('\nCorrect!','green'))
                                        print('\nThanks Im stuffed!')
                                        print('\nNext time I will be a lot smarter thanks to you!')


                            print('Which of the following is a python module?\n')

                            print('1)random')
                            print('2)except')
                            print('3)import')
                            print('4)return')  

                            thechoice = int(input('\nEnter your choice here: '))

                            if thechoice != 1:

                                        print(colored('\nWrong!','red'))
                                        print('\nTry the next one.')
                                        wronganswer += 1

                            else:
                                        print(colored('\nCorrect!','green'))
                                        print('\nThanks Im stuffed!')
                                        print('\nNext time I will be a lot smarter thanks to you!')

                            print('\nWhat does != mean in python')
                            print('1)addition of a and b')
                            print('2)a is equal to b')
                            print('3)a divided by b')
                            print('4)a is not equal to b')

                            thechoice = int(input('\nEnter your choice here: '))

                            if thechoice != 4:
                                        print(colored('\nWrong!','red'))
                                        print('\nNext time I will be a lot smarter thanks to you!')
                                        wronganswer += 1                                        
                            elif thechoice == 4:
                                        print(colored('\nCorrect!','green'))
                                        print('\nNext time I will be a lot smarter thanks to you!') 

                            print('What does the python module “array” mean?\n')

                            print('1)Defines an object type which can efficiently represent a collection of basic values like characters, integers, and floating point numbers.')
                            print('2)Executable statement that defines a clasobject')
                            print('3) A disassembler of python byte code intmnemonics')
                            print('4)A multi-producer, multi-consumer queue')  

                            thechoice = int(input('\nEnter your choice here: '))

                            if thechoice != 1:

                                        print(colored('\nWrong!','red'))
                                        print('\nTry the next one.')
                                        wronganswer += 1
                            elif thechoice == 1:
                                        print(colored('\nCorrect!','green'))
                                        print('\nNext time I will be a lot smarter thanks to you!') 

                            print('What is a list in python\n')

                            print('1)collection which is unordered and unindexed. No duplicate members')
                            print('2) collection which is ordered and changeable. Allows duplicate members')
                            print('3)collection which is ordered and unchangeable. Allows duplicate members.')
                            print('4)collection which is unordered, changeable and indexed. No duplicate members')  

                            thechoice = int(input('\nEnter your choice here: '))

                            if thechoice != 2:
                                        print(colored('\nWrong!','red'))
                                        print('\nTry the next one.')
                                        wronganswer += 1
                            elif thechoice == 2:
                                        print(colored('\nCorrect!','green'))
                                        print('\nNext time I will be a lot smarter thanks to you!') 

                            print('What does break mean in python?\n')
 
                            print('1)It stops the code from executing for 10 seconds')
                            print('2)It signifies the start of a new line')
                            print('3)It irreversibly breaks the program')
                            print('4)It terminates the current loop and resumes execution at the next statement')  

                            thechoice = int(input('\nEnter your choice here: '))

                            if thechoice != 4:

                                        print(colored('\nWrong!','red'))
                                        print('\nTry the next one.')
                                        wronganswer += 1
                            elif thechoice == 4:
                                        print(colored('\nCorrect!','green'))										
                                        print("Thanks!I'm stuffed")
                                        print('\nNext time I will be a lot smarter thanks to you!')        		
                                        
                            print('Last question! What is not one of the 4 essential parts of a computer?\n')

                            print('1)voltage')
                            print('2)HDD')
                            print('3)processors')
                            print('4)motherboard')  

                            thechoice = int(input('\nEnter your choice here: '))

                            if thechoice != 2:

                                        print(colored('\nWrong!','red'))
                                        print('\nTry the next one.')
                                        wronganswer += 1                                        
                            elif thechoice == 2:
                                        print(colored('\nCorrect!','green'))										
                                        print("Thanks!I'm stuffed")
                                        print('\nNext time I will be a lot smarter thanks to you!')     
												
                                       
                    def method_name():
                        return main()
                    
                    def quit():
                        return method_name()
                    
                    quit()
                    return main, method_name, quit
                
                main, method_name, quit = test()
                return test
            
            test = test2()
            return test, test2
        
        test, test2 = test3()
        return test3
    
    test3 = WISE()
    return WISE, test3

WISE, test3 = wise()