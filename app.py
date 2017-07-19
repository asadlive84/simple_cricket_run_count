# simple_cricket_run_count

'''
    Simple App for count run per over
    Asaduzzaman Sohel / twitter: asadlive84
'''
print("Please type your over!!!")
while True:
    try:
        total_over=int(input())
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

for over in range(1,total_over+1):
    bowl=1
    run=0
    run1=0
    bowl1='first'
    no_ball_count=0

    while bowl <= 6:
        print("Bowl no %s" % (bowl))
        print("NO/WIDE Ball??? please, type 'NO' or 'YES' ")

        no_ball=input()
        if no_ball == 'YES' or no_ball == 'yes':
            if bowl1 == 'first':
                bowl-=1
                run1+=1
                bowl1='repeat'

            elif bowl1 == 'repeat':
                run1+=1

            no_ball_count+=1
            bowl1='repeat'

            print("Do you want to add any extra run??")

            try:
                extra_run=int(input())
                run1+=extra_run
            except ValueError:
                print("Oops!  That was no valid number.  Try again...")

            print("Run add extra ONE and and run is %s" % run1)

        else:
            print("Add Your Ran!!! ")
            while True:
                try:
                    run=int(input())
                    break
                except ValueError:
                    print("Oops!  That was no valid Run.  Try again...")
            bowl+=1
            run1+=run
            bowl1='first'
            print("Run is %s" % run1)

        print("====================================================================")
       
    print("End %d over" % over)
    print("Total Run is %d and no ball this over : %d" % (run1,no_ball_count))
    print("====================================================================")
    print("====================================================================")

print("Thanks for using this software")
