


def unique_bad( data, start, stop ) :
    
    if stop - start <= 1 : return True
    elif not unique_bad( data, start, stop - 1 ) : return False
    elif not unique_bad( data, start + 1, stop ) : return False
    else: return data[start] != data[stop]


def unique_n2( data ) :

    for p in range( len( data ) ) :

        for q in range( p + 1, len( data ) ) : 
        
            if ( data[p] == data[q] ) :
                return False

    return True


def unique_sort( data ) :
    
    data.sort()

    for q in range( 1, len( data ) ) :
        
        if ( data[q - 1] == data[q] ) :
            return False
    
    return True


maxLen = 25
testData = [ q + 1 for q in range( maxLen ) ]
testData.append( maxLen // 2 )

## print testData
## print 'hasUniqueElements: ' , unique_bad( testData, 0, maxLen - 1 )
## print 'hasUniqueElements: ' , unique_n2( testData )
## print 'hasUniqueElements: ' , unique_sort( testData )



def bad_fibonacci( n ) :

    if ( n == 1 or n == 0 ) : 
        return 1

    else :
        return bad_fibonacci( n - 1 ) + bad_fibonacci( n -2 )
    

def good_fibonacci( n ) :

    if n <= 1 : 
        return ( n, 0 )

    else :
        ( a, b ) = good_fibonacci( n - 1 )
        return ( a + b, a )


print 'fibonacci calculation'
fiboTarget = 35
print 'f(100): ' , bad_fibonacci( fiboTarget )
print 'f(100): ' , good_fibonacci( fiboTarget + 1 )
