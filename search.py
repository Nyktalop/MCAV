from utils import *

def exhaustive_tile(tile, im, fenDim=16) :
    center = tile.center
    negT, posT = tile.shape[0]//2, (tile.shape[0]-1)//2
    negF, posF = fenDim//2, (fenDim-1)//2

    bestX, bestY = center
    bestMSE = np.inf

    for x in range( clamp(center[0]-negF, negT, im.shape[0]-posT), clamp(center[0]+posF, negT, im.shape[0]-posT)) :
        for y in range( clamp(center[1]-negF, negT, im.shape[1]-posT), clamp(center[1]+posF, negT, im.shape[1]-posT)) :

            score = tile.mse(im[x-negT:x+posT+1,y-negT:y+posT+1])

            if score < bestMSE :
                bestMSE = score
                bestX = x
                bestY = y


    return bestX, bestY

def log2D_tile(tile, im, fenDim=16) :
    step = 1+(fenDim//4)
    x,y = tile.center
    negT, posT = tile.shape[0]//2, (tile.shape[0]-1)//2

    best_previousMSE = np.inf

    while step > 0 :
        score = tile.mse(im[x - negT:x + posT + 1, y - negT:y + posT + 1])
        bestMSE = score
        bestX = x
        bestY = y


        if(y-step-negT > 0):
            score = tile.mse(im[x - negT:x + posT + 1, y - step - negT:y - step + posT + 1])
            if score < bestMSE :
                bestMSE = score
                bestX = x
                bestY = y - step
        if(x-step-negT > 0) :
            score = tile.mse(im[x - step - negT:x - step + posT + 1, y - negT:y + posT + 1])
            if score < bestMSE:
                bestMSE = score
                bestX = x - step
                bestY = y
        if(x+step+posT < im.shape[0]) :
            score = tile.mse(im[x + step - negT:x + step + posT + 1, y - negT:y + posT + 1])
            if score < bestMSE:
                bestMSE = score
                bestX = x + step
                bestY = y
        if(y+step+posT < im.shape[1]):
            score = tile.mse(im[x - negT:x + posT + 1, y + step - negT:y + step + posT + 1])
            if score < bestMSE :
                bestMSE = score
                bestX = x
                bestY = y + step

        if bestMSE < best_previousMSE :
            best_previousMSE = bestMSE
            x,y = bestX, bestY


        step = step//2

    return x,y

def unalafois_tile(tile, im, fenDim=16):
    negT, posT = tile.shape[0] // 2, (tile.shape[0] - 1) // 2
    x, y = tile.center
    Bx, By = x, y
    totalDecX = 0
    totalDecY = 0

    #Do
    score = tile.mse(im[x - negT:x + posT + 1, y - negT:y + posT + 1])
    bestMSE = score

    if (x-1-negT > 0):
        score = tile.mse(im[x - 1 - negT:x + posT, y - negT:y + posT + 1])
        if score < bestMSE :
            bestMSE = score
            Bx = x - 1
            totalDecX -= 1

    if (x+1+posT < im.shape[0]):
        score = tile.mse(im[x+1-negT:x+posT+2,y-negT:y+posT+1])
        if score < bestMSE :
            bestMSE = score
            Bx = x + 1
            totalDecX += 1

    #While
    while(Bx != x) :
        print(Bx, x)
        x = Bx
        score = tile.mse(im[x - negT:x + posT + 1, y - negT:y + posT + 1])
        bestMSE = score

        if (x - 1 - negT > 0 and totalDecX-negT > -(fenDim//2)):
            score = tile.mse(im[x - 1 - negT:x + posT, y - negT:y + posT + 1])
            if score < bestMSE:
                bestMSE = score
                Bx = x - 1
                totalDecX -= 1

        if (x + 1 + posT < im.shape[0] and totalDecX+posT < fenDim//2 ):
            score = tile.mse(im[x + 1 - negT:x + posT + 2, y - negT:y + posT + 1])
            if score < bestMSE:
                bestMSE = score
                Bx = x + 1
                totalDecX += 1

    print("--------")
    #Do

    score = tile.mse(im[x - negT:x + posT + 1, y - negT:y + posT + 1])
    bestMSE = score

    if (y-1-negT > 0):
        score = tile.mse(im[x - negT:x + posT + 1 , y - 1 - negT:y + posT])
        if score < bestMSE :
            bestMSE = score
            By = y - 1
            totalDecY -= 1

    if (y+1+posT < im.shape[0]):
        score = tile.mse(im[x-negT:x+posT+1,y-negT+1:y+posT+2])
        if score < bestMSE :
            bestMSE = score
            By = y + 1
            totalDecY += 1

    #While
    while(By != y) :
        y = By
        score = tile.mse(im[x - negT:x + posT + 1, y - negT:y + posT + 1])
        bestMSE = score

        if (y - 1 - negT > 0 and totalDecY-negT > -(fenDim//2)):
            score = tile.mse(im[x - negT:x + posT + 1, y - 1 - negT:y + posT])
            if score < bestMSE:
                bestMSE = score
                By = y - 1
                totalDecY -= 1

        if (y + 1 + posT < im.shape[0] and totalDecY+posT < fenDim//2):
            score = tile.mse(im[x - negT:x + posT + 1, y - negT + 1:y + posT + 2])
            if score < bestMSE:
                bestMSE = score
                By = y + 1
                totalDecY += 1

    return x, y