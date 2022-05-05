import random
import math

# Globals
my_dots = {}
food_assigned = {}
countFlocked = 0
numDots = 1
attacking = 0
flocked = 0
foodSeekLimit = 60

def init():
    return("😎")

def run(db_cursor , state):
    global my_dots
    global food_assigned
    global numDots
    global attacking
    global foodSeekLimit
    global flocked
    #get all my dots
    rows = db_cursor.execute(f"select x,y from main_game_field as gf, owner  where is_flag = FALSE and gf.owner_id = owner.owner_id and owner.name = '{state['NAME']}'")

    if numDots >= foodSeekLimit:
        attacking = 1
        food_assigned = {}
        if foodSeekLimit < 60:
            foodSeekLimit += 1
    else:
        attacking = 0

    if not attacking:
        flocked = 0
        foodSeekState(db_cursor, rows)
    else:
        flockState(db_cursor, state, rows)

def flockState(db_cursor, state, rows):
    prevDot = ()
    flockPattern = [(-2,2), (-1,2), (0,2), (-2,1), (-1,1), (0,1), (-2,0), (-1,0), (-2,-1), (-1,-1), (0,-1), (-2,-2), (-1,-2), (0,-2)]
    global numDots
    global countFlocked
    global flocked
    global my_dots
    global foodSeekLimit
    currDots = {}
    rows = rows.fetchall()
    myFlag = db_cursor.execute(f"select x,y from main_game_field as gf, owner where is_flag = TRUE and gf.owner_id = owner.owner_id and owner.name = '{state['NAME']}'").fetchone()
    enemies = db_cursor.execute(f"select x,y from main_game_field as gf, owner where is_flag = FALSE and gf.owner_id = owner.owner_id and owner.name != '{state['NAME']}'and owner.name != 'Food'")
    enemy = enemies.fetchone()
    count = 0

    if countFlocked > numDots/2 and not flocked:
        flocked = 1
        my_dots = {}
    else:
        countFlocked = 0

    for row in rows:
        count+=1
        if prevDot == ():
            if not flocked:
                currentSeek = (myFlag[0], myFlag[1]-2)
            else:
                if enemy != None:
                    currentSeek = (enemy[0], enemy[1])
                else: 
                    currentSeek = (myFlag[0], myFlag[1]-2)
        elif (row[0], row[1]) not in my_dots or flocked:
            formMultiple = (count // 14) + 1
            formMod = count % 14
            currentSeek = (prevDot[0] + (flockPattern[formMod][0]*formMultiple),prevDot[1]+flockPattern[formMod][1])
        else:
            currentSeek = my_dots[(row[0],row[1])]

        currDots[(row[0],row[1])] = currentSeek
        
        prevDot = (row[0],row[1])
        if currentSeek != ():
            offset = getOffset(row[0], row[1], currentSeek[0], currentSeek[1])

        if (row[0], row[1]) != currentSeek and (row[0] + offset[0], row[1] + offset[1]) not in my_dots:
            db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0] + offset[0] }, {row[1] + offset[1] }, 'MOVE')")
            del currDots[(row[0], row[1])]
            currDots[ (row[0] + offset[0], row[1] + offset[1]) ] = currentSeek
            if (row[0], row[1]) in my_dots:
                del my_dots[(row[0], row[1])]
            my_dots[ (row[0] + offset[0], row[1] + offset[1]) ] = currentSeek
        elif (row[0], row[1]) == currentSeek:
            countFlocked += 1

    numDots = count
    my_dots = currDots


def foodSeekState(db_cursor, rows):
    global numDots
    global my_dots
    global countFlocked
    global foodSeekLimit
    currDots = {}
    count = 0
    for row in rows.fetchall():
        count += 1
        if (row[0],row[1]) not in my_dots or (row[0],row[1]) == my_dots[ (row[0],row[1]) ]:
            my_dots[ (row[0],row[1]) ] = seekFood(db_cursor, row[0], row[1])

        currentSeek = my_dots[ (row[0],row[1])]
        if currentSeek != ():
            offset = getOffset(row[0], row[1], currentSeek[0], currentSeek[1])
        else:
            foodSeekLimit -= 2
            offset = [random.choice([0,1,-1]), random.choice([0,1,-1])]
            
        if (row[0] + offset[0], row[1] + offset[1]) not in my_dots:
            db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0] + offset[0] }, {row[1] + offset[1] }, 'MOVE')")
            currDots[ (row[0] + offset[0], row[1] + offset[1]) ] = currentSeek
        else:
            currDots[ (row[0], row[1]) ] = currentSeek
    my_dots = currDots

    numDots = count


def getOffset(curX, curY, toX, toY):
    deltaX = toX - curX
    deltaY = toY - curY
    res = [0,0]

    if deltaX < 0:
        res[0] = -1
    elif deltaX > 0:
        res[0] = 1

    if deltaY < 0:
        res[1] = -1
    elif deltaY > 0:
        res[1] = 1

    return res

def seekFood(db_cursor, x, y):
    global food_assigned
    global my_dots
    currentFood = ()
    mDistance = 9999
    foodCursor = db_cursor.execute(f"select x,y from main_game_field where x >= {x-50} and x <= {x+50} and y >= {y-25} and y <= {y+25} and owner_id = (select owner_id from owner where name='Food')")

    for food in foodCursor.fetchall():
        newDistance = abs(math.dist([food[0], food[1]], [x, y]))
        if newDistance < mDistance and newDistance != 0 and (food[0], food[1]) not in food_assigned:
            currentFood = (food[0], food[1])
            mDistance = newDistance
    
    food_assigned[currentFood] = 1
    return currentFood