import sys



bitmap=""" ....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        
                   
                   **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
...................................................................."""


print('Welcome to Bitmap Display')
print('Input the messege you want ot Display')
messege=input('>')
if messege== '':
    sys.exit()

for line in bitmap.splitlines():
    for i,bit in enumerate(line):
        if bit==' ':
            print(' ',end='')
        else:
            print(messege[i % len(messege)], end=' ')
    print()









