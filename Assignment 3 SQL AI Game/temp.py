 for i in range(50):
        seekX = seekX + 1
        seekY = y - 25
        if seekX < 0:
            seekX = 0
        if seekY < 0:
            seekY = 0
        for j in range(50):
            seekY = seekY + 1
            foodCursor = db_cursor.execute(f"select x,y from main_game_field where x = {seekX} and y = {seekY} and owner_id = (select owner_id from owner where name='Food')")
            food = foodCursor.fetchone()
            
            if food != None:
                newDistance = abs(math.dist([seekX, seekY], [x, y]))
                if newDistance < mDistance and (seekX, seekY) not in food_assigned:
                    currentFood = (seekX, seekY)
                    mDistance = newDistance