def reward_function(params):
    wp = params['closest_waypoints'][1]
    speed = params['speed']

    # Check if the car is between waypoints 59 and 81
    if 59 <= wp <= 81:
        # Check if the car's speed is greater than or equal to 2
        if speed >= 2:
            return 0.003  # Return zero_val
        else:
            return speed  # Return the current speed
    else:
        # If the car is not between waypoints 59 and 81, return a low reward
        return 0.001
