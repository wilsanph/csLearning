

import math
import random

def book_binarySearch( data, target, low, high ) :
    
    if low > high :
        return -1
    else :
        mid = ( low + high ) // 2

        if target == data[mid] :
            return mid

        elif target < data[mid] :
            high = mid - 1
            return book_binarySearch( data, target, low, high )
        else :
            low = mid + 1
            return book_binarySearch( data, target, low, high )

def binarySearch( sortedArray, x ) :
    
    leftIndx = 0
    rightIndx = len( sortedArray ) - 1

    if ( len( sortedArray ) == 0 ) :
        return -1

    if ( len( sortedArray ) == 1 ) :
        if ( sortedArray[0] == x ) :
            return 0
        else :
            return -1

    while True :        

        testIndx = int( ( leftIndx + rightIndx ) / 2 )

        if ( leftIndx == testIndx ) or ( rightIndx == testIndx ) :
            if ( x == sortedArray[leftIndx] ) :
                return leftIndx
            elif ( x == sortedArray[rightIndx] ) :
                return rightIndx
            else :
                return -1

        if ( x == sortedArray[testIndx] ) :
            return testIndx

        elif ( x > sortedArray[testIndx] ) :
            leftIndx = testIndx

        else :
            rightIndx = testIndx
        
    return -1

maxLen = 20

## testArray = [ random.randint( 1, maxLen ) for q in range( maxLen ) ]
## testArray = [ 1, 4, 3, 1, 5, 8, 2, 2, 3, 5, 9, 10, 7, 6, 5 ]
testArray = [ 2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37 ]
testArray.sort()


print 'array: ' , testArray
for q in range( 40 ) :
    print 'bs(' + str( q + 1 ) + '): ', binarySearch( testArray, q + 1 )
    print 'bs(' + str( q + 1 ) + '): ', book_binarySearch( testArray, q + 1, 0, len( testArray ) - 1 )
