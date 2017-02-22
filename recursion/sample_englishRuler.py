
def drawLine( length, markStr = '' ) :
    strTicks = '-' * length

    if markStr != '' :
        strTicks += ' ' + markStr

    print strTicks

def drawInterval( tickLength ) :
    if tickLength > 0 :
        drawInterval( tickLength - 1 )
        drawLine( tickLength )
        drawInterval( tickLength - 1 )

def drawEnglishRuler( majorTickLength, inchesCount ) :
    drawLine( majorTickLength, str( 0 ) )

    for q in range( inchesCount ) :
        drawInterval( majorTickLength - 1 )
        drawLine( majorTickLength, str( q + 1 ) )
    

drawEnglishRuler( 8, 4 )
